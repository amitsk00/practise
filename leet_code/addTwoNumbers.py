def addTwoNumbers(l1 , l2):
    listOutput = []

    # print(l11)
    # print(l11.reverse())
    # l1 = l11.reverse()
    # l2 = l22.reverse()

    l1.reverse()
    l2.reverse()
    
    lenL1 = len(l1)
    lenL2 = len(l2)
    carry = 0

    if lenL1 >= lenL2:
        maxLen = lenL1
    else:
        maxLen = lenL2

    for i in range(maxLen):
        
        if i <= lenL1 -1: 
            d1 = l1[i] 
        else:
            d1 = 0 

        if i <= lenL2 - 1:
            d2 = l2[i]  
        else:
            d2 = 0 
        dAnswer = d1 + d2 + carry
        # print(f"{i} - {dAnswer}")

        if dAnswer > 9:
            listOutput.append(dAnswer % 10)
            carry = dAnswer // 10 
        else:
            listOutput.append(dAnswer)
            carry = 0

    listOutput.reverse()
    if carry:
        listOutput.insert(0,carry)

        

    
    


    return listOutput



if __name__ == "__main__":
    l1 = [1,2,3,9]
    l2 = [9,9,4,5]
    print(l1)
    print(l2)
    l3 = addTwoNumbers(l1,l2)
    print("==============")
    print(l3)