# Mike Wilson 24 June 2021
# This program converts a given temperature in Kelvin to Fahrenheit.
# It can also be used to convert Kelvin to Celsius.

import math

# Definies the temp in Kelvin using an integer. Integer can be changed
kelvin_temp = 301

# Converts the Kelvin temp to Celsius.
celsius_temp = round(kelvin_temp - 273.15)

# Converts the Celsius temp to Fahrenheit.
fahrenheit_temp = math.floor(celsius_temp * (1.8) + 32)

# Display results
print(f"{kelvin_temp} in Kelvin is {fahrenheit_temp} in Fahrenheit.")
print(f"{kelvin_temp} in Kelvin is {celsius_temp} in Celsius.")