celcius_fahrenheit = lambda c: (9/5) * c + 32
celcius_reamur = lambda c: 0.8 * c

celcius = int(input("Input Celcius = "))

print("Ouput Farenheit : ", int(celcius_fahrenheit(celcius)))
print("Output Reamur : ", int(celcius_reamur(celcius)))
