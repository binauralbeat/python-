class Employee(object):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber


class Company(object):
    # """This represents a company in which people work"""
    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

    def get_company_name(self):
        # """Returns the name of the company"""

        return self.company_name

    # Add the remaining methods to fill the requirements above

if __name__ == '__main__':
    # Create the bank
    Google = Company()

    # Create some Employee
    steve = Employee("Steve", "Brownlee", "000000000")
    ryan = Employee("Ryan", "Tanay", "000000000")
    charisse = Employee("Charisse", "Lambert", "000000000")

    # Add the Employee into the aggregate instance variable of the bank
    Google.Employee.add(steve)
    Google.Employee.add(ryan)
    Google.Employee.add(charisse)