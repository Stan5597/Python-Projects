#Script to convert Fahrenheit into Kelvin and vice versa

Fahrenheit= int(input("Please enter a Fahrenheit temperture:") )
print("Fahrenheit:" , Fahrenheit)
kelvin =\
 int(((Fahrenheit -32) *5) /9 + 273.15)
print(kelvin)
print()
Kelvin= int(input("Please enter a Kelvin temperture:"))
print("Kelvin:" , Kelvin)
Fahrenheit=\
int(((Kelvin - 273.25) * 9) /5+32)
print(Fahrenheit)
