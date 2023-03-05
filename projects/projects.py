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

# def checkIfPrime(value):
#     divNr = 0
#     for i in range(1,value+1):
#         if value%i == 0:
#             divNr +=1
#     if divNr == 2:
#         return True
#     else:
#         return False
# def nextPrimeWish():
#     value = 1
#     while True:
#         print('Would you like to see prime number: ')
#         userInp = input()
#         if userInp == 'yes':
#             if checkIfPrime(value):
#                 print(value)
#             else:
#                 while True:
#                     value+=1
#                     if checkIfPrime(value):
#                         print(value)
#                         break
#                     else:
#                         value+=1
#                         continue
#             value+=1
#         elif userInp == 'no':
#             print('Finishing for today, bye!')
#             break
#         else:
#             print('Not recognized command, try again...')
#             continue
# nextPrimeWish()

#########################################################################################################################
"""Find Cost of Tile to Cover W x H Floor - 
Calculate the total cost of tile it would take to cover a floor plan 
of width and height, using a cost entered by the user."""
#########################################################################################################################

# def sizeOfFloor():
#     print('Enter the size of the floor...')
#     print('Width ')
#     width = float(input())
#     print('Height  ')
#     height = float(input())
#     print('Enter total cost ')
#     cost = float(input())
#     area = width*height
#     totalCost = cost*area
#     return totalCost
# print(sizeOfFloor())

#########################################################################################################################
"""Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given 
Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. 
For added complexity, add an option for users to select the compounding interval 
(Monthly, Weekly, Daily, Continually)."""
#########################################################################################################################
# def mortgageCalc():
#     print('Enter how much you borrowed ')
#     borrowedMoney = float(input())
#     print('Enter the motrgage period in years ')
#     mortgagePeriod = int(input())
#     mortgagePeriodMonths = 12 * mortgagePeriod
#     print('Enter the interes rates ')
#     interestRates = float(input())
#     monthlyInterestRates = interestRates/100/12
#     top = (1+monthlyInterestRates)**mortgagePeriodMonths
#     bottom = ((1+monthlyInterestRates)**mortgagePeriodMonths) -1
#     fixedPayments = (borrowedMoney * (monthlyInterestRates*top)/bottom)
#     #fixedPayments = borrowedMoney*((interestRates*(1+interestRates)**mortgagePeriodMonths)/((1+interestRates)**mortgagePeriodMonths -1))
#     print(round(fixedPayments,2))
##############################SECOND SOLUTION##################################################################################
# mortgageCalc()

# months = int(input("Enter mortgage term (in months): "))
# rate = float(input("Enter interest rate: "))
# loan = float(input("Enter loan value: "))
#
# monthly_rate = rate / 100 / 12
# payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
# print(monthly_rate)
#
# print("Monthly payment for a $%.2f %s year mortgage at %.2f%% interest rate is: $%.2f" % (loan, (months / 12), rate, payment))
##############################SECOND SOLUTION############################################################################

#########################################################################################################################
"""Change Return Program - The user enters a cost and then the amount of money given. 
The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change."""
#########################################################################################################################

# def changeReturner():
#     hundredNr = 0
#     fiftyNr = 0
#     twentyNr = 0
#     tenNr = 0
#     fifeNr = 0
#     oneNr = 0
#     quarterNr = 0
#     dimeNr = 0
#     nickelNr = 0
#     penniesNr = 0
#     cost = float(input('Enter the cost of the product: '))
#     moneyGiven = float(input('Enter the amount of money given '))
#     moneyToBeReturned = moneyGiven - cost
#     print('Your change is %s'% round(moneyToBeReturned, 2))
#     while moneyToBeReturned >= 100:
#             hundredNr +=1
#             moneyToBeReturned = moneyToBeReturned - 100
#     while moneyToBeReturned >= 50:
#             fiftyNr += 1
#             moneyToBeReturned = moneyToBeReturned - 50
#     while moneyToBeReturned >= 20:
#             twentyNr += 1
#             moneyToBeReturned = moneyToBeReturned - 20
#     while moneyToBeReturned >= 10:
#             tenNr += 1
#             moneyToBeReturned = moneyToBeReturned - 10
#     while moneyToBeReturned >= 5:
#             fifeNr += 1
#             moneyToBeReturned = moneyToBeReturned - 5
#     while moneyToBeReturned >= 1:
#             oneNr += 1
#             moneyToBeReturned = moneyToBeReturned - 1
#     while moneyToBeReturned >= 0.25:
#             quarterNr += 1
#             moneyToBeReturned = moneyToBeReturned - 0.25
#     while moneyToBeReturned >= 0.10:
#             dimeNr += 1
#             moneyToBeReturned = moneyToBeReturned - 0.10
#     while moneyToBeReturned >= 0.05:
#             nickelNr += 1
#             moneyToBeReturned = moneyToBeReturned - 0.05
#     while moneyToBeReturned > 0:
#             penniesNr += 1
#             moneyToBeReturned = moneyToBeReturned - 0.01
#
#     print('You should receive:\n %s of hundreds\n %s of fifties\n %s of twenties\n %s of tens\n %s of fives\n %s of ones\n %s of quarters\n %s of dimes\n %s of nickles\n %s of pennies' % (hundredNr, fiftyNr, twentyNr, tenNr, fifeNr, oneNr,quarterNr,dimeNr, nickelNr, penniesNr))
#
# changeReturner()
#########################################################################################################################
"""Binary to Decimal and Back Converter - 
Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent."""
#########################################################################################################################
def binaryToDecimal():
    binary = input('Wprowadź wartość w postaci binarnej: ')
    binaryValues = list(binary)
    print(binaryValues)
    binIntegers = []
    for i in range(len(binaryValues)):
        binIntegers.append(int(binaryValues[i]))
    print(binIntegers)
    sum = 0
    index = 0
    for i in reversed(binIntegers):
        if i == 1:
            sum = sum + 2**index
        index +=1
    print('Postać dziesietna liczby %s to %s' %(binary,sum))
    print('Postać binarna liczby %s to %s' % (sum, bin(sum)))
binaryToDecimal()
#########################################################################################################################
"""Calculator - A simple calculator to do basic operators. Make it a scientific calculator for added complexity."""
#########################################################################################################################