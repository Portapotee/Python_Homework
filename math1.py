def maxFraction(first, sec): 
      
    a = first[0]; b = first[1] 
    c = sec[0]; d = sec[1] 
  
    Y = a * d - b * c 
  
    return first if Y<0 else sec

def arabicNumbers(romanNumerals):
    D=500
    C=100
    L=50
    X=10
    V=5
    I=1
    sum = 0
    for i in romanNumerals:
        if(i =="D"): sum += 500
        if(i =="C"): sum += 100
        if(i =="L"): sum += 50
        if(i =="X"): sum += 10
        if(i =="V"): sum += 5
        if(i =="I"): sum += 1
    return sum

def add(x,y,z):
    print("%d. %d + %d = %d" % (z,x,y,x+y))

def sub(x,y,z):
    print("%d. %d - %d = %d" % (z,x,y,x-y))

def mutiply(x,y,z):
    print("%d. %d x %d = %d" % (z,x,y,x*y))

def divide(x,y,z):
    print("%d. %d / %d = %d" % (z,x,y,x/y))



def addList(x):
    sum = 0
    result = '';
    for s in x:
        sum += s
        result += str(s) + ' + '
    result = result[:len(result)-2]
    print(f'{result}= {sum}')



def primeNumber(Number):
    flag = True

    for i in range(2,(Number//2)):
        if(Number % i == 0):
            flag = False
            break

    return flag

def rangePrime(x,y):
    list1 = []
    for i in range(x,y+1):
        if(primeNumber(i)):
            list1.append(i)
    return list1


def countPrime(x,y):
    list1 = rangePrime(x,y)
    return len(list1)
