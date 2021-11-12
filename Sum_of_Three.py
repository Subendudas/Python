'''
@Auther: Subendu Das
@Date: 2021-11-11 10:30:30
@Last Modified by: Subendu Das
@Last Modified Time: 10:30:30
@Title: Sum of three Integer adds to ZERO
Desc -> A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0.
'''
'''Fuction to find sum of three integer which adds to zero.'''
def findTriplets(arr, n): 
  
    found = True
    for i in range(0, n-2): 
      
        for j in range(i+1, n-1): 
          
            for k in range(j+1, n): 
              
                if (arr[i] + arr[j] + arr[k] == 0): 
                    print(arr[i], arr[j], arr[k]) 
                    found = True           
    # If no triplet with 0 sum  
    # found in array 
    if (found == False): 
        print(" not exist ") 
  
# Driver code 
arr = [0, -1, 2, -3, 1] 
n = len(arr) 
findTriplets(arr, n) 