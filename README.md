# Mars Rover Challenge

This is my take on the Google [Mars Rover Challenge](https://code.google.com/archive/p/marsrovertechchallenge/) 

#### Usage
You will need to install python 3.0 or above (Created in Python 3.9.5).  
To run the unit tests either run `make test` or manually run `python -m unittest test.py`  
To run the main program run `make run` or manually run `python main.py`

The instructions followed by the rovers are found in the instructions.txt file


#### Description
A series of rovers are dropped on a plateau on mars and then given instructions to explore the plateau.
The plateau is of a defined size given by the first parameter in the file, then the following 2 lines define the rovers starting point and the rovers instructions to follow, the instructions are given as 'M' to move forward, 'L' to move left and 'R' to move right

#### Features
* Edge detection, if a rover gets to the end of the plateau and a 'M' command is given the rover will ignore the command and move onto the next command in the string
* Collision detection, if a rover gets to a tile where another Rover is present and a 'M' command is given the rover will ignore the command and move onto the next command in the string
