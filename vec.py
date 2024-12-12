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

	def __sub__(self, other):
		return vec(self.x - other.x, self.y - other.y)
	
	def __mul__(self, n):
		return vec(self.x * n, self.y * n)

	def __truediv__(self, n):
		return vec(self.x / n, self.y / n)
	
	def __floordiv__(self, other):
		return vec(self.x % other.x, self.y % other.y)
	
	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self
	
	def __neg__(self):
		return vec(-self.x, -self.y)
	
	def copy(self):
		return vec(self.x, self.y)

	def rotate(self):
		return vec(-self.y, self.x)
	
	def is_inside(self, max):
		return self.x >= 0 and self.x < max.x and self.y >= 0 and self.y < max.y

	def neighbours(self):
		return [self + x for x in [vec(1, 0), vec(0, 1), vec(-1, 0), vec(0, -1)]] 

	def inside_neighbours(self, max):
		return [x for x in self.neighbours() if x.is_inside(max)]

