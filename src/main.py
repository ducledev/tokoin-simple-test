import click

from ducle.utils import search_data, SearchType

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """A simple command line tool."""


def validate_search_type(ctx, param, value):
    try:
        value = int(value)
        if value not in [1, 2, 3]:
            raise ValueError
        return value
    except ValueError:
        raise click.BadParameter('search type must be in the list [1, 2, 3]')


@main.command('search', short_help='Search many objects', options_metavar='[options]')
@click.option('--search_type', metavar='<search_type>', prompt='Select 1) Users or 2) Tickets or 3) Organizations',
              callback=validate_search_type, required=True, help='Note: 1-Users, 2-Tickets, 3-Organizations', type=int)
@click.option('--term', metavar='<term>', prompt='Enter search term', required=True)
@click.option('--value', metavar='<value>', prompt='Enter search value', default='')
def search(search_type, term, value):
    data = search_data(search_type, term, value)
    map_search_type = {
        SearchType.USER.value: 'users',
        SearchType.ORGANIZATION.value: 'organizations',
        SearchType.TICKET.value: 'tickets'
    }
    click.echo('Searching %s for "%s" with a value of "%s"\n' % (map_search_type.get(search_type), term, value))
    for item in data:
        click.echo(item)
    if not data:
        click.echo('No results found')


@main.command('searchable', short_help='List of Searchable fields')
def searchable_fields():
    user_fields = [
        "_id", "url", "external_id", "name", "alias", "created_at", "active", "verified", "shared", "locale",
        "timezone", "last_login_at", "email", "phone", "signature", "organization_id", "tags", "suspended", "role"
    ]
    click.echo('------------------------------------------')
    click.echo('Search Users with')
    for f in user_fields:
        click.echo(f)

    ticket_fields = [
        "_id", "url", "external_id", "created_at", "type", "subject", "description", "priority", "status",
        "submitter_id", "assignee_id", "organization_id", "tags", "has_incidents", "due_at", "via"
    ]
    click.echo('------------------------------------------')
    click.echo('Search Tickets with')
    for f in ticket_fields:
        click.echo(f)

    organization_fields = [
        "_id", "url", "external_id", "name", "domain_names", "created_at", "details", "shared_tickets", "tags"
    ]
    click.echo('------------------------------------------')
    click.echo('Search Organizations with')
    for f in organization_fields:
        click.echo(f)


if __name__ == '__main__':
    main()
