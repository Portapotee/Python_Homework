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

def add(x,y):
    print("%d + %d = %d" % (x,y,x+y))

def sub(x,y):
    print("%d - %d = %d" % (x,y,x-y))

def multiply(x,y):
    print("%d x %d = %d" % (x,y,x*y))

def divide(x,y):
    print("%d / %d = %d" % (x,y,x/y))

def exponent(x,y,z):
    print("%d. %d ^ %d = %d" % (z,x,y,x**y))

def convertTocelsius(x):
    print("%d degrees Fahrenheit is %d degrees Celsius" % (x,(x-32)*(5/9)))
    

def convertTofahrenheit(x):
    print("%d degrees Celsius is %d degrees Fahrenheit" % (x,x*(9/5)+32))

def addList(x):
    sum = 0
    result = '';
    for s in x:
        sum += s
        result += str(s) + ' + '
    result = result[:len(result)-2]
    # return(f'{result}= {sum1}')
    f'{result}= {sum}'
    return(sum)

def subList(x,y):
    sum = x
    result = '';
    for s in y:
        sum -= s
        result += str(s) + ' - '
    result = result[:len(result)-2]
    # return(f'{result}= {sum1}')
    f'{result}= {sum}'
    return(sum)

def multiplyList(x):
    sum = 0
    result = '';
    for s in x:
        if sum == 0:
            sum += s
        else:
            sum = sum*s
            # result += str(s) + ' + '
    result = result[:len(result)-2]
    # return(f'{result}= {sum1}')
    f'{result}= {sum}'
    return(sum)

def divideList(x,y):
    sum = x
    result = '';
    for s in y:
        if sum == 0:
            sum += s
        else:
            sum = sum/s
        # result += str(s) + ' - '
    result = result[:len(result)-2]
    # return(f'{result}= {sum1}')
    f'{result}= {sum}'
    return(sum)

# def primeNumber(Number):
#     flag = True

#     for i in range(2,(Number//2)):
#         if(Number % i == 0):
#             flag = False
#             break

#     return flag

# def rangePrime(x,y):
#     list1 = []
#     for i in range(x,y+1):
#         if(primeNumber(i)):
#             list1.append(i)
#     return list1

# def countPrime(x,y):
#     list1 = rangePrime(x,y)
#     return len(list1)

def add2(x,y):
    if type(x) not in [int, float, tuple, list]:
        raise TypeError("Please enter real numbers")
    if type(y) not in [int, float, tuple, list]:
        raise TypeError("Please enter real numbers")
    if type(x) in [tuple]:
        a = []
        for i in x:
            a.append(i)
        x = addList(a)
    if type(y) in [tuple]:
        a = []
        for i in y:
            a.append(i)
        y = addList(a)
    if type(x) in [list]:
        x = addList(x)
    if type(y) in [list]:
        y = addList(y)
    return(x+y)
    print("Done.")


def add3(x,y):
    try:
        sum = add2(x,y)
        print(x,'+',y,'=',sum)
    except Exception as err:
        print("Error:", err)


def sub2(x,y):
    if type(x) not in [int, float, tuple, list]:
        raise TypeError("Please enter real numbers")
    if type(y) not in [int, float, tuple, list]:
        raise TypeError("Please enter real numbers")
    if type(x) in [tuple]:
        a = []
        for i in x:
            a.append(i)
        x = addList(a)
    if type(y) in [tuple]:
        a = []
        for i in y:
            a.append(i)
        y = addList(a)
    if type(x) in [list]:
        x = addList(x)
    if type(y) in [list]:
        y = addList(y)
    return(x-y)
    print("Done.")

def sub3(x,y):
    try:
        difference = sub2(x,y)
        print(x,'-',y,'=',difference)
    except Exception as err:
        print("Error:", err)


def multiply2(x,y):
    if type(x) not in [int, float, tuple, list]:
        raise TypeError("Please enter real numbers")
    if type(y) not in [int, float, tuple, list]:
        raise TypeError("Please enter real numbers")
    if type(x) in [tuple]:
        a = []
        for i in x:
            a.append(i)
        x = multiplyList(a)
    if type(y) in [tuple]:
        a = []
        for i in y:
            a.append(i)
        y = multiplyList(a)
    if type(x) in [list]:
        x = multiplyList(x)
    if type(y) in [list]:
        y = multiplyList(y)
    return(x*y)
    print("Done.")

def multiply3(x,y):
    try:
        product = multiply2(x,y)
        print(x,'x',y,'=',product)
    except Exception as err:
        print("Error:", err)


def divide2(x,y):
    if type(x) in [tuple, list]:
        raise TypeError("Please enter an integer")
    if type(x) not in [int, float]:
        raise TypeError("Please enter real numbers")
    if type(y) not in [int, float, tuple, list]:
        raise TypeError("Please enter real numbers")
    if type(x) in [tuple]:
        a = []
        for i in x:
            a.append(i)
        x = divideList(a)
    if type(y) in [tuple]:
        a = []
        for i in y:
            a.append(i)
        y = divideList(x,a)
    if type(x) in [list]:
        x = divideList(x)
    if type(y) in [list]:
        y = divideList(x,y)
    if y == 0:
        raise TypeError("The answer is Undifined")
    return(y)
    print("Done.")

def divide3(x,y):
    try:
        dividend = divide2(x,y)
        print(x,'/',y,'=',dividend)
    except Exception as err:
        print("Error:", err)