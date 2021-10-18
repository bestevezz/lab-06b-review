tempInCelsius = input("Pls enter a temperature in Celsius ")
tempInFar = (float(tempInCelsius) * 1.8 + 32)
tempInFar = round(tempInFar, 2)
print(str(tempInCelsius) + " degrees Celsius is " +
      str(tempInFar) + " degrees Fahrenheit.")
