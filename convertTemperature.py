def convertTemperature(temp, scale):
    if scale == 'C':
       convertedValue = (temp * 9/5) + 32 
       print(convertedValue)
    elif scale == 'F':
        convertedValue = (temp - 32) * (5/9)
        print(convertedValue)
    else:
        print("invalid Scale")


convertTemperature(20, 'C')
convertTemperature(100,'F')
