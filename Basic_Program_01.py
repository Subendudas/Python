'''
@Auther: Subendu Das
@Date: 2021-11-07 08:00:30
@Last Modified by: Subendu Das
@Last Modified Time: 08:00:30
@Title: User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''
try:
    username=input("Enter Username: ")
    if len(username)>=3:
     print("Hello "+ username+ ", How are you?")
except Exception as e:
    print(e)
    print(Exception)
    print("Username must contain atleast 3 characters.")