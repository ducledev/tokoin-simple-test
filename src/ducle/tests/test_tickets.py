import unittest
from unittest.mock import patch

from ducle.tests.mock import create_mock_open_tickets, create_mock_open_organizations, create_mock_open_users
from ducle.utils import search_data, SearchType


class TestTicket(unittest.TestCase):
    def setUp(self):
        self.patcher1 = patch('ducle.utils._open_tickets_json', create_mock_open_tickets())
        self.patcher1.start()
        self.patcher2 = patch('ducle.utils._open_organizations_json', create_mock_open_organizations())
        self.patcher2.start()
        self.patcher3 = patch('ducle.utils._open_users_json', create_mock_open_users())
        self.patcher3.start()

    def tearDown(self):
        self.patcher1.stop()
        self.patcher2.stop()
        self.patcher3.stop()

    def test_search_tickets_exist(self):
        result = search_data(SearchType.TICKET.value, '_id', "fc5a8a70-3814-4b17-a6e9-583936fca909")
        self.assertEqual(len(result), 1)

    def test_search_tickets_not_found(self):
        result = search_data(SearchType.TICKET.value, '_id', "abc")
        self.assertEqual(len(result), 0)

    def test_search_tickets_boolean(self):
        result = search_data(SearchType.TICKET.value, 'has_incidents', True)
        self.assertEqual(len(result), 1)

    def test_search_tickets_string(self):
        result = search_data(SearchType.TICKET.value, 'type', "problem")
        self.assertEqual(len(result), 1)

    def test_search_tickets_empty_string(self):
        result = search_data(SearchType.TICKET.value, 'description', "")
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()
