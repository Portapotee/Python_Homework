from employeeClass import *
from managerClass import *
from developerClass import *

worker1 = employee("bryan", 32453, "2020-5-3", 200.34)
print(worker1)

worker2 = manager("bob", 99999, "2019-3-23", 205.99)
print(worker2)

worker3 = developer("unknown", 12345, "2020-4-5", 203.51)
print(worker3)

worker2.assignWork()
worker3.coding()
worker3.testing()
worker3.reportWork()
worker2.review()