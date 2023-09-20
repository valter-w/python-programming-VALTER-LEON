import math

def euclidean_distance(point_1_x, point_1_y, point_2_x, point_2_y):
    x_square = (point_1_x - point_2_x)**2
    y_square = (point_1_y - point_2_y)**2
    distance = math.sqrt(x_square + y_square)
    return distance

# Removes parenthesis and spaces,
# thus "(3, 4)" becomes "3,4"
def clean_point_input(point_input):
    point_input = point_input.strip()
    point_input = point_input.replace("(", "")
    point_input = point_input.replace(")", "")
    point_input = point_input.replace(" ", "")
    return point_input

# Returns the x value of an entered coordinate, 
# e.g. "(3, 4)" returns 3
def parse_x(point_input):
    point_input = clean_point_input(point_input)
    x_y = point_input.split(",")
    x = x_y[0]
    return int(x)

# Returns the y value of an entered coordinate, 
# e.g. "(3, 4)" returns 4
def parse_y(point_input):
    point_input = clean_point_input(point_input)
    x_y = point_input.split(",")
    y = x_y[1]
    return int(y)


point_1_input = input("Enter the first point (x, y): ")
point_1_x = parse_x(point_1_input)
point_1_y = parse_y(point_1_input)

point_2_input = input("Enter the second point (x, y): ")
point_2_x = parse_x(point_2_input)
point_2_y = parse_y(point_2_input)


distance = euclidean_distance(point_1_x, point_1_y, point_2_x, point_2_y)
msg = f"\nThe distance between ({point_1_x}, {point_1_y}) "
msg += f"and ({point_2_x}, {point_2_y}) "
msg += f"is {distance:.2f}."
print(msg)