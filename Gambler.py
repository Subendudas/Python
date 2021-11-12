'''
@Author: Subendu Das
@Date: 11-11-2021 07:15:00
@Last modified by: Pavani
@Last modified time: 07-11-2021 07:15:00
@Title: Gambler
Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
        he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
        times he/she wins and the number of bets he/she makes. 
'''
import random
class Myclass:       #created class
 def __init__(self,stake,goal,number): #parameterized constructor'
        self.stake = stake
        self.goal = goal
        self.number = number

 def gambler(self,stake,goal,number):

    win_count = 0
    loss_count = 0
    count = 0
    while (stake > 0 and stake < goal and count < number):   
        try:           
           count = count + 1
           random_generated = random.randint(0,1)    #if suppose randint() given three parameters generating type error exception
                                                     # randint() Return random integer in range [a, b], including both end points.
           if (random_generated == 1):
               win_count = win_count + 1
               self.stake = self.stake + 1
           else:
               loss_count = loss_count + 1
               self.stake = self.stake - 1
        except Exception as e:
                print(e)
                print("error found as you entered invalid input" )                     #to find type of exception type(e).

    percent_winning = (win_count/number)*100
    percent_loss = 100-percent_winning
    print("Number of wins",win_count)
    print("winning percent :",percent_winning,'%')
    print("loss percent :",percent_loss,'%' )
if __name__ == '__main__':                                 #main function
    stake = int(input("Enter the stake amount :"))
    goal = int(input("Enter your goal amount : "))
    number = int(input("How many times you want to bet :"))

    obj = Myclass(stake,goal,number)         ,'object of Myclass'
    obj.gambler(stake,goal,number)         ,'caling function gambler'