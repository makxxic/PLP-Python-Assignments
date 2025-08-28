#Assignment 1: Design Your Own Class
# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived Class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # Inheriting from Device
        self.storage = storage
        self.battery = battery
        self.__secret_code = "1234"  # Encapsulation (private attribute)

    # Method to display details
    def phone_details(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}mAh"

    # Method to simulate charging
    def charge(self, amount):
        self.battery += amount
        return f"Battery charged. Current: {self.battery}mAh"
    
    # Getter method (Encapsulation example)
    def get_secret_code(self):
        return self.__secret_code


# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S22", 256, 4000)
phone2 = Smartphone("Apple", "iPhone 14", 128, 3200)

print(phone1.phone_details())
print(phone2.phone_details())

print(phone1.charge(500))
print("Secret Code (via getter):", phone1.get_secret_code())


#Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🛥️"

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
