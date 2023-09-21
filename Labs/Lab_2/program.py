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

# Check if there were any lines read from datapoints.txt
print(f"{len(lines) = }")

print("End.")