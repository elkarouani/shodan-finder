import unittest
from shodan_finder import ShodanFinder
from socket import gaierror

class TestShodanFinder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Starting tests on Shodan Finder Module')
        print('Initializing instances ...')
        cls.shodan_finder_instance  = ShodanFinder(['adacis.com'])
        cls.shodan_finder_instance.extractData('52.58.78.16')

    def test_init(self):
        print('Testing constructor ...')
        self.assertEqual(self.shodan_finder_instance.sites_list, ['adacis.com'])
        self.assertEqual(type(self.shodan_finder_instance.data_instance).__name__, 'dict')

    def test_get_host(self):
        print('Testing get host method ...')
        self.assertEqual(self.shodan_finder_instance.getHost('adacis.com'), '52.58.78.16')
        with self.assertRaises(gaierror):
            self.shodan_finder_instance.getHost('i am not a website')

    def test_extract_data(self):
        print('Testing extract data method ...')
        self.assertEqual(type(self.shodan_finder_instance.data_instance).__name__, 'dict')

    def test_extract_ports_list(self):
        print('Testing extract ports list method ...')
        self.assertEqual(self.shodan_finder_instance.extractPortsList(), [80, 443])

    def test_extract_used_server(self):
        print('Testing extract used server method ...')
        self.assertEqual(self.shodan_finder_instance.extractUsedServer(80), "openresty/1.13.6.2")
        self.shodan_finder_instance.extractData('91.121.82.49')
        self.assertEqual(self.shodan_finder_instance.extractUsedServer(993), "Not Found")
        self.shodan_finder_instance.extractData('52.58.78.16')
        
    def test_extract_bannere(self):
        print('Testing extract bannere method ...')
        self.assertEqual(type(self.shodan_finder_instance.extractBannere(80)).__name__, "str")
    
    def test_extract_technologies(self):
        print('Testing extract technologies method ...')
        self.assertIn(type(self.shodan_finder_instance.extractTechnologies(443)).__name__, ("dict", "str"))
        self.shodan_finder_instance.extractData('91.121.82.49')
        self.assertEqual(self.shodan_finder_instance.extractTechnologies(993), "Not Found")
        self.shodan_finder_instance.extractData('52.58.78.16')

    def test_shodan_procedure(self):
        print('Testing shodan procedure method ...')
        self.assertEqual(type(self.shodan_finder_instance.shodanProcedure()).__name__, "list")

if __name__ == "__main__":
    unittest.main()

