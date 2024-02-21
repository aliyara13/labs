#degree
import math
def degree_to_radian(degrees):
    radians = degrees * math.pi / 180
    return radians

input_degree = 15
output_radian = degree_to_radian(input_degree)

print("Input degree:", input_degree)
print("Output radian:", output_radian)

#trapezoid
import math
def Area_trap(height, a, b):
    area=1/2*(a+b)*height
    return area
input_a=5
input_b=6
input_height=5

output_area=Area_trap(input_a, input_b, input_height)
print(output_area)

#parallelogram
import math
length=5
heigth=6
area=length*heigth
print(area)

#polygon
import math
length=25
sides=4
area=(sides*length**2)/4*math.tan(math.pi/sides)    
print(round(area))