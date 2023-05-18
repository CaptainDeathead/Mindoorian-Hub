import requests
#import html5lib

class Nationstates:
    def __init__(self, nation):
        self.nation = nation
        self.url = "https://www.nationstates.net/cgi-bin/api.cgi?nation=" + self.nation + "&q="
        self.nation_data = self.get_nation_data()
        self.world_data = self.get_world_data()
        
    def get_nation_data(self):
        self.nation_data = requests.get(self.url + "nationdata").text
        return self.nation_data
    
    def get_world_data(self):
        self.world_data = requests.get(self.url + "world").text
        return self.world_data
    
    def get_nation_name(self):
        self.nation_name = self.nation_data.split("<NAME>")[1].split("</NAME>")[0]
        return self.nation_name