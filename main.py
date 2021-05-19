import pygame 
from shapes import Shapes

resolution = [500, 1000]
pixel_size = 50

screen = pygame.display.set_mode(resolution)
colour_dictionary = {0: (255, 255, 255)}

def display():
	running = True
	while running:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a:
						update_shape(LEFT)
					if event.key == pygame.K_d:
						update_shape(RIGHT)

					# Add rotation here later

		draw_board()



def draw_board():
		for i in range(10):
			for j in range(20):
				location = (i * pixel_size, j * pixel_size, pixel_size, pixel_size)
				pygame.draw.rect(screen, colour_dictionary[board[i][j]], location)

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
display()