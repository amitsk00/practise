import threading
from math import sqrt
import time


prime_numbers = []
all_threads = []
number = 10**6
numThreads = 3
startNum = 2


def get_prime_numbers(startNum , endNum):
    # duration = 0
    start = time.time()
    
    if startNum < 2:
        startNum = 2

    for i in range(startNum, endNum):
        for j in range(2, int(sqrt(i))+1 ):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)

    end = time.time() 
    # duration = duration + (end - start)
    duration = (end - start)
    print(f"Time taken: {duration:.4f} seconds ")  # and type is {type(duration)}")

    


def main():

    
    for t in range(numThreads):
        print(t)
        startNum = t * number
        endNum = (t+1) * number
           
        thr1 = threading.Thread(target=get_prime_numbers, args=(startNum, endNum))
        all_threads.append(thr1)
        thr1.start()
        # thr1.join()

        # start = time.time()
        # get_prime_numbers(startNum , endNum)
        # end = time.time() 
        # duration = duration + (end - start)

    for thr2 in all_threads:
        thr2.join()

    
    print(f"Number of prime numbers: {len(prime_numbers)}")



if __name__ == "__main__":
    # print(" started")
    main()
    # print(" ended")