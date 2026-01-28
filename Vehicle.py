class Vehicle:
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel

    def display_vehicle(self):
        print("Speed:", self.speed, "km/h")
        print("Fuel:", self.fuel)

class Car(Vehicle):
    def car_type(self):
        print("Vehicle Type: Car")

class Motorcycle(Vehicle):
    def wheel_type(self):
        print("Wheel Type: Two Wheeler")

class Truck(Vehicle):
    def cargo_capacity(self, capacity):
        print("Cargo Capacity:", capacity, "tons")

speed = int(input("Enter vehicle speed (km/h): "))
fuel = input("Enter fuel type: ")

print("\nChoose Vehicle Type")
print("1. Car")
print("2. Motorcycle")
print("3. Truck")

choice = int(input("Enter your choice: "))

if choice == 1:
    v = Car(speed, fuel)
    v.display_vehicle()
    v.car_type()

elif choice == 2:
    v = Motorcycle(speed, fuel)
    v.display_vehicle()
    v.wheel_type()

elif choice == 3:
    capacity = float(input("Enter cargo capacity (tons): "))
    v = Truck(speed, fuel)
    v.display_vehicle()
    v.cargo_capacity(capacity)

else:
    print("Invalid choice")
