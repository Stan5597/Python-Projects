# Script that prints a table of Kelvin and their equivalent Fahrenheit values.

# Prints conversion table
def print_conversion_table(min, max):
    print_header()
    for kelvin in range (min, max + 1) :
        print_table_line(kelvin)

# Prints table header
def print_header():
    print("Kelvin", "\t", "Fahrenheit")
    print("-------------------")

# Prints table and line
def print_table_line(kelvin):
    fahrenheit = ((kelvin - 273.15) * 9)/5 +32
    print(kelvin,"\t", round(fahrenheit))


min = int(input("Minimum Kelvin temperature: "))
max = int(input("Maximum Kelvin temperature: "))
print()
print_conversion_table(min, max)
