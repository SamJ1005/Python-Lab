class Vehicle:
    def __init__(self, s=0, f=''):
        self.s, self.f = s, f

    def show(self):
        self.s = int(input("Speed: "))
        self.f = input("Fuel: ")

    def display(self):
        print("Speed:", self.s, "km/h | Fuel:", self.f)

class Car(Vehicle):
    def extra(self):
        print("Type: Car | Feature: AC")

class Motorcycle(Vehicle):
    def extra(self):
        print("Type: Motorcycle | Wheels: Two Wheeler")

class Truck(Vehicle):   
    def __init__(self, s=0, f='', c=0):
        super().__init__(s, f)
        self.c = c

    def extra(self):
        self.c = float(input("Cargo capacity (tons): "))
        print("Type: Truck | Cargo:", self.c, "tons")

while True:
    print("\n1.Car  2.Motorcycle  3.Truck  4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        v = Car()
    elif ch == 2:
        v = Motorcycle()
    elif ch == 3:
        v = Truck()
    elif ch == 4:
        print("Exiting Vehicle...")
        break
    else:
        print("Invalid choice")
        continue

    v.show()      # all inputs first
    v.extra()     # extra input (cargo if truck)
    v.display()   # final vehicle display