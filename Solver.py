import keyboard

import Data

addTurns = Data.addTurns
removeTurns = Data.removeTurns
replaceTurns = Data.replaceTurns
arithmetic = Data.arithmetic


def splitInput(equality):
    parsed = []
    currency = ""
    for i in range(len(equality)):
        if equality[i] not in arithmetic:
            currency += equality[i]
        else:
            parsed.append(int(currency))
            parsed.append(equality[i])
            currency = ""
    parsed.append(int(currency))
    return parsed


def listtonumber(my_list):
    c = 0
    dic = 0
    for i in range(len(my_list) - 1, -1, -1):
        c += my_list[i] * 10 ** dic
        dic += 1
    return c


def printAnswer(array):
    print(*array, sep="")


def checkEquality(arr_equality):
    curr = ""
    i = 0
    while arr_equality[i] != "=":
        curr += str(arr_equality[i])
        i += 1
    return eval(curr) == arr_equality[len(arr_equality) - 1]


def changeInOne(number):
    answer = []
    number_arr = [int(char) for char in str(number)]
    for i in range(len(number_arr)):
        start = number_arr[i]
        start_without = removeTurns[start]

        for j in range(len(start_without)):
            localarr = number_arr.copy()
            localarr[i] = start_without[j]

            for k in range(len(localarr)):
                if i != k:
                    finish = localarr[k]
                    finish_with = addTurns[finish]
                    for l in range(len(finish_with)):
                        superarr = localarr.copy()
                        superarr[k] = finish_with[l]
                        answer.append(listtonumber(superarr))

    return answer


def solve(arr):
    for i in range(0, len(arr), 2):
        current_arr_for_check = arr.copy()
        elementToReplace = arr[i]

        for local in range(len(str(elementToReplace))):
            possibleReplaces = replaceTurns[int(str(elementToReplace)[local])]

            for j in range(len(possibleReplaces)):
                currentnumber = [int(char) for char in str(elementToReplace)]
                currentnumber[local] = possibleReplaces[j]
                current_arr_for_check[i] = currentnumber

                for local_2 in range(len(current_arr_for_check)):
                    if isinstance(current_arr_for_check[local_2], list):
                        current_arr_for_check[local_2] = listtonumber(current_arr_for_check[local_2])

                if checkEquality(current_arr_for_check):
                    return current_arr_for_check

    for i in range(len(arr)):
        current_arr_for_check = arr.copy()
        element_start = arr[i]

        for local in range(len(str(element_start))):
            if element_start not in arithmetic:
                possibleTakes = removeTurns[int(str(element_start)[local])]
            else:
                possibleTakes = removeTurns[element_start]

            for j in range(len(possibleTakes)):
                TakenArr = current_arr_for_check.copy()

                if element_start not in arithmetic:
                    currentnumber = [int(char) for char in str(element_start)]
                    currentnumber[local] = possibleTakes[j]
                    TakenArr[i] = currentnumber
                else:
                    TakenArr[i] = possibleTakes[j]

                for local_2 in range(len(TakenArr)):
                    if isinstance(TakenArr[local_2], list):
                        TakenArr[local_2] = listtonumber(TakenArr[local_2])

                for k in range(len(arr)):
                    if i != k:
                        element_finish = arr[k]

                        for local_777 in range(len(str(element_finish))):
                            if element_finish not in arithmetic:
                                possibleGivings = addTurns[int(str(element_finish)[local_777])]
                            else:
                                possibleGivings = addTurns[element_finish]

                            for l in range(len(possibleGivings)):
                                ReadyArr = TakenArr.copy()

                                if element_finish not in arithmetic:
                                    currentnumber = [int(char) for char in str(element_finish)]
                                    currentnumber[local_777] = possibleGivings[l]
                                    ReadyArr[k] = currentnumber
                                else:
                                    ReadyArr[k] = possibleGivings[l]

                                for local_222 in range(len(ReadyArr)):

                                    if isinstance(ReadyArr[local_222], list):
                                        ReadyArr[local_222] = listtonumber(ReadyArr[local_222])
                                if checkEquality(ReadyArr):
                                    return ReadyArr
                    else:
                        if arr[i] not in arithmetic:
                            localcopy = arr.copy()
                            sus = changeInOne(localcopy[i])
                            for klmn in range(len(sus)):
                                localcopy[i] = sus[klmn]
                                if checkEquality(localcopy):
                                    return localcopy
    return False


arr = splitInput([char for char in input("Enter your equality:\n")])

if checkEquality(arr):
    print("Equality is correct.\n")
else:
    x = solve(arr)
    if x:
        printAnswer(x)
        print("\n")
    else:
        print("No answer.\n")

print("Press any key to exit...")
keyboard.read_key()
