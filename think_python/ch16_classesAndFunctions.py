class Time:
    '''Represents the time of day.
    attributes: hour, minute, second
    '''


time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def print_time(time):
    # returns a string representation of time in hh.mm.ss
    return '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)


print(print_time(time))


def is_after(t1, t2):
    print(t1 > t2)


is_after(50, 30)
