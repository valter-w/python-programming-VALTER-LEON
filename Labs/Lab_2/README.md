# Lab 2

## Code explained

### Reading and writing to files

The two data files used by this program, *datapoints.txt* and *testpoints.txt*, 
are stored in the same directory as the actual program [program.py](program.py). 
During development in Visual Studio Code, when trying to open *datapoints.txt* 
with `open(".\datapoints.txt")`, I experienced errors since the working directory in 
the terminal in the IDE was not the same directory as the program bering run, 
*program.py*. 
For this reason, I developed a function called `reliable_path(file_name)` that 
will return the full path for `file_name`,
independent of the current working directory:
``` python
from pathlib import Path

def reliable_path(file_name):
    this_file = __file__
    p = Path(this_file).with_name(file_name)
    return p.absolute()
```
Examples of using this function:
``` python
data_points_path = reliable_path("datapoints.txt")
test_points_path = reliable_path("testpoints.txt")
```
Beware that this function does not return a string. In my case, it returned an 
object of the type `WindowsPath` as I am developing and running the program in a 
Microsoft Windows environment. For a Linux user, it would likely return an 
object of the type `PosixPath`. (Fore more information, see the graph in 
[this documentation](https://docs.python.org/3/library/pathlib.html#module-pathlib) 
about the `pathlib` library.) Using this object instead of a string as an 
argument for the `open()` function was not an issue though:
```
with open(data_points_path) as file:
    lines = file.readlines()
```

## Sources