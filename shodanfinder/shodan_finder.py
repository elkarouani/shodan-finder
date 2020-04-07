import shodan
import socket

class ShodanFinder :
    API = 'tedoHTagcSRqQm9LhIzUCqIqUvI06dHz'

    def __init__(self, sites):
        self.sites_list = sites
        self.data_instance = {}

    def getHost(self, site):
        return socket.gethostbyname(site)

    def extractData(self, host):
        api = shodan.Shodan(self.API)
        self.data_instance = api.host(host)

    def extractPortsList(self):
        return self.data_instance['ports']
    
    def extractUsedServer(self, port):
        for port_container in self.data_instance['data']:
            if port_container['port'] == port:
                return port_container['http']['server']

    def extractBannere(self, port):
        for port_container in self.data_instance['data']:
            if port_container['port'] == port:
                return port_container['data']

    def extractTechnologies(self, port):
        for port_container in self.data_instance['data']:
            if port_container['port'] == port:
                return port_container['http']['components'] if hasattr(port_container['http'], 'components') else "Not Found"

    def shodanProcedure(self):
        sites_services = []

        for site in self.sites_list:
            sites_services.append({'name': site})

            host = self.getHost(site)
            self.extractData(host)
            sites_services[len(sites_services) - 1]['host'] = host

            ports = self.extractPortsList()
            services = []
            for port in ports:
                services.append({
                    'port': port,
                    'serveur': self.extractUsedServer(port),
                    'banner': self.extractBannere(port),
                    'technologies': self.extractTechnologies(port)
                })
            sites_services[len(sites_services) - 1]['services'] = services

        return sites_services

