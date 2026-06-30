
def fib(num : int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    
    nth_term = 0
    nth_term =  fib(num - 1)  + fib(num - 2)
    return nth_term


def factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


if __name__ == "__main__":


    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1

    assert fib(8) == 21
    assert fib(10) == 55
    assert fib(11) == 89

    print("All tests passed for fibonacci !")

    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24   

    print("All tests passed for factorial !")       

