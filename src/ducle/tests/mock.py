from ijson.compat import BytesIO
from unittest.mock import mock_open
from ducle.tests import dummy


def create_mock_open_users():
    mock_open_users = mock_open()
    mock_open_users.return_value = BytesIO(dummy.dummy_user_data)
    return mock_open_users


def create_mock_open_tickets():
    mock_open_tickets = mock_open()
    mock_open_tickets.return_value = BytesIO(dummy.dummy_ticket_data)
    return mock_open_tickets


def create_mock_open_organizations():
    mock_open_organizations = mock_open()
    mock_open_organizations.return_value = BytesIO(dummy.dummy_organization_data)
    return mock_open_organizations
