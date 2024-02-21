import math
def degree_to_radian(degrees):
    radians = degrees * math.pi / 180
    return radians

input_degree = 15
output_radian = degree_to_radian(input_degree)

print("Input degree:", input_degree)
print("Output radian:", output_radian)