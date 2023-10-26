class Time:
    '''
    Represents the time of day.
    
    attributes: hour, minute, second.
    '''
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        # returns a string representation of time in hh.mm.ss
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        '''prints a string representation of time in hh.mm.ss '''
        print(str(self))

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

        # converts time o integers
    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

    # print(time_to_int(start))  # == 35160 seconds
    def __radd__(self, other):
        return self.__add__(other)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    # when using the '+' operator, python calls the __add__ method. Which means you can add two time objects together. Interesting!
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


start = Time(9, 45)
duration = Time(1, 35)
# print(start + duration, "> using add_time")

print(start + 1337, "> using __add__")
print(1337 + start, "> using __Radd__")


def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))


print_attributes(start)  # prints the attributes of the object
# print_attributes(duration)