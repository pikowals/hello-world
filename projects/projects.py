###########################################################################################################
"""Find PI to the Nth Digit -
Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go."""
#########################################################################################################################
# import random
# import math
# from decimal import Decimal
# def piGenerator():
#     try:
#         m = input('Podaj ile liczb po przecinku chcesz zobaczyc w liczbie pi: ')
#         m = int(m)
#         if m > 50:
#             print('Program wyswietla maksmalnie 39 liczb po przecinku')
#             raise Exception('Maksymalna liczba po przecinku osiągnięta')
#         SquarePoints = 0
#         CirclePoints = 0
#         n = 1000000
#         while SquarePoints < n:
#             x = random.random()
#             y = random.random()
#             SquarePoints = SquarePoints + 1
#             if (x*x + y*y < 1):
#                 CirclePoints = CirclePoints + 1
#         pi = Decimal(4*CirclePoints/SquarePoints)
#         print(format(pi, f'.{m}f'))
#     except Exception as err:
#         print(str(err))
# piGenerator()
# print(format(math.pi, f'.{m}f'))
# z = round(random.uniform(0,90),5)
# print(z)
#########################################################################################################################
"""Find e to the Nth Digit - 
Just like the previous problem, but with e instead of PI. 
Enter a number and have the program generate e up to that many decimal places. 
Keep a limit to how far the program will go."""
#########################################################################################################################
# from decimal import Decimal
# def eNumberGenerator():
#     try:
#         x = input('Podaj liczbę liczb po przecinku do których ma wyświetlać się liczba Eulera, liczba nie może przekraczać 40: ')
#         x = int(x)
#         if x > 40:
#             raise Exception('Nie można wyświetlić więcej niż 40 liczb po przecinku!BŁĄD!')
#         e = (1+(1/100000))**100000
#         dec_e = Decimal(e)
#         print(format(dec_e, f'.{x}f'))
#
#     except Exception as error:
#         print(str(error))
# eNumberGenerator()
#########################################################################################################################
"""Fibonacci Sequence - 
Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number."""
#########################################################################################################################
# def FibSeq():
#     a = 0
#     b = 1
#     print('Wprowadz ile liczb fibonacciego chcesz otrzymac: ')
#     nfib = input()
#     print(a, end=' ')
#     print(b, end=' ')
#     for i in range(int(nfib)):
#         c = a + b
#         a = b
#         b = c
#         print(c, end=' ')
# FibSeq()
#########################################################################################################################
"""Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them."""
#########################################################################################################################
# def primeFactor():
#     print('Wprowadz liczbe ')
#     nPrime = input()
#     for i in range(1,int(nPrime)+1):
#         divNum = 0
#         n = (int(nPrime)%i)
#         if n == 0 and i>1:
#             for j in range(1,i+1):
#                 if i%j == 0:
#                     divNum = divNum +1
#             if divNum <= 2:
#                 print('%s jest liczbą pierwszą ' % i)
# primeFactor()

#########################################################################################################################
"""Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one."""
#########################################################################################################################

def checkIfPrime(value):
    divNr = 0
    for i in range(1,value+1):
        if value%i == 0:
            divNr +=1
    if divNr == 2:
        return True
    else:
        return False
def nextPrimeWish():
    value = 1
    while True:
        print('Would you like to see prime number: ')
        userInp = input()
        if userInp == 'yes':
            if checkIfPrime(value):
                print(value)
            else:
                while True:
                    value+=1
                    if checkIfPrime(value):
                        print(value)
                        break
                    else:
                        value+=1
                        continue
            value+=1
        elif userInp == 'no':
            print('Finishing for today, bye!')
            break
        else:
            print('Not recognized command, try again...')
            continue


nextPrimeWish()
