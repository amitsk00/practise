import re 

def countFreq(line: str) -> dict :
     
    dictFreq = {}
    # tmpList = line.split(" ")
    tmpList = re.split(r'[,.;:\s]+', line)

    for item in tmpList:
        # print(item)
        if item in dictFreq.keys():
            dictFreq[item] = dictFreq[item] + 1
        else:
            dictFreq[item] = 1


    return dictFreq 


if __name__ == "__main__":
    line = "my name is anthony my ist gon gon "
    line = "abcdjwyfwrnvfjnvjfhvjf"
    line = ""
    line = "a a a a b b b c c d"
    dict1 = countFreq(line)
    print(dict1)
