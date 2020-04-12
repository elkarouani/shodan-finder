from shodan_finder import ShodanFinder

shodan_instance = ShodanFinder(['adacis.com', 'google.com', 'facebook.net'])

shodan_instance.setAPIKey("tedoHTagcSRqQm9LhIzUCqIqUvI06dHz")

sites_services = shodan_instance.shodanProcedure()

shodan_instance.printDocument(sites_services)