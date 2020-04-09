from shodan_finder import ShodanFinder

shodan_instance = ShodanFinder(['adacis.net', 'google.com', 'facebook.net'])

sites_services = shodan_instance.shodanProcedure()

shodan_instance.printDocument(sites_services)