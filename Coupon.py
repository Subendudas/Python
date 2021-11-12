'''
@Auther: Subendu Das
@Date: 2021-11-11 11:00:03
@Last Modified by: Subendu Das
@Last Modified Time: 11:00:03
@Title: Coupon Numbers using oops concept.
Desc -> Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
'''
import random
'''Class Created'''
class coupon_num():
    '''Funcion Created'''
    def coupon(self):
         coupon = []
         randon_num=0

         try:
             no_of_coupon=int(input('How many coupon you want: '))
             print('coupons:- ')
             for i in range(no_of_coupon):
                 coupon_num=random.randint(10,100)
                 if coupon_num not in coupon:
                     coupon.append(coupon_num)
                     randon_num+=1
                     print(coupon_num)

                 print('Total random number: ',end=' ')
                 print(randon_num)
         except Exception as e:
             print(e)

if __name__ == '__main__':
     obj=coupon_num()  ,'''creating object of class coupon_num()'''
     obj.coupon()      ,'calling the function'