addTurns = {
    0: [8],
    1: [7],
    2: [],
    3: [9],
    4: [],
    5: [6, 9],
    6: [8],
    7: [],
    8: [],
    9: [8],
    "+": [],
    "-": ["+"],
    "=": []
}
removeTurns = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [5],
    7: [1],
    8: [0, 6, 9],
    9: [3, 5],
    "+": ["-"],
    "-": [],
    "=": []
}

replaceTurns = {
    0: [9],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [9],
    7: [],
    8: [],
    9: [0, 6],
    "+": [],
    "-": [],
    "=": []
}


def splitInput(equality):
    parsed = []
    currency = ""
    for i in range(len(equality)):
        if equality[i] != "+" and equality[i] != "-" and equality[i] != "=":
            currency += equality[i]
        else:
            parsed.append(int(currency))
            parsed.append(equality[i])
            currency = ""
    parsed.append(int(currency))
    return parsed


def printAnswer(array):
    print(*array, sep="")


def checkEquality(arr_equality):
    curr = ""
    i = 0
    while arr_equality[i] != "=":
        curr += str(arr_equality[i])
        i += 1
    return eval(curr) == arr_equality[len(arr_equality) - 1]


arr = splitInput([char for char in input()])

if checkEquality(arr):
    print("Equality is correct.")

else:
    for i in range(0, len(arr), 2):
        current_arr_for_check = arr.copy()
        elementToReplace = arr[i]
        possibleReplaces = replaceTurns[elementToReplace]

        for j in range(len(possibleReplaces)):
            current_arr_for_check[i] = possibleReplaces[j]
            if checkEquality(current_arr_for_check):
                printAnswer(current_arr_for_check)

    for i in range(len(arr)):
        current_arr_for_check = arr.copy()
        element_start = arr[i]
        possibleTakes = removeTurns[element_start]

        for j in range(len(possibleTakes)):
            TakenArr = current_arr_for_check.copy()
            TakenArr[i] = possibleTakes[j]

            for k in range(len(arr)):
                if i != k:
                    element_finish = arr[k]
                    possibleGivings = addTurns[element_finish]

                    for l in range(len(possibleGivings)):
                        ReadyArr = TakenArr.copy()
                        ReadyArr[k] = possibleGivings[l]
                        if checkEquality(ReadyArr):
                            printAnswer(ReadyArr)
