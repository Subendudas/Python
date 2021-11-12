'''
@Auther: Subendu Das
@Date: 2021-11-07 09:30:30
@Last Modified by: Subendu Das
@Last Modified Time: 09:30:30
@Title: Leap Year
'''
def CheckLeap(Year):
  try:
  # Checking if the given year is leap year
    if(Year>999):
      if((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):
        print("Given Year is a leap Year"); 
  # Else it is not a leap year  
      else:
        print ("Given Year is not a leap Year")
    else:
      print("Please enter 4 digit input")
  except Exception as e:
    print(Exception)     
# Taking an input year from user  
Year = int(input("Enter the number: "))   
# Printing result  
CheckLeap(Year)