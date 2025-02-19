"""
Make a func to display triangles
"""

class Shape:
    width = 5
    height = 5
    printChar = '#'

    def printRow(self, i):
        raise NotImplementedError("Will be implemented by children extending this class")

    def print(self):
        for i in range(self.height):
            self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
    def __init__(self, height=5):
        self.height = height
    def printRow(self, i):
        print(self.printChar * i)

    def printi(self):
            self.printRowi()
    def printRowi(self):
        for i in range (self.height*2-1):
            if i % 2 != 0:
                print(' '*int(self.height-i/2) + self.printChar * i)
            else:
                continue

b = Triangle(24)
b.printi()
b.print()