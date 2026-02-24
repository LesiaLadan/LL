class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    
    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        summary_square = self.get_square() + other.get_square()
        for new_width in range(summary_square // 2, 0, -1):
            if summary_square % new_width == 0:
                new_height = summary_square // new_width
                return Rectangle(new_width, new_height)

    def __mul__(self, n):
        if not isinstance(n, int) or n <= 0:
            return NotImplemented
        summary_square = self.get_square() * n
        for new_width in range(summary_square // 2, 0, -1):
            if summary_square % new_width == 0:
                new_height = summary_square // new_width
                return Rectangle(new_width, new_height)
    
    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print(r1)
print(r2)
print(r3)
print(r4)

