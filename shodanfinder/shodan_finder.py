from re import match
import shodan
from socket import gethostbyname, gaierror

class ShodanFinder :
    API = 'tedoHTagcSRqQm9LhIzUCqIqUvI06dHz'

    def __init__(self, sites):
        self.sites_list = sites
        self.data_instance = {}

    def getHost(self, site):
        if match(r'[a-zA-Z0-9]*.[a-zA-Z0-9]*', site):
            return gethostbyname(site)
        else:
            raise gaierror

    def extractData(self, host):
        api = shodan.Shodan(self.API)
        self.data_instance = api.host(host)

    def extractPortsList(self):
        return self.data_instance['ports']
    
    def extractUsedServer(self, port):
        for port_container in self.data_instance['data']:
            if port_container['port'] == port:
                if not 'http' in port_container or not 'server' in port_container['http'] : return "Not Found"

                return port_container['http']['server']

    def extractBannere(self, port):
        for port_container in self.data_instance['data']:
            if port_container['port'] == port:
                return port_container['data']

    def extractTechnologies(self, port):
        for port_container in self.data_instance['data']:
            if port_container['port'] == port:
                if not 'http' in port_container or not 'components' in port_container['http'] : return "Not Found"
                return port_container['http']['components'] if port_container['http']['components'] != {} else "Not Found"

    def shodanProcedure(self):
        sites_services = []

        for site in self.sites_list:
            try:
                host = self.getHost(site)
                sites_services.append({'name': site})

                self.extractData(host)
                sites_services[len(sites_services) - 1]['host'] = host

                ports = self.extractPortsList()
                services = []
                
                if ports == [] : services.append({'ports': "Not Found"})

                for port in ports:
                    services.append({
                        'port': port,
                        'serveur': self.extractUsedServer(port),
                        'banner': self.extractBannere(port),
                        'technologies': self.extractTechnologies(port)
                    })
                sites_services[len(sites_services) - 1]['services'] = services
            except gaierror:
                print(f"\n • The address requested ['{site}'] is not associated with any host. \n")
                pass
        

        return sites_services
