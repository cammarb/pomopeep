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
        while work_time:
            state = '💪Work'
            timer(work_time, state)
            time.sleep(1)
            work_time -= 1
        print("", end="\r")
        print('Time for a break!', end="\r")
        print("", end="\r")
        while break_time:
            state = '😎Break'
            timer(break_time, state)            
            time.sleep(1)
            break_time -= 1
menu()
