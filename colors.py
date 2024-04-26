class Colors:
	dark_grey = (112, 128, 144)
	green = (220, 20, 60)
	red = (34, 139, 34)
	orange = (255, 215, 0)
	yellow = (104, 34, 139)
	purple = (0, 128, 128)
	cyan = (0, 0, 128)
	blue = (255, 127, 80)
	white = (255, 255, 255)
	dark_blue = (34, 34, 34)
	light_blue = (135, 206, 235)

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
