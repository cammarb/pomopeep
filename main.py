import time
import datetime

def menu():
    print('Pomopeep! 🍅')
    print('-----------------------')
    sessions = int(input('Number of sessions: '))
    work_time = int(input('Working time (min): '))
    break_time = int(input('Short break time (min): '))
    print('-----------------------')
    countdown(sessions, work_time, break_time)

def timer(t, state):
    # minutes, seconds = divmod(t*60, 60)
    timer = datetime.timedelta(seconds = t)
    print(state, timer, end="\r")

def countdown(sessions, work_time, break_time): 

    for i in range(sessions): 
        #if sessions >=4:
         #   if i == 3:
          #      break_time = break_time*3
           # else:
            #    break_time
        wt = work_time*60
        bt = break_time*60
        while wt > -1:
            state = '💪Work'
            timer(wt, state)
            time.sleep(1)
            wt -= 1
            print("                     ", end="\r")
        
        while bt > -1:
            state = '😎Break'
            timer(bt, state)            
            time.sleep(1)
            bt -= 1
            print("                      ", end="\r")
        
        if i == sessions-1:
            print("Done. Good job!")
        
menu()
