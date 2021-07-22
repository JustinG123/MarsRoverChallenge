import sys

class rover:
	# Creates the rover with the grid width and height, the initial x and y and the starting orientation
	# And an array of previous rovers to avoid any colisions
	def __init__(self, width, height, x, y, cardinal, rovers):
		if int(height) <= 0 or int(width) <= 0:
			self.print_error('Please enter a valid height and width for the plateau')
		self.height = int(height)
		self.width = int(width)

		if 0 > int(x) or int(x) >= self.width:
			self.print_error('Please enter a x coordinate within the parameters of the plateau')
		self.x = int(x)

		if 0 > int(y) or int(y) >= self.height:
			self.print_error('Please enter a y coordinate within the parameters of the plateau')
		self.y = int(y)

		if cardinal[0] not in 'NESW':
			self.print_error('Please enter a valid starting cardinal direction')
		self.cardinal = cardinal[0]

		self.rovers = rovers
	
	# Determines the cardinal direction the rover will be facing on turning
	# direction can be L or R
	def turn(self, direction):
		card_dir = ['N', 'E', 'S', 'W']
		curr_index = card_dir.index(self.cardinal)

		if direction == 'R':
			curr_index = curr_index + 1 if curr_index != 3 else 0
		elif direction == 'L':
			curr_index = curr_index - 1 if curr_index != 0 else 3

		self.cardinal = card_dir[curr_index]

	# Moves the rover forward based on its current cardinal direction
	# If a rover is about to crash or fall off the plateau it ignores the command and goes to the next command
	def forward(self):
		move_grid = {
			'N': (0, 1),
			'E': (1, 0),
			'S': (0, -1),
			'W': (-1, 0),
		}

		movement = move_grid[self.cardinal]
		if self.check_bounds(self.x + movement[0], self.y + movement[1]):
			self.x += movement[0]
			self.y += movement[1]

	# Check if the rover is in bounds or if a colission between 2 rovers will occur
	def check_bounds(self, new_x, new_y):
		if new_x >= self.width or 0 > new_x or new_y >= self.height or 0 > new_y:
			return False
		
		for pos in self.rovers:
			if pos.get_position()[0:3] == f'{new_x} {new_y}':
				return False

		return True

	# Get the current position and direction of the Mars Rover
	def get_position(self):
		return f"{self.x} {self.y} {self.cardinal}"

	# Runs the input string of instructions to manuver the rover
	def go(self, input):
		for cmd in input:
			if cmd == 'M':
				self.forward()
			else:
				self.turn(cmd)

	def print_error(self, error_mesage):
		print(error_mesage)
		sys.exit()