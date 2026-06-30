

def checkForValid(pattern):

    if len(pattern) % 2 == 1:
        return False
    
    isValid = True
    
    listBracketsOpening = ['(', '{', '[' ]
    listBracketsClosing = [')', '}', ']' ]
    listBrackets = listBracketsOpening + listBracketsClosing
    stack = []
    
    # print(listBrackets)

    for i in pattern:
        # print(i)
        if not i in listBrackets:
            print("non bracket char")
            continue
        else:
            if i in listBracketsOpening:
                stack.append(i)
            else:
                if not stack:
                    return False
                
                currOpenBracket = stack.pop()

                # print(f"{currOpenBracket} - {i}")
                if listBracketsOpening.index(currOpenBracket) == listBracketsClosing.index(i):
                    continue
                else:
                    return False
                
    if stack:
        return False
    else:
        return True




if __name__ == "__main__":

    pattern = "{{{(}}})"

    flagBrackets = checkForValid(pattern)
    if flagBrackets:
        print("valid")
    else:
        print("Invalid")



    print("--------------------------------------------------------------")
    print("running test cases")

    assert checkForValid("(([]){})[]" ) == True
    assert checkForValid("[{()}([])]" ) == True
    assert checkForValid("({[()][]})" ) == True
    assert checkForValid("(((()))){}[]" ) == True
    assert checkForValid("{{[[(())]]}}" ) == True



    assert checkForValid("(([]){})[}" ) ==False
    assert checkForValid("([{}]))(([]" ) == False
    assert checkForValid("((({[[]]}}))" ) == False
    assert checkForValid("[{()}([]))(" ) == False
    assert checkForValid("({[]({[]}))" ) == False

    print("All test cases passed")
    
