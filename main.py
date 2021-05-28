import pygame
import pprint
from shapes import shape_mani, i_shape

pixel_size = 40
resolution = [pixel_size * 10, pixel_size * 20]

screen = pygame.display.set_mode(resolution)
colour_dictionary = {0: (35, 39, 42), 1: (255, 255, 255)}

def display():
	global shape

	running = True
	count = 0
	count2 = 0
	while running:
		count += 1
		draw_board()
		pygame.display.flip()

		if count == 1000:
			if not controller.is_colliding(board, shape):
				controller.move_shape_down(board, shape)

			else: 
				shape = i_shape()

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
				if event.key == pygame.K_SPACE:
					controller.rotate_shape(shape)

				# Add rotation here later



def draw_board():
	width = resolution[0] / pixel_size
	height = resolution[1] / pixel_size
	for idx in range(int(height)):
		for idx2 in range(int(width)):
			location = (idx2 * pixel_size, idx * pixel_size, pixel_size, pixel_size)
			pygame.draw.rect(screen, colour_dictionary[board[idx][idx2]], location)


def create_board():
	global board
	
	board = []
	x = resolution[0] / pixel_size
	y = resolution[1] / pixel_size


	row = []
	for i in range(int(x)):
		row.append(0)

	for j in range(int(y)):
		board.append(row.copy())


create_board()
shape = i_shape()
controller = shape_mani()
controller.spawn_shape(board, shape)

display()
