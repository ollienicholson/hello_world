# Result:
# GUI runs, alarm clock does not ring at se time, otherwise works as expected
# https://data-flair.training/blogs/alarm-clock-python/

from tkinter import Tk, Label, StringVar, Entry, Button
import datetime
import time
import winsound
'''
Create alarm functions
'''


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d-%m-%y")
        print("The Set Date is: ", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to wake up!")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break


def actual_time():
    set_alarm_timer = f'''{hour.get()}:{minutes.get()}:{seconds.get()}'''
    alarm(set_alarm_timer)


'''
Initiate alarm clock GUI
'''
# inti tkinter
clock = Tk()

# set title
clock.title("Alarm Clock")
# set GUI size
clock.geometry("400x200")

# formatting the GUI
time_format = (
    Label(
        clock,
        text="Enter time in 24 hour format",
        fg='red',
        bg='black',
        font='Arial'
    ).place(x=80, y=120)
)
addTime = Label(clock, text="Hour Min Sec", font=60).place(x=110)

setYourAlarm = (
    Label(
        clock,
        text="When to wake up: ",
        fg='black',
        font=("Helvetica", 7, "bold")
    ).place(x=5, y=29)
)

# Variables we require to set the alarm (initialisation):
hour = StringVar()
minutes = StringVar()
seconds = StringVar()

# Time required to set the alarm clock
hourTime = (
    Entry(clock, textvariable=hour, bg='pink', width=15).place(x=110, y=30)
)
minTime = (
    Entry(clock, textvariable=minutes, bg='pink', width=15).place(x=150, y=30)
)
secTime = (
    Entry(clock, textvariable=seconds, bg='pink', width=10).place(x=200, y=30)
)

# take the time input from the user
submit = (
    Button(clock, text="Set Alarm", fg='red', width=10,
           command=actual_time).place(x=110, y=70)
)

# run the window
clock.mainloop()
