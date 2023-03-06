import math


class Point:
    '''Represents a point in 2-D space'''


blank = Point()

blank.x = 3.0
blank.y = 4.0

# distance = math.sqrt(blank.y**2 + blank.x**2)
# print('(%g, %g)' % (blank.y, blank.x), ">> '(%g, %g)' % (blank.y, blank.x)")


def print_point(p):
    print('(%g, %g)' % (p.y, p.x))


# print(print_point(blank))


def distance_between(x, y):
    distance = x - y
    return distance


class Rectangle:
    '''represents a rectangle.
    attributes: width, height, corner
    '''


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p


center = find_center(box)

# print(print_point(center), ">> print_point(center)")

box.width = box.width + 50
box.height = box.height + 100


def grow_rectangle(rect, dwidth: int, dheight: int):
    rect.width += dwidth
    rect.height += dheight


# print(box.width, box.height, ">> h & w")

grow_rectangle(box, 50, 100)

# print(box.width, box.height, ">> new h & w")


# ====== NOT WORKING =====
def new_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


# print(new_rectangle(box, 5, 10))

p1 = Point()
p1.x = 5
p1.y = 10

import copy

p2 = copy.copy(p1)

# print(p2.x)
# print(p2.y)
# print(p1 is p2)
# print(p1 == p2)

box2 = copy.copy(box)
# print(box2.width)
# print(box2.corner.x)

# print(box2 is box)
# print(box2.corner is box.corner, "box2")

box3 = copy.deepcopy(box)

print(box3 is box)
print(box3.corner is box.corner, "box 3")

print(type(box))
print(isinstance(blank, Rectangle))

print(hasattr(box, 'width'))
print(hasattr(p1, 'x'))