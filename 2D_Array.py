'''
@Auther: Subendu Das
@Date: 2021-11-11 09:00:03
@Last Modified by: Subendu Das
@Last Modified Time: 09:00:03
@Title: 2D Array
a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
'''
def Two_D_Array():'''This Function prints the 2D_array by taking user-Input.'''
    
rows = int(input("enter number of rows: "))
columns = int(input("enter number of columns: "))
matrix=[]
print('Enter Elements')
try:
        for i in range(0,rows):
            array=[]
            for j in range(0,columns):
                array.append(int(input()))
            matrix.append(array)
        print('2D Array.')
        for i in range(0,rows):
            for j in range(0,columns):
                print(matrix[i][j], end=' ')
            print()
except Exception as e:
     print(e)

Two_D_Array()     