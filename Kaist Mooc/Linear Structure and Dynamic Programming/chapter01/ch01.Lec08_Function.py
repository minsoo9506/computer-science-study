# Function statement
# 여러개 값 return 가능


def add(a, b):
    return a+b


addvar = add(10, 3)


def mul(a, b):
    return a*2, b*3


mulvar1, mulvar2 = mul(10, 3)

# Finding prime number


def isPrimeNumber(num1):
    for i in range(2, num1):
        if num1 % i == 0:
            break
    else:
        return True
    return False


def findPrime(num1, num2):
    numCount = 1
    for i in range(num1, num2):
        if isPrimeNumber(i) == True:
            print(numCount, 'th prime :', i)
            numCount = numCount + 1


findPrime(1, 10)
