# John Asare
# Jun 18 2020


""" SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a
6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14 """


def summer_69(arr):
    keep = []
    move_on = True

    for number in arr:
        while move_on:
            if number != 6:
                keep.append(number)
                break
            else:
                move_on = False

        while not move_on:
            if number != 9:
                break
            else:
                move_on = True
                break
    return sum(keep)

#print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
#print(summer_69([2, 1, 6, 9, 11]))
