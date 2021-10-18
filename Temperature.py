tempInCelsius = float(input("Pls enter a temperature in Celsius... "))
#tempInCelsius = float(tempInCelsius)
tempInFar = tempInCelsius * 1.8 + 32
tempInFar = round(tempInFar, 2)
# round() is a FUNCTION to limit the number of decimal places
print(str(tempInCelsius) + " degrees Celsius is " +
      str(tempInFar) + " degrees Fahrenheit.")
