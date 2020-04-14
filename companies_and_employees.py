from company import Company
from employee import Employee

first_company = Company("REI", "800 Rock Way", "Outdoor Retail")
second_company = Company("Lyft", "300 2nd Ave", "Rideshare")

first_employee = Employee("Alyssa", "Outdoor Trip Leader", "02/23/20")
first_company.add_employee(first_employee.name)

second_employee = Employee("Matt", "Desk Manager", "01/04/20")
first_company.add_employee(second_employee.name)

third_employee = Employee("Stacey", "Sales Representative", "12/15/19")
first_company.add_employee(third_employee.name)

fourth_employee = Employee("Katie", "Customer Experience Associate", "03/20/20")
second_company.add_employee(fourth_employee.name)

fifth_employee = Employee("Sofia", "Critical Response Line Associate", "04/12/20")
second_company.add_employee(fifth_employee.name)

print(f"{first_company.name} is in the {first_company.industry} located at {first_company.address} and has the following employees:")

for employee in first_company.employees:
    print(employee)

print(f"{second_company.name} is in the {second_company.industry} industry located at {second_company.address} and has the following employees:")

for employee in second_company.employees:
    print(employee)