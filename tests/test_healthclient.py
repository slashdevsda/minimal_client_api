import unittest
from algolia_minimal.health import HealthClient, RequestException


class TestStatusMethods(unittest.TestCase):
    def setUp(self):
        self.client = HealthClient.create('', '')
        
    def test_simple(self):
        st = self.client.status()
        self.assertIs(type(st), dict)

    def test_no_existing_host(self):
        with self.assertRaises(RequestException):
            st = self.client.status('nonexist.ha.ovh.net')


class TestIncidentMethods(unittest.TestCase):
    def setUp(self):
        self.client = HealthClient.create('', '')
        
    def test_filter(self):
        # may flak at some point :)
        st = self.client.incidents('c7-eu')
        self.assertIs(type(st), dict)
        
    def test_simple(self):
        st = self.client.incidents()
        self.assertIs(type(st), dict)
        
    def test_no_existing_host(self):
        with self.assertRaises(RequestException):
            st = self.client.incidents('nonexist.ha.ovh.net')
            


if __name__ == '__main__':
    unittest.main()
