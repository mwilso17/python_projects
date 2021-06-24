# Mike Wilson 24 June 2021
# This program converts a given temperature in Kelvin to Fahrenheit.
# It can also be used to convert Kelvin to Celsius.

# Definies the temp in Kelvin using an integer.
kelvin_temp = 301

# Converts the Kelvin temp to Celsius.
celsius_temp = kelvin_temp - 273.15

# Converts the Celsius temp to Fahrenheit.
fahrenheit_temp = celsius_temp * (1.8) + 32

# Display results
print(fahrenheit_temp)