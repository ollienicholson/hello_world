# Named Tuples
from collections import namedtuple


# Conventional class definition
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)


# Simplified class definition using namedtuple

Point_simple = namedtuple("Point", ["x", "y"])
# print(Point_simple)  # Output: <class '__main__.Point'>

p = Point_simple(1, 2)  # Output: Point(x=1, y=2)
# print(p)

# print(p.x, p.y) # Output: 1 2

# print(p[0], p[1]) # Output: 1 2

# ====== this is good for simple class construction =====

# if you wish to add complexity to the class, you can initialize the class within the class,
#   otherwise you could refactor the named tuple as a conventional class.


class Pointier(Point_simple):
    # add more methods to the class
    #  e.g. distance from origin
    pass
