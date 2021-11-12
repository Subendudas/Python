'''
@Auther: Subendu Das
@Date: 2021-11-11 10:00:30
@Last Modified by: Subendu Das
@Last Modified Time: 10:00:30
@Title: Windchill index
a. Desc -> This program takes a two input temperature and windspeed and determines
the windchill index.
'''
import math
def windchillindex(): '''At this function this checks the condition for temperature to be under 50 and windspeed between 3 to 120.'''
tempe=float(input("Enter Temperature: "))
windspeed=float(input("Enter wind speed: "))
try:
        if tempe<50 and windspeed>=3 and windspeed<120:

         v=(math.pow(windspeed,0.16))
        windchill=35.74+0.6215*tempe+(0.4275*tempe-35.75)*v
        print("windchill={}".format(windchill))
except:
        print("Invalid Input.")

windchillindex()    
