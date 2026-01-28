class Vehicle:
    def __init__(self, s, f):
        self.s, self.f = s, f

    def show(self):
        print("Speed:", self.s, "km/h | Fuel:", self.f)

class Car(Vehicle):
    def extra(self):
        print("Type: Car | Feature: AC")

class Motorcycle(Vehicle):
    def extra(self):
        print("Type: Motorcycle | Wheels: Two")

class Truck(Vehicle):
    def __init__(self, s, f, c):
        super().__init__(s, f)
        self.c = c

    def extra(self):
        print("Type: Truck | Cargo:", self.c, "tons")

while True:
    print("\n1.Car  2.Motorcycle  3.Truck  4.Exit")
    ch = int(input("Choice: "))

    if ch == 4:
        break

    if ch not in (1, 2, 3):
        print("Invalid choice")
        continue

    s = int(input("Speed: "))
    f = input("Fuel: ")

    if ch == 3:
        c = float(input("Cargo capacity (tons): "))
        v = Truck(s, f, c)
    elif ch == 1:
        v = Car(s, f)
    else:
        v = Motorcycle(s, f)

    v.show()
    v.extra()
