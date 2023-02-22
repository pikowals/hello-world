def FibSeq():
    a = 0
    b = 1
    print('Wprowadz ile liczb fibonacciego chcesz otrzymac: ')
    nfib = input()
    print(a, end=' ')
    print(b, end=' ')
    for i in range(int(nfib)):
        c = a + b
        a = b
        b = c
        print(c, end=' ')
FibSeq()