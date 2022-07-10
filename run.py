import time

def menu():
    print('Welcome to pomopeep! 🍅')
    sessions = int(input('Choose the amount of sessions you want to work on: '))
    work_time = int(input('Enter the amount of minutes you will be working: '))
    break_time = int(input('Short break time: '))
    countdown(sessions, work_time, break_time)

def timer(t, state):
    minutes, seconds = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(state, timer, end="\r")

def countdown(sessions, work_time, break_time):
    for i in range(sessions):
        wt = work_time
        bt = break_time
        while wt:
            state = '💪Work'
            timer(wt, state)
            time.sleep(1)
            wt -= 1
        print("", end="\r")
        
        while bt:
            state = '😎Break'
            timer(bt, state)            
            time.sleep(1)
            bt -= 1
        print("", end="\r")
menu()
