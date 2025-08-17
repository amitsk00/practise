# class Solution:
# def plusOne(self, digits: list[int]) -> list[int]:
def plusOne( digits: list[int]) -> list[int]:

    myLen = len(digits)
    new_digits = digits.copy()
    if myLen > 100:
        print("invalid length")
    
    carry_fwd = False
    for i in range(myLen):
        # print("i:", i, "myLen:", myLen)
        iDigit = digits[myLen - i - 1]
        
        if i ==0:
            newDigit = iDigit + 1

        if carry_fwd:
            # newDigit += 1
            newDigit = iDigit + 1

        if newDigit == 10:
            carry_fwd = True
            new_digits[myLen - i - 1] = 0
        else:
            new_digits[myLen - i - 1] = newDigit
            carry_fwd = False
            break

    if carry_fwd:
        new_digits.insert(0, 1)
    
    return new_digits



                


if __name__ == "__main__":
    digits = [1, 2, 3]
    assert plusOne(digits) == [1, 2, 4]

    digits = [1,2,9]
    assert plusOne(digits) == [1, 3, 0] 

    digits = [9,9,9]
    assert plusOne(digits) == [1, 0, 0, 0]

    digits = [0]
    assert plusOne(digits) == [1]

    digits = []
    new_digits = []
    for j in range(4):
        # print("j:", j)
        digits.insert(j, 9)
        new_digits.insert(j, 0)

    new_digits.insert(0,1)
    # print("digits:", digits, "new_digits:", new_digits)
    assert plusOne(digits) == new_digits

    print("All test cases passed!")
