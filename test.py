import sys
import io
import unittest

from rover import rover

# rover(self, height, width, x, y, cardinal, rovers)

class unitTest(unittest.TestCase):
	def test_no_grid(self):
		suppress_text = io.StringIO()
		sys.stdout = suppress_text 

		setup_width = 0
		setup_height = 0

		with self.assertRaises(SystemExit):
			rover(setup_width, setup_height, 1, 1, 'N', [])

		sys.stdout = sys.__stdout__

	def test_no_movement_basic(self):
		setup_width = 5
		setup_height = 7
		
		rover_one = rover(setup_width, setup_height, 0, 0, 'N', [])
		self.assertEqual(rover_one.get_position(), '0 0 N')

		rover_two = rover(setup_width, setup_height, 1, 1, 'N', [])
		self.assertEqual(rover_two.get_position(), '1 1 N')

	def test_out_of_bounds(self):
		suppress_text = io.StringIO()
		sys.stdout = suppress_text 

		setup_width = 5
		setup_height = 7

		with self.assertRaises(SystemExit):
			rover(setup_width, setup_height, 5, 1, 'N', [])

		with self.assertRaises(SystemExit):
			rover(setup_width, setup_height, 1, 7, 'N', [])

		with self.assertRaises(SystemExit):
			rover(setup_width, setup_height, -1, 1, 'N', [])

		with self.assertRaises(SystemExit):
			rover(setup_width, setup_height, 1, -1, 'N', [])

		sys.stdout = sys.__stdout__

	def test_cardinal_directions(self):
		suppress_text = io.StringIO()
		sys.stdout = suppress_text 

		setup_width = 5
		setup_height = 7

		with self.assertRaises(SystemExit):
			rover(setup_width, setup_height, 1, 1, 'P', [])

		rover_one = rover(setup_width, setup_height, 1, 1, 'N', [])
		self.assertEqual(rover_one.get_position(), '1 1 N')

		sys.stdout = sys.__stdout__

	def test_move(self):
		setup_width = 5
		setup_height = 5
		
		rover_one = rover(setup_width, setup_height, 1, 2, 'N', [])
		self.assertEqual(rover_one.get_position(), '1 2 N')
		rover_one.go('LMLMLMLMM')
		self.assertEqual(rover_one.get_position(), '1 3 N')

		rover_two = rover(setup_width, setup_height, 3, 3, 'E', [])
		self.assertEqual(rover_two.get_position(), '3 3 E')
		rover_two.go('MMRMMRMRRM')
		self.assertEqual(rover_two.get_position(), '4 1 E')

	def test_collission(self):
		setup_width = 5
		setup_height = 5

		rover_one = rover(setup_width, setup_height, 1, 2, 'N', [])
		self.assertEqual(rover_one.get_position(), '1 2 N')
		rover_one.go('LMLMLMLMM')
		self.assertEqual(rover_one.get_position(), '1 3 N')

		rover_two = rover(setup_width, setup_height, 1, 2, 'N', [rover_one])
		self.assertEqual(rover_two.get_position(), '1 2 N')
		rover_two.go('M')
		self.assertEqual(rover_two.get_position(), '1 2 N')