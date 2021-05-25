import pygame
import pprint
from shapes import Shapes

pixel_size = 40
resolution = [pixel_size * 10, pixel_size * 20]

screen = pygame.display.set_mode(resolution)
colour_dictionary = {0: (35, 39, 42), 1: (255, 255, 255)}

def display():
	running = True
	while running:
		draw_board()
		pygame.display.flip()

		# Key inputs
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					update_shape(LEFT)
				if event.key == pygame.K_d:
					update_shape(RIGHT)

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

	pprint.pprint(board)


create_board()
display()