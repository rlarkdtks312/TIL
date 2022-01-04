def addNumber(num) :
    if num <= 1 :
        return 1
    return num + addNumber(num-1)
    
print(addNumber(10))


def fact(num) :
    if num <= 1 :
        return 1
    return num*fact(num-1)

print(fact(5))

def countDown(n) :
    if n == 0 :
        print("발사!!!")
        return 0
    print(n)
    countDown(n-1)

countDown(5)

def printStar(n):
    if n == 0 :
        return 0
    printStar(n-1)
    print('별'*n)
    
printStar(4)

def gugu(dan, num) :
    if dan == 0 :
        return
    gugu(dan-1, num)
    print(dan,'단 시작')
    for _ in range(9) :
        print("%d x %d = %d"%(dan, num, dan*num))
        num += 1
    
gugu(9,1)

def pow(x, n) :
    if n == 0 :
        return 1
    return x*pow(x,n-1)

print(pow(2,5))

import random as rd

def arySum(Ary, n) :
    if n == 0 :
        return 0
    return Ary[n-1] + arySum(Ary[:n],n-1)

ary = [rd.randint(1,20) for _ in range(10)]

N = len(ary)

print(arySum(ary, N))