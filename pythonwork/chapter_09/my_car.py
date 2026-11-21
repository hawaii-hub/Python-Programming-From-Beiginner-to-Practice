from car import Car
from electric_car import ElectricCar as EC  

my_mustang = Car('audi', 'a4', 2024)
print(my_mustang.get_descriptive_name())

my_mustang.update_odometer(23)
my_mustang.read_odometer()

print("")
my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
