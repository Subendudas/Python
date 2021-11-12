'''
@Auther: Subendu Das
@Date: 2021-11-09 08:00:30
@Last Modified by: Subendu Das
@Last Modified Time: 08:00:30
@Title: Power of 2
a. Desc -> This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
'''
def power_of_2():
    value = int(input("Enter Value - "))
    try:

    #check if input is in range of 0 to 31
        if 0 <= value < 31:
            for power_value in range(0, value+1):
                generate_number = 2**power_value
                print("2^" + str(power_value) + " = " + str(generate_number))
        else:
            print("Please enter number less than 31 and greater than or equal to 0 ")
    except:
        print(Exception)        
      #power_of_2()
power_of_2()