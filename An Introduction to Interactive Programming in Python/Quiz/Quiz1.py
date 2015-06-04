def f (x) :
    return (-5 * (x**5)) + (69 * (x**2)) - 47

print f(0)
print f(1)
print f(2)
print f(3)

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    return present_value * ( (1 + rate_per_period) ** periods)

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
future_value(500, .04, 10, 10) #745.317442824

import math

def polygonarea (sides, length):
    return (1.0/4.0) * (sides * (length ** 2)) / math.tan(math.pi / sides)

print polygonarea(5,7) #84.3033926289
print polygonarea(7,3) #84.3033926289

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4) #1.09888451159