from vec import vec

class line:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f"({self.first} -> {self.second})"

    def intersect(self, other):
        numerators = [
            (self.first.x * self.second.y - self.first.y * self.second.x) * (other.first.x - other.second.x) - (self.first.x - self.second.x) * (other.first.x * other.second.y - other.first.y * other.second.x),
            (self.first.x * self.second.y - self.first.y * self.second.x) * (other.first.y - other.second.y) - (self.first.y - self.second.y) * (other.first.x * other.second.y - other.first.y * other.second.x),
                ]
        denominator = (self.first.x - self.second.x) * (other.first.y - other.second.y) - (self.first.y - self.second.y) * (other.first.x - other.second.x)

        if not denominator:
            return None

        return vec(numerators[0] / denominator, numerators[1] / denominator)
