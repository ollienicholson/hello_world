# debugging function - returns false if times are not valid
def valid_time(time):
    """
    Checks whether a Time object satisfies the invariants.
    time: Time
    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


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

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


# time = Time()
# time.hour = 11
# time.minute = 59
# time.second = 30

start = Time()
start.hour = 24
start.minute = 45
start.second = 30

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

time = Time(9, 45, 30)
# print(time.print_time(), ">> time.print_time()")
print(time, ">> time")

# print(Time.print_time(start), ">> Time.print_time(start)")
Time.print_time(start)

# print(start.print_time(), ">> start.print_time()")

# print(print_time(time))
end = start.increment(1337)
# print(end.print_time(), ">> end.print_time()")

print(end.is_after(start), ">>> end.is_after(start)")
# prints out True or False as per the function above

# time.is_after(50, 30)

# Pure Functions
# --------------


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum


# done = add_time(start, duration)
# print(print_time(done), "print_time(done)")

# Modifiers
# -----------


def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1


# print(mod_increment(start, 30), "pure_increment(start, 30)")


# converts time o integers
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


# print(time_to_int(start))  # == 35160 seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


# consistency check
# print(time_to_int(int_to_time(10)) == 10)  # True


# option 1 for error checking
def new_add_time(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in new_add_time')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


# option 2 for error checking
def new_add_time1(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


newTime = new_add_time(start, duration)

newTime1 = new_add_time1(start, duration)

# print(Time.print_time(newTime), "print_time(done)")  # == 11:20:30

# print(Time.print_time(newTime1), "print_time(done)")  # == 11:20:30

thistime = increment(start, 30), "increment(newTime, 30)"
