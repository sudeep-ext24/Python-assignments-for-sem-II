from temp import cel_to_far
from temp import far_to_cel
from temp import cel_to_kev

print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
c = float(input("Enter temperature in Celsius: "))
result = cel_to_far.convert(c)
print("Temperature in Fahrenheit:", result)

elif choice == 2:
f = float(input("Enter temperature in Fahrenheit: "))
result = far_to_cel.convert(f)
print("Temperature in Celsius:", result)