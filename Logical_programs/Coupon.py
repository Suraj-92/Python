'''
Author: Suraj N Temkar
Date: 12/04/2021
Title: Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number? 
    This program simulates this random process.
'''


import random

def AddCouponNumber():
    try:
        couponSet = set()
        condition = True

        while condition == True:
            userCoupon = int(input('Enter distinct numbers: '))
            couponSet.add(userCoupon)
            print('Number added: ', userCoupon)
            anotherNumber = input('Add Another Number Enter y/Y, or enter any other key to stop: ')
            if anotherNumber == 'y' or anotherNumber == 'Y':
                condition = True
            else:
                condition = False

        sortedUserCoupon = sorted(couponSet)
        firstElement = sortedUserCoupon[0]
        lastElement = sortedUserCoupon[len(sortedUserCoupon) - 1]
        Coupons = set()
        condition2 = True
        while condition2 == True:
            randomCoupan = random.randint(firstElement,lastElement)
            print('generated coupon: ', randomCoupan)

            Coupons.add(randomCoupan)
            generateAnotherCoupon=input('Enter y/Y to generate another coupon, or press any other key to see all generated coupons: ')
            if generateAnotherCoupon=='y' or generateAnotherCoupon=='Y':
                condition2=True
            else:
                condition2=False

        print('Coupon set is:',Coupons)

    except Exception as e:
        print(e)       

if __name__ == '__main__':
    AddCouponNumber()