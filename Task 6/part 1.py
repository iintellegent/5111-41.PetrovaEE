import math
import numpy
import random

def calc_geom( arr: numpy.ndarray):
    mult = 1
    for num in a:
        mult*=num
    return math.pow(mult, 1/arr.size)
n = 10
a = numpy.ndarray(n)
for i in range(0,10):
    a[i]=random.randint(1,100)
avg_geom = calc_geom(a)
listnumbers = [a]
z=[a for a in a if a%2==0 and a%3!=0] 
print(a)
print(sum(z))
print ("Среднее значение =",numpy.mean(listnumbers))



