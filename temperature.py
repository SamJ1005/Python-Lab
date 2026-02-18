from tempe_package.ctof import cel_to_fah
from tempe_package.ftoc import fah_to_cel

print("Temperature Conversion Package")

c = float(input("\nEnter temperature in Celsius: "))
print("Fahrenheit:", cel_to_fah(c))

f = float(input("Enter temperature in Fahrenheit: "))
print("Celsius:", fah_to_cel(f))
