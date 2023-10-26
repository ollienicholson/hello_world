#  GATHERING KEYWORD ARGUMENTS

#  The * operator can be used to gather keyword arguments into a tuple.
#  The ** operator can be used to gather keyword arguments into a dictionary.

from namedTuples import Point


def printall_tup(*args: tuple):
    '''
    Returns a tuple of the given args.
    We use the * operator to gather keyword arguments into a tuple.
    '''
    print(args)


printall_tup(1, 2.0, '3')  # returns a tuple: (1, 2.0, '3')


def printall_dict(**args: dict):
    '''
    Returns a dictionary of the given args.
    We use the ** operator to gather keyword arguments into a dictionary.
    '''
    print(args)


printall_dict(
    x=1, y=2.0, z='3'
)  # returns a dictionary: {'x': 1, 'y': 2.0, 'z': '3'}


def printall_legend(*args, **kwargs):
    '''
    Returns a tuple of the given args and a dictionary of the given kwargs.
    We use both the * and ** operators to gather keyword arguments into a tuple and dictionary.
    '''
    print(args, kwargs)


printall_legend(1, 2.0, third='3')

# NOTE: if you have a dictionary and you want to pass its contents as keyword arguments, you can use the ** operator.
#  e.g. printall_dict(**d) where d is a dictionary.

d = dict(x=1, y=2)
# Point(d) # will not work as Point expects x and y as keyword arguments
Point(**d)  # will work as Point expects x and y as keyword arguments

print(Point(**d))  # returns a Point object: (1, 2) CORRECTO!!
