# John Asare
# Jun 18 2020


""" Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False """


def has_33(nums):
    for number in nums:
        if number == 3:
            found = [number]
            if found == 33:
                return True
        else:
            return False
        print(found)


#has_33([1, 3, 3])
print((has_33([1, 3, 1, 3])))
#has_33([3, 1, 3])
