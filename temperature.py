from tempe_package.ctof import cel_to_fah
from tempe_package.ftoc import fah_to_cel

print("Temperature Conversion Package")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", cel_to_fah(c))

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", fah_to_cel(f))

else:
    print("Invalid choice")
