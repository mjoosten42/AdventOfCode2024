class vec:
	x: int = 0
	y: int = 0

	def __init__(self, first, second=None):
		if (isinstance(first, str)):
			match first:
				case '^':
					self.x = 0
					self.y = -1
				case '>':
					self.x = 1
					self.y = 0
				case 'v':
					self.x = 0
					self.y = 1
				case '<':
					self.x = -1
					self.y = 0
		
		if isinstance(first, int) and isinstance(second, int):
			self.x = first
			self.y = second

	def __str__(self):
		return f"[{self.x}, {self.y}]"

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash((self.x, self.y))

	def __add__(self, other):
		return vec(self.x + other.x, self.y + other.y)

	def copy(self):
		return vec(self.x, self.y)

	def rotate(self):
		return vec(-self.y, self.x)
	
