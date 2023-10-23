def questions():
    myList = [ 1, 2, 3, 4]
    anotherList = [[1, 2, 3, 4], [5, 8, 7, 9]]
    myNames = [ "Beth", "Dorcas"]

    # for num in myList:
    #     print(num)

    for row in range(len(anotherList)):
        for column in range(len(anotherList[row])):
            print(anotherList[row][column])
            # print(row[column])

questions()
