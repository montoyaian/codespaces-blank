from package import Package
from package import StandardPackage
from package import OverWeigthPackage
from person import  Person
from bill import  Bill
from address import  Address
from deliver import  Deliver

Box = Package(123456, 5.6, "Box", 500000)
product = StandardPackage(5,20,"laptop", 200000,1000)
client = Person(1,"ian","montoya")
addressc = Address("29/03/2004","1:40","juan","ian","turbaco","cartagena","3022846010","laptop","horizonte","calle2","cartagena","mamonal","11001")
delivery = Deliver("30/03/2004","1:40","juan","ian","turbaco","cartagena","3022846010","laptop")

print("informacion del paquete")
print(Box)

print("\n client")
print (client)

print("\n delivery address")
print(addressc)

print("\n delivery details")
print(delivery)

print("\n cost")
print(product.calculate())

