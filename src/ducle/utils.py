import click
import ijson
import json
import enum
import os


class SearchType(enum.Enum):
    USER = 1
    TICKET = 2
    ORGANIZATION = 3


def _get_file_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
    data_dir = os.path.normpath(os.path.join(current_dir, '../../data'))
    file_path = data_dir + '/' + file_name
    return file_path


def _match_value(value1, value2):
    if value1 == value2:
        return True
    else:
        if isinstance(value1, bool) and isinstance(value2, bool):
            return value1 == value2
        elif value1 is True and value2 in ('True', 'true'):
            return True
        elif value1 is False and value2 in ('False', 'false'):
            return True
        elif isinstance(value1, int) and isinstance(value2, str) and value1 == int(value2):
            return True
        elif isinstance(value1, list) and isinstance(value2, str) and json.dumps(value1) == value2:
            return True
        else:
            return False


def _open_users_json():
    try:
        file_path = _get_file_path('users.json')
        return open(file_path, 'rb')
    except FileNotFoundError as ex:
        raise Exception('Invalid User JSON file')


def _extract_users_data(term, value):
    result = []
    with _open_users_json() as input_file:
        user_data = ijson.items(input_file, 'item')
        for user_item in user_data:
            if _match_value(user_item.get(term), value):
                result.append(user_item)
            elif isinstance(value, list) and user_item.get(term) in value:   # value is a list
                result.append(user_item)

    return result


def _open_organizations_json():
    try:
        file_path = _get_file_path('organizations.json')
        return open(file_path, 'rb')
    except FileNotFoundError as ex:
        raise Exception('Invalid Organization JSON file')


def _extract_organizations_data(term, value):
    result = []
    with _open_organizations_json() as input_file:
        organization_data = ijson.items(input_file, 'item')
        for org_item in organization_data:
            if _match_value(org_item.get(term), value):
                result.append(org_item)
            elif isinstance(value, list) and org_item.get(term) in value:   # value is a list
                result.append(org_item)

    return result


def _open_tickets_json():
    try:
        file_path = _get_file_path('tickets.json')
        return open(file_path, 'rb')
    except FileNotFoundError as ex:
        raise Exception('Invalid Tickets JSON file')


def _extract_tickets_data(term, value):
    result = []
    with _open_tickets_json() as input_file:
        ticket_data = ijson.items(input_file, 'item')
        for ticket_item in ticket_data:
            if _match_value(ticket_item.get(term), value):
                result.append(ticket_item)
            elif isinstance(value, list) and ticket_item.get(term) in value:  # value is a list
                result.append(ticket_item)

    return result


def _format_user(user_items: list):
    organization_ids = [int(item.get('organization_id')) for item in user_items if item.get('organization_id')]
    orgs = _extract_organizations_data('_id', organization_ids)

    user_ids = [int(item.get('_id')) for item in user_items if item.get('_id')]
    tmp_tickets = []
    with _open_tickets_json() as input_file:
        ticket_data = ijson.items(input_file, 'item')

        for ticket_item in ticket_data:
            if ticket_item.get('submitter_id') in user_ids:
                tmp_tickets.append(ticket_item)
            if ticket_item.get('assignee_id') in user_ids:
                tmp_tickets.append(ticket_item)

    for user_item in user_items:
        tmp_orgs = list(filter(lambda o: o['_id'] == user_item.get('organization_id'), orgs))
        org_name = tmp_orgs[0].get('name', '') if len(tmp_orgs) > 0 else ''
        user_item['organization_name'] = org_name

        sub_idx, ass_idx = 0, 0

        for ticket_item in tmp_tickets:
            if ticket_item.get('submitter_id') == user_item.get('_id'):
                user_item['submitted_ticket_%s' % sub_idx] = ticket_item.get('subject')
                sub_idx += 1
            elif ticket_item.get('assignee_id') == user_item.get('_id'):
                user_item['assignee_ticket_%s' % ass_idx] = ticket_item.get('subject')
                ass_idx += 1

    return user_items


def _format_organization(organization_items: list):
    organization_ids = [int(item.get('_id')) for item in organization_items if item.get('_id')]
    users = _extract_users_data('organization_id', organization_ids)
    tickets = _extract_tickets_data('organization_id', organization_ids)

    for organization_item in organization_items:
        tmp_users = filter(lambda o: o.get('organization_id') == organization_item['_id'], users)
        for idx, val in enumerate(tmp_users):
            organization_item['user_%s' % idx] = val.get('name')

        tmp_tickets = filter(lambda o: o.get('organization_id') == organization_item['_id'], tickets)
        for idx, val in enumerate(tmp_tickets):
            organization_item['ticket_%s' % idx] = val.get('subject')

    return organization_items


def _format_ticket(ticket_items: list):
    organization_ids = [int(item.get('organization_id')) for item in ticket_items if item.get('organization_id')]
    organization_data = _extract_organizations_data('_id', organization_ids)

    user_ids = []
    for ticket_item in ticket_items:
        if ticket_item.get('assignee_id'):
            user_ids.append(ticket_item.get('assignee_id'))
        if ticket_item.get('submitter_id'):
            user_ids.append(ticket_item.get('submitter_id'))
    user_data = _extract_users_data('_id', user_ids)

    for ticket_item in ticket_items:
        orgs = list(filter(lambda o: o['_id'] == ticket_item.get('organization_id'), organization_data))
        org_name = orgs[0].get('name', '') if len(orgs) > 0 else ''
        ticket_item['organization_name'] = org_name

        for user_item in user_data:
            if user_item.get('_id') == ticket_item.get('assignee_id'):
                ticket_item['assignee_name'] = user_item.get('name')
            elif user_item.get('_id') == ticket_item.get('submitter_id'):
                ticket_item['submitter_name'] = user_item.get('name')

    return ticket_items


def _pretty_print(item_dict: dict):
    string = """"""
    for k, v in item_dict.items():
        string += """%s\t\t\t\t%s\n""" % (str(k).ljust(30), json.dumps(v))

    return string


def search_users(term, value):
    user_items = _extract_users_data(term, value)
    if user_items:
        user_items = _format_user(user_items)
    return user_items


def search_organizations(term, value):
    organization_items = _extract_organizations_data(term, value)
    if organization_items:
        organization_items = _format_organization(organization_items)
    return organization_items


def search_tickets(term, value):
    ticket_items = _extract_tickets_data(term, value)
    if ticket_items:
        ticket_items = _format_ticket(ticket_items)
    return ticket_items


def search_data(search_type, term, value, pretty_print=False):
    search_type = int(search_type)
    result = []
    # search users
    if search_type == SearchType.USER.value:
        result = search_users(term, value)
    # search organizations
    elif search_type == SearchType.ORGANIZATION.value:
        result = search_organizations(term, value)
    # search tickets
    elif search_type == SearchType.TICKET.value:
        result = search_tickets(term, value)

    if result:
        result = list(map(_pretty_print, result))
        if pretty_print:
            click.echo('\n---------------\n')
            for item in result:
                click.echo(item)

    return result
