class Company:

    def __init__(self, name, address, industry):
        self.name = name
        self.address = address
        self.industry = industry
        self.employees = []

    def add_employee(self, name):
        self.employees.append(name)


    