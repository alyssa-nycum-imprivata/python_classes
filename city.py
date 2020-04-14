class City:

    def __init__(self, name, mayor, established_year):
        self.name = name
        self.mayor = mayor
        self.established_year = established_year
        self.buildings = []

    def add_building(self, building_address):
        self.buildings.append(building_address)
