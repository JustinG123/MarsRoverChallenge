from rover import rover

def main():
	reader = open("instructions.txt", "r")


	height, width = reader.readline().split(' ')
	rovers = []
	start_pos = ''

	# rover(self, height, width, x, y, cardinal, rovers)

	line_count = 0
	for file_line in reader:
		if not line_count % 2:
			x, y, cardinal = file_line.split(' ')
			rovers.append(rover(height, width, x, y, cardinal, rovers))
			pass
		else:
			rovers[-1].go(file_line)
			print(rovers[-1].get_position())
		line_count += 1
		
	reader.close()	

if __name__ == "__main__":
	main()