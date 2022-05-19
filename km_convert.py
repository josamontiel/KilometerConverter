# input the km amount you want converted
kilometers = float(input("Enter value in kilometers: "))

# conversion rate
conMil = 0.621371

# calculate miles
miles = kilometers * conMil
print('%0.2f kilometers is equal to %0.2f miles' % (kilometers, miles))
