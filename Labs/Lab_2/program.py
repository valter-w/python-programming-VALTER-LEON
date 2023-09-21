from pathlib import Path


def reliable_path(file_name):
    '''Returns the full path to file_name, assuming the file is in 
    the same directory as this file (program.py).'''
    this_file = __file__
    p = Path(this_file).with_name(file_name)
    return p.absolute()

data_points_path = reliable_path("datapoints.txt")
print(f"{type(data_points_path) = }")
print(f"{data_points_path = }")

with open(data_points_path) as file:
    lines = file.readlines()

# Manage file contents outside with statement above in order to 
# close the file asap.

# remove "\n" at end of each line
lines = [line.rstrip() for line in lines]

# remove head line
lines = lines[1:]

# each item will contain data about a pokemon
measurements = []

for line in lines:
    line_data = line.split(", ")
    width = float(line_data[0])
    height = float(line_data[1])
    label = int(line_data[2])
    measurement = {
        "width": width,
        "height": height,
        "label": label
    }
    measurements.append(measurement)
    print(f"{measurement = }")

# Check if there were any lines read from datapoints.txt
print(f"{len(lines) = }")

print("End.")