def listFlatten(listInput : list) -> list:
    listFlat = []

    for i in listInput:
        if isinstance(i, list):
            listFlat.extend(listFlatten(i))
        else:
            listFlat.append(i)

    return listFlat



if __name__ == "__main__":
    l = [[1,2],[3,4],[5,[6,7]]]
    x = listFlatten(l)
    print("x:", x)


    assert listFlatten([1,2,3]) == [1,2,3]
    assert listFlatten([[1,2],[3,[4,[5,[6,[7]]]]]]) == [1,2,3,4,5,6,7]
    assert listFlatten([[1,2],[3,[4,[5,[6,[7,71,72],69],58],47],[33,34]]]) == [1,2,3,4,5,6,7,71,72,69,58,47,33,34]
    assert listFlatten([[[[[[[[[[[4]]]]]]]]]]]) == [4]
    assert listFlatten([]) == []

    print("all test cases passed")
