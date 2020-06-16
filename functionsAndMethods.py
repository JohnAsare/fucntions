# John Asare
# Jun 15 2020


"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are
even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5 """


def lesser_of_two_evens(a, b):
    if a and b % 2 == 0:
        if a < b:
            return a
        else:
            return b

    elif a or b % 2 != 0:
        if a < b:
            return b
        else:
            return a


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(4, 7))

