from math1 import *
print("1. 2020 - 20 =", 2020 - 20)
add(2020, 20, 1)
sub(2020, 20, 1)
list1 = [2020,20,50,120]
addList(list1)
# print("2. 494 + 118 =", 494 + 118)
add(494, 118, 2)
# print("3. The tens digit of 1296 is", "1296" [-2])
# print("4. 60/5 = ", 60/5)
# print("5. 14 x 50 =", 14*50)
multiply(14,50,5)
# print("6. The remainder of 66/4 is", 66 % 4)
# print("7. The product of 14 and 3 is", 14*3)
# print("8.  8 x 11 + 8 =", 8*11+8)
# print("9. 53 + 12 + 28 + 7 =", 53+12+28+7)
list3 = [53,12,28,7] #define list
addList(list3)
# print("10. 201 + 402 + 804 + 603 =", 201+402+804+603)

# import math

# print("11. 1987 rounded to the nearest ten is", math.floor((1987+5)/10)*10)
# print("12. 17^2 =", 17**2)
multiply(17,17,12)
# print("13. 578 - 361 - 27 =", 578-361-27)
# print("14. 11 x 48 =", 11*48)
# print("15. 681 - 292 =", 681-292)
# print('16. 45 x 18 =', 45*18)
sum = arabicNumbers('CVVI')

print('17. CVVI in Arabic Numerals is', sum)
# print('18. 37 + 41 + 45 =', 37+41+45)
# print('19. 32 x 28 =', 32*28)
# print('20. 398 x 202 =', 398*202)
# print('21. 36 x 25', 36*25)
# print('22. 44 x 3/33 =', 44*3/33)

# import math
# print('23. The GCD of 28 and 21 is ',end='' )
# print (math.gcd(28,21)) 

# print("24. 342/18 =", 342/18)
# print('25. If 1 yard is equal to 3 feet than 63 feet is equal to',63/3,'yards.')
# print('26. 24^2 =', 24**2)
print('27. The smaller of 5/8 and 3/5 is ',end='')
  

def maxFraction(first, sec): 
      
    a = first[0]; b = first[1] 
    c = sec[0]; d = sec[1] 
  
    Y = a * d - b * c 
  
    return first if Y<0 else sec
   
first = ( 5, 8 ) 
sec = ( 3, 5 ) 
res = maxFraction(first,sec) 
print(str(res[0]) + "/" + str(res[1]))
#code from https://www.geeksforgeeks.org/gcd-in-python/

# print('28. 5/8 + 1/24 = ', end='')
 
# def gcd(a, b): 
#     if (a == 0):  
#         return b;  
#     return gcd(b % a, a);  
  
# def lowest(den3, num3):  
    
#     common_factor = gcd(num3, den3);  
    
#     den3 = int(den3 / common_factor);  
#     num3 = int(num3 / common_factor); 
#     print(num3, "/", den3); 
    
# def addFraction(num1, den1, num2, den2):  
  
#     den3 = gcd(den1, den2);  
  
#     den3 = (den1 * den2) / den3;  
   
#     num3 = ((num1) * (den3 / den1) + 
#             (num2) * (den3 / den2));  
  
#     lowest(den3, num3);  
   
# num1 = 5; den1 = 8;  
# num2 = 1; den2 = 24;  
  
# addFraction(num1, den1, num2, den2); 
# #code from https://www.geeksforgeeks.org/program-to-add-two-fractions/

# print('29. Seventeen weeks is', 7*17, 'days.')
# print('30. 29 x 41 x 61 =', 21*41*61)
# print('31. 9 + 13 + 17 + 21 + 25 =', 9+13+17+21+25)
# print('32. 65^2 =', 65**2)
# print('33. 1.444 x 10^3 =', 1.444*10**3)
# print('34. The LCM of 28 and 21 is ', end='')

# a=28
# b=21
# if(a>b):
#     min1=a
# else:
#     min1=b
# while(1):
#     if(min1%a==0 and min1%b==0):
#         print(min1)
#         break
#     min1=min1+1
# #code from https://www.sanfoundry.com/python-program-find-lcm-two-numbers/

# print('35. 54 x 101 =', 54*101)
# print('36. The number of multiples between 5 and 11 is ',end='')

# a = [5, 6, 7, 8, 9, 10, 11]

# print(a.count(5) + (a.count(10)))
# #code from https://www.tutorialgateway.org/python-count-list-items/

# print('37. 63 x 63 =', 63*67)
# print('38. The number of prime numbers that are between 40 and 50 is ',end='')

# l,u= 40, 50
# c=0
# for i in range(l,u + 1):
#    if  i> 1:
#        for j in range(2,i):
#            if (i%j) == 0:
#                break
#        else:
#            c+=1
# print(c)
# #code from https://spicycoders.blogspot.com/2017/08/count-primes-in-range-python.html

# print('39. 99 x 42 =',99*42)
# print('40. The cube root of 511111 is', 51111**(1/3))
# print('41. 32^2 - 21^2 =', (32**2) - (21**2))
# print('42. The square root of 784 is', 784**(1/2))
# print('43. The remainder of 458/11 is', 458 % 11)
# print('44. 2^9 =',2**9)
# print('45. 112 x 103 =', 112*103)
# print('46. The next term is the arithmatic sequence 14,33,52,71,90,... is',(90 - 71)+90)
# print('47. 66 x 46 =', 66*46)
# print('48. The perimeter of a rectangle with sides of length 12 and 9 is', (12*2)+(9*2))
# print('49. 1/7 + 1/14 + 1/28 = ', end='')

# from fractions import*

# x = (1/7)+(1/14)+(1/28)
# str(Fraction(x))
# print(Fraction(x))

# print('50. 375 x 480 =', 375*480)
# print('51. 32^2 + 17^2 =', (32**2) + (17**2))
# print('52. 16(2/3)% = ', end='')

# print(str(float(((16*3)+2)/3))+'%')
# #code from https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value-in-python

# print('53. 4/9 of 1/4 of 99 is', (99*(1/4))*(4/9))
# print('54. If 4 + 12x = 36 then 3x + 1 =', (((36 - 4)/12)*3)+1)
# print('55. 92 x 92 =',92*92)
# print('56. The greatest possible perimeter of an isoceles triangle with sides of length 2 and 5 is', 5 + 2 + ((5-2)+3))
# print('57. The square root of 7056 is', 7056**0.5)
# print('58. 134 in base 8 in base 2 is ',)#end='')

# #y=((oct(134)))
# #print(bin(y))

# print('59. The sum of the terms in the arithmatic sequence 1,3,5,7,...,49 is')

# print('60. 285714 x 16 =', 285714*16)
# print('61. A fair dice is rolled twice. The probability of the two rolls summing to 9 is', (4*2)/(6*6))

# print('62. 241 x 111 =', 241*111)
# print('63. 9(5/8) x 9(3/8) = ' , end='')

# import fractions

# f1 = fractions.Fraction(((9*8)+5), 8)
# f2 = fractions.Fraction(((9*8)+3), 8)

# print((f1*f2))

# #code from https://www.w3resource.com/python-exercises/math/python-math-exercise-46.php

# print('64. The supplement to a 51 degree angle has a measure of', 180-51, 'degrees')
# print('65. If 6^x = 16 then 6^2x =', 16*16)
# print('66. The number 75 written in base 6 is')
# print('67. 7(2/3) x 11(2/3) = ', end='')

# import fractions

# f3 = fractions.Fraction(((7*3)+2), 3)
# f4 = fractions.Fraction(((11*3)+2), 3)

# print((f3*f4))

# print('68. 0.0666... (fraction) = ', end='')

# from fractions import Fraction

# print(Fraction(0.06))

# print('69. 72 x 625 =', 72*625)
# print('70. The square root of 10 to the power of 5 is', (10**0.5)**5)
# print('71. The cube root of 1259712 is', 1259712**(1/3))
# print('72. The hypotenuse of a right triangle with legs of length 20 and 21 is',((20**2)+(21**2))**0.5)
# print('73. 396 x 394 =', 396*394)
# print('74. An equilateral triangle with side of length 6 x the square root of 3 has a height of length', (6*(3**0.5))-((6*(3**0.5))/2))
# print('75. The number of positive integral divisors of 54 is')
# print('76. The mean of the set 9,21,20,22,23 is', (9+21+20+22+23)/5)
# print('77. The reciprocal of 20/19 is', 19/20)
# print('78. The eighth term in the geometric sequence 1/8, 1/4, 1/2 1,... is', ((1-(1/2))*4)+1)
# print('79. 16 x 22 x 15 =', 16*22*15)
# print('80. The square root of 2 time the square root of 101 time the square root of 9 times the square root of 2 is', (2**0.5)*(101**0.5)*(8**0.5)*(2**0.5))
