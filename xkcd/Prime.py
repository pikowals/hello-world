def primeFactor():
    print('Wprowadz liczbe ')
    nPrime = input()
    for i in range(1,int(nPrime)+1):
        divNum = 0
        n = (int(nPrime)%i)
        if n == 0 and i>1:
            for j in range(1,i+1):
                if i%j == 0:
                    divNum = divNum +1
            if divNum <= 2:
                print('%s jest liczbą pierwszą ' % i)
primeFactor()