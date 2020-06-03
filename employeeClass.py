from datetime import *

class employee:
    def __init__(self, name, employeeID, startdate, salary):
        self.name = name
        self.employeeID = employeeID
        self.startDate = startdate
        self.salary = salary
    
    def __repr__(self):
        return "{0}: employeeID = {1} \t startdate = {2} \t salary = {3}".format(self.name, self.employeeID, self.startDate, self.salary)