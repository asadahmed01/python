import imp
from employee import Employee
from developer import Developer
from manager import Manager

dev = Developer("steve", "Mark", 90000, "python")
dev2 = Developer("aa", "bb", 90000, "java")
mnger = Manager("Alex", "Cuban", 100000, [dev])
print(mnger.fullname())
mnger.add_emp(dev)
mnger.add_emp(dev2)
print(mnger.showEmployees())
