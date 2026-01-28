class Vehicle:
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel

    def display_details(self):
        print("Speed:", self.speed, "km/h")
        print("Fuel Type:", self.fuel)

class Car(Vehicle):
    def car_feature(self):
        print("Vehicle Type: Car")
        print("Feature: Air Conditioning")

class Motorcycle(Vehicle):
    def wheel_type(self):
        print("Vehicle Type: Motorcycle")
        print("Wheel Type: Two Wheeler")

class Truck(Vehicle):
    def cargo_capacity(self):
        capacity = float(input("Enter cargo capacity (in tons): "))
        print("Vehicle Type: Truck")
        print("Cargo Capacity:", capacity, "tons")

speed = int(input("Enter vehicle speed (km/h): "))
fuel = input("Enter fuel type: ")

print("\nSelect Vehicle")
print("1. Car")
print("2. Motorcycle")
print("3. Truck")

choice = int(input("Enter your choice: "))
if choice == 1:
    vehicle = Car(speed, fuel)
    vehicle.display_details()
    vehicle.car_feature()

elif choice == 2:
    vehicle = Motorcycle(speed, fuel)
    vehicle.display_details()
    vehicle.wheel_type()

elif choice == 3:
    vehicle = Truck(speed, fuel)
    vehicle.display_details()
    vehicle.cargo_capacity()

else:
    print("Invalid choice")
