'''
@Auther: Subendu Das
@Date: 2021-11-10 10:00:30
@Last Modified by: Subendu Das
@Last Modified Time: 10:00:30
@Title: Distance Between Two Coordinates
a. Desc -> This program takes input as coordinates and find the distance between them.
'''
import math

a=input("enter first coordinate : ")
p1 = a.split(",")
b=input("enter second coordinate : ")
p2 = b.split(",")
try:
 distance = math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2) )
except Exception as e:
    print(e)
else:
 print("distance between ", a,"and", b, "is",distance) 