'''
@Auther: Subendu Das
@Date: 2021-11-10 08:00:30
@Last modified by: Subendu Das
@Last modified time: 2021-11-10 08:00:30
@Title: StopWatch
Desc -> Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
'''
import time
class stopwatch:
    def __init__(self):
        input("Press Enter to continue and ctrl+C to exit the stopwatch")
        while True:
            try:
                 start_time=time.time()
                 print("Stopwatch has started")
                 while True:
                      print("Time elapsed:",round(time.time()-start_time,0),'secs',end='\n')
                      time.sleep(1)
            except KeyboardInterrupt:
                 print("Timer has stopped")
                 end_time=time.time()
                 print("The time elapsed:",round(end_time-start_time,4),'secs')

obj=stopwatch()