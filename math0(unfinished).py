print("1. 2020 - 20 =", 2020 - 20)
print("2. 494 + 118 =", 494 + 118)
print("3. The tens digit of 1296 is", "1296" [-2])
print("4. 60/5 = ", 60/5)
print("5. 14 x 50 =", 14*50)
print("6. The remainder of 66/4 is", 66 % 4)
print("7. The product of 14 and 3 is", 14*3)
print("8.  8 x 11 + 8 =", 8*11+8)
print("9. 53 + 12 + 28 + 7 =", 53+12+28+7)
print("10. 201 + 402 + 804 + 603 =", 201+402+804+603)

import math

print("11. 1987 rounded to the nearest ten is", math.floor((1987+5)/10)*10)
print("12. 17^2 =", 17**2)
print("13. 578 - 361 - 27 =", 578-361-27)
print("14. 11 x 48 =", 11*48)
print("15. 681 - 292 =", 681-292)
print('16. 45 x 18 =', 45*18)

D=500
C=100
L=50
X=10
V=5
I=1
sum = 0
for i in "DCLXXVI":
    if(i =="D"): sum += 500
    if(i =="C"): sum += 100
    if(i =="L"): sum += 50
    if(i =="X"): sum += 10
    if(i =="V"): sum += 5
    if(i =="I"): sum += 1

print('17. DCLXXVI in Arabic Numerals is', sum)
print('18. 37 + 41 + 45 =', 37+41+45)
print('19. 32 x 28 =', 32*28)
print('20. 398 x 202 =', 398*202)
print('21. 36 x 25', 36*25)
print('22. 44 x 3/33 =', 44*3/33)

import math
print('23. The GCD of 28 and 21 is ',end='' )
print (math.gcd(28,21)) 

print("24. 342/18 =", 342/18)
print('25. If 1 yard is equal to 3 feet than 63 feet is equal to',63/3,'yards.')
print('26. 24^2 =', 24**2)
print('27. The smaller of 5/8 and 3/5 is ',end='')
  
def maxFraction(first, sec): 
      
    a = first[0]; b = first[1] 
    c = sec[0]; d = sec[1] 
  
    Y = a * d - b * c 
  
    return sec if Y else sec 
   
first = ( 5, 8 ) 
sec = ( 3, 5 ) 
res = maxFraction(first, sec) 
print(str(res[0]) + "/" + str(res[1]))
#code from https://www.geeksforgeeks.org/gcd-in-python/

print('28. 5/8 + 1/24 = ', end='')
 
def gcd(a, b): 
    if (a == 0):  
        return b;  
    return gcd(b % a, a);  
  
def lowest(den3, num3):  
    
    common_factor = gcd(num3, den3);  
    
    den3 = int(den3 / common_factor);  
    num3 = int(num3 / common_factor); 
    print(num3, "/", den3); 
    
def addFraction(num1, den1, num2, den2):  
  
    den3 = gcd(den1, den2);  
  
    den3 = (den1 * den2) / den3;  
   
    num3 = ((num1) * (den3 / den1) + 
            (num2) * (den3 / den2));  
  
    lowest(den3, num3);  
   
num1 = 5; den1 = 8;  
num2 = 1; den2 = 24;  
  
addFraction(num1, den1, num2, den2); 
#code from https://www.geeksforgeeks.org/program-to-add-two-fractions/

print('29. Seventeen weeks is', 7*17, 'days.')
print('30. 29 x 41 x 61 =', 21*41*61)
print('31. 9 + 13 + 17 + 21 + 25 =', 9+13+17+21+25)
print('32. 65^2 =', 65**2)
print('33. 1.444 x 10^3 =', 1.444*10**3)
print('34. The LCM of 28 and 21 is ', end='')

a=28
b=21
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print(min1)
        break
    min1=min1+1
#code from https://www.sanfoundry.com/python-program-find-lcm-two-numbers/

print('35. 54 x 101 =', 54*101)
print('36. The number of multiples between 5 and 11 is ',end='')

a = [5, 6, 7, 8, 9, 10, 11]

print(a.count(5) + (a.count(10)))
#code from https://www.tutorialgateway.org/python-count-list-items/

print('37. 63 x 63 =', 63*67)
print('38. The number of prime numbers that are between 40 and 50 is ',end='')

l,u= 40, 50
c=0
for i in range(l,u + 1):
   if  i> 1:
       for j in range(2,i):
           if (i%j) == 0:
               break
       else:
           c+=1
print(c)
#code from https://spicycoders.blogspot.com/2017/08/count-primes-in-range-python.html

print('39. 99 x 42 =',99*42)
print('40. The cube root of 511111 is', 51111**(1/3))
print('41. 32^2 - 21^2 =', (32**2) - (21**2))
print('42. The square root of 784 is', 784**(1/2))