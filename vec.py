import math

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
        
        if isinstance(first, float) and isinstance(second, float):
            self.x = first
            self.y = second

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __repr__(self):
        return str(self)

    def __format__(self, fmt):
        return f"[{self.x:{fmt}}, {self.y:{fmt}}]"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __abs__(self):
        return vec(abs(self.x), abs(self.y))

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

    def __mod__(self, other):
        return vec(self.x % other.x, self.y % other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __neg__(self):
        return vec(-self.x, -self.y)
    
    def copy(self):
        return vec(self.x, self.y)

    def length_squared(self):
        return self.x * self.x + self.y + self.y

    def magnitude(self):
        return math.isqrt(length_squared())

    def rotate(self):
        return vec(-self.y, self.x)
    
    def is_inside(self, max):
        return self.x >= 0 and self.x < max.x and self.y >= 0 and self.y < max.y

    def neighbours(self):
        return [self + x for x in [vec(1, 0), vec(0, 1), vec(-1, 0), vec(0, -1)]] 

    def inside_neighbours(self, max):
        return [x for x in self.neighbours() if x.is_inside(max)]

    def reachable(self, distance = 1):
        res = []

        for y in range(self.y - distance, self.y + distance + 1):
            for x in range(self.x - distance, self.x + distance + 1):
                pos = vec(x, y)

                if pos.distance(self) <= distance:
                    res.append(pos)

        return res

    def distance(self, other):
        sub = other - self

        return (abs(sub.x) + abs(sub.y))

    def div(self, other):
        return self.x / other.x

    def to_char(self):
        match [self.x, self.y]:
            case [1, 0]:
                return '>'
            case [0, 1]:
                return 'v'
            case [-1, 0]:
                return '<'
            case [0, -1]:
                return '^'

    def sign(self):
       if not self.x:
           return vec(0, self.y // abs(self.y))

       if not self.y:
           return vec(self.x // abs(self.x), 0)

vec.ZERO = vec(0, 0)


