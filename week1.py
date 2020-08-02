#๊Urasaya Nakpram TU
#Python code that received multiple value to find maximum minimum and average.
import math
x = list(map(int, input("Enter a multiple value: ").split()))
#Find a maximum
maximum = math.max(x)
#Find a minimum
minimum = min(x)
#Find a average
avg = sum(x)/len(x)
print("The maximum value is {:5.2f} The minimum value is {:5.2f} The average is {:5.2f}.".format(maximum,minimum,avg))
