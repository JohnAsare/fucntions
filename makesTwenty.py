# John Asare
# Jun 16 2020


""" MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers
 is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False """


def makes_twenty(n1, n2):
    total = sum((n1, n2))
    print(total)

    if total == (n1 + n2):
      return
    if total or n1 == 20:
        return True
    elif total or n2 == 20:
        return True
    else:
       return False


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))
