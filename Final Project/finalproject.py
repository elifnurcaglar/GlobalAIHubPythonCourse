print("******COMPANY MANAGEMENT SYSTEM********")
print("--MANAGERS--")

class Manager:
    def __init__(self, mfirstname, mlastname, mages):
        self.managerfirstname = mfirstname
        self.managerlastname = mlastname
        self.managerfullname = mfirstname + mlastname
        self.managerages = mages
    def printmanagername(self):
        print(self.managerfirstname + self.managerlastname)
    def printmanagerage(self):
        print(self.managerfullname + " is " + str(self.managerages) + " years old.")
    def managerstatus(self):
        print(self.managerfullname + " is a manager and " + str(self.managerages) + " years old.")

manager1 = Manager("Deniz", " Çalıkuşu", 32)
manager1.printmanagername()
manager1.printmanagerage()
manager1.managerstatus()

print("--EMPLOYEES--")


class Employees:
    def __init__(self, efirstname, elastname, eages, elanguages):
        self.employeesfirstname = efirstname
        self.employeeslastname = elastname
        self.employeesfullname = efirstname + elastname
        self.employeesage = eages
        self.employeeslanguages = elanguages
    def printemployeesname(self):
        print(self.employeesfirstname + self.employeeslastname)
    def printemployeesage(self):
        print(self.employeesfullname + " is " + str(self.employeesage) + " years old.")
    def employeestatus(self):
        print(self.employeesfullname + " is an employee and " + str(self.employeesage) + " years old.")
    def printlanguages(self):
        print(self.employeesfullname + " can speak:" + self.employeeslanguages)
employees1 = Employees("Tuğra", " Çalışkan", 28, " Spanish " + " English " + " Turkish ")
employees1.printemployeesname()
employees1.printemployeesage()
employees1.employeestatus()
employees1.printlanguages()

print("--EMPLOYEE LANGUAGES--")

employees1.printlanguages()
