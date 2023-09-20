import math

def euclidean_distance(point_1_x, point_1_y, point_2_x, point_2_y):
    x_square = (point_1_x - point_2_x)**2
    y_square = (point_1_y - point_2_y)**2
    distance = math.sqrt(x_square + y_square)
    return distance

# (10, 3), (-1, -9), (10, -10), (4, -2), (9, -10)
points = [
    [10, 3],
    [-1, 9],
    [10, -10],
    [4, -2],
    [9, -10],
]

for point in points:
    point_x = point[0]
    point_y = point[1]
    distance = euclidean_distance(0, 0, point_x, point_y)
    msg = "The distance between (0, 0) and "
    msg += f"({point_x}, {point_y}) is {distance:.1f}."
    print(msg)