import pygame
import pprint
import random
from shapes import shape_mani, i_shape, t_shape, j_shape, l_shape, o_shape, s_shape, z_shape
all_shapes = [i_shape, t_shape, j_shape, l_shape, o_shape, s_shape, z_shape]

pixel_size = 40
resolution = [pixel_size * 10, pixel_size * 20]
score = 0

screen = pygame.display.set_mode(resolution)
colour_dictionary = {
	0: (35, 39, 42), 
	1: (0, 255, 255), 
	2: (128, 0, 128), 
	3: (0, 0, 255),
	4: (255, 127, 0), 
	5: (255, 255, 0),
	6: (0, 255, 0),
	7: (255, 0, 0)
}

def display():
	global shape

	running = True
	count = 0
	while running:
		count += 1
		draw_board()
		pygame.display.flip()


		if count == 1000:
			if shape.active:
				controller.move_shape_down(board, shape)

			else: 
				check_lines(board)
				shape = random.choice(all_shapes)()

				if controller.check_game_over(board, shape):
					running = False

			count = 0

		# Key inputs
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					controller.move_shape(board, shape, -1)
				if event.key == pygame.K_d:
					controller.move_shape(board, shape, 1)
				if event.key == pygame.K_s:
					count = 0
					if shape.active:
						controller.move_shape_down(board, shape)

					else: 
						check_lines(board)
						shape = random.choice(all_shapes)()

						if controller.check_game_over(board, shape):
							running = False

				if event.key == pygame.K_SPACE:
					controller.rotate_shape(board, shape)


def draw_board():
	width = resolution[0] / pixel_size
	height = resolution[1] / pixel_size
	for idx in range(int(height)):
		for idx2 in range(int(width)):
			location = (idx2 * pixel_size, idx * pixel_size, pixel_size, pixel_size)
			pygame.draw.rect(screen, colour_dictionary[board[idx][idx2]], location)


def create_board():
	global board, empty_row
	
	board = []
	x = resolution[0] / pixel_size
	y = resolution[1] / pixel_size


	empty_row = []
	for i in range(int(x)):
		empty_row.append(0)

	for j in range(int(y)):
		board.append(empty_row.copy())


def remove_lines(board, full_lines):
	global score
	
	for line in full_lines:
		board.pop(line)
		board.insert(0, empty_row.copy())
		score += 400		

	print(score)


def check_lines(board):
	idx = 0
	full_lines = []
	for line in board:
		full_line = True

		for cell in line:
			if cell == 0:
				full_line = False

		if full_line:
			full_lines.append(idx)
		idx += 1

	if full_lines != []:
		remove_lines(board, full_lines)


create_board()
shape = random.choice(all_shapes)()
controller = shape_mani()
controller.spawn_shape(board, shape)

display()
