import pprint
from itertools import cycle

class shape_mani:
	def spawn_shape(self, board, obj):
		shape = obj.info(obj.location)

		for pos in shape:
			board[pos[0]][pos[1]] = obj.color


	def update_shape(self, board, obj, old, new):
		# Wipe old shape off board and put new in
		for pos in old:
			board[pos[0]][pos[1]] = 0

		for pos in new:
			board[pos[0]][pos[1]] = obj.color

	# WHY NOT WORKING
	def rotate_shape(self, board, obj):
		old = obj.info(obj.location)
		idx = obj.shape
		length = len(obj.rotations) - 1

		if idx == length:
			idx = 0

		else:
			idx += 1

		print(idx)
		obj.shape = idx
		self.update_shape(board, obj, old, obj.info(obj.location))



	def move_shape_down(self, board, obj):
		if self.is_colliding(board, obj):
			return

		new_pos = [obj.location[0] + 1, obj.location[1]]

		current = obj.info(obj.location)
		new = obj.info(new_pos)
		obj.location = new_pos

		self.update_shape(board, obj, current, new)


	def is_colliding(self, board, obj):
		new_pos = [obj.location[0] + 1, obj.location[1]]
		new = obj.info(new_pos)

		for pos in new:
			try:
				if board[pos[0]][pos[1]] != 0:
					return True

			except IndexError:
				return True
		return False


	def move_shape(self, board, obj, direction):
		try:
			new_pos = [obj.location[0], obj.location[1] + direction]

			shape = obj.info(new_pos)
			for pos in shape:
				if pos[0] < 0 or pos[1] < 0:
					return

				board[pos[0]][pos[1]] = board[pos[0]][pos[1]]

		except IndexError:
			return

		current = obj.info(obj.location)
		new = obj.info(new_pos)

		pixel = new.copy()
		for pos in current:
			if pos in pixel:
				pixel.remove(pos)

		if board[pixel[0][0]][pixel[0][1]] != 0:
			return

		obj.location = new_pos
		self.update_shape(board, obj, current, new)


class i_shape:
	def __init__(self):
		self.location = [0, 5]
		self.color = 1

	def info(self, pos):
		x = pos[0]
		y = pos[1]

		self.rotations = [[[x, y - 2], [x, y - 1], [x, y], [x, y + 1]], [[x - 2, y], [x - 1, y], [x, y], [x + 1, y]]]
		self.shape = 0

		return self.rotations[self.shape]