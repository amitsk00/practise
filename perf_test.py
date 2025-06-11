from time import time



all_primes = []

def func3(numMax):
    i = numMax
    isPrime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            isPrime = False
            break

    return isPrime

def func3(numMax):
    i = numMax
    isPrime = True
    for j in range(2, int(i /2) + 1):
        if i % j == 0:
            isPrime = False
            break

    return isPrime


def func1(numMax):
    i = numMax
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break

    return isPrime


def main():

    numMax = 10**7
    numMax = numMax + 3

    start = time()
    flag = func1(numMax)
    end = time()
    duration = end - start 
    print(f"Time taken: {duration:.8f} seconds  and {numMax} prime is {flag}")   

    start = time()
    flag = func3(numMax)
    end = time()
    duration = end - start 
    print(f"Time taken: {duration:.8f} seconds  and {numMax} prime is {flag}")   
        
    start = time()
    flag = func3(numMax)
    end = time()
    duration = end - start 
    print(f"Time taken: {duration:.8f} seconds  and {numMax} prime is {flag}")   


if __name__ == "__main__":
    main()