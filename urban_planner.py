from building import Building
from city import City

building_one = Building("100 1st Street", 2)
building_one.construct()
building_one.purchase("Bob Builder")
building_one.print_details()

building_two = Building("200 2nd Street", 5)
building_two.construct()
building_two.purchase("Ashley Agency")
building_two.print_details()

building_three = Building("300 3rd Street", 9)
building_three.construct()
building_three.purchase("Henry House Hunters")
building_three.print_details()

building_four = Building("400 4th Street", 19)
building_four.construct()
building_four.purchase("Rafael's Real Estate")
building_four.print_details()

building_five = Building("500 5th Stree", 11)
building_five.construct()
building_five.purchase("Brittany's Buying Business")
building_five.print_details()

nashville = City("Nashville", "John Cooper", 1806)

nashville.add_building(building_one.address)
nashville.add_building(building_two.address)
nashville.add_building(building_three.address)
nashville.add_building(building_four.address)
nashville.add_building(building_five.address)

print(f"{nashville.name} was established in {nashville.established_year}. {nashville.mayor} is the current mayor. {nashville.name} contains the following buildings:")

for building in nashville.buildings:
    print(building)

