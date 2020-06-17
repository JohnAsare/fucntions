# John Asare
# Jun 16 2020


""" OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald """


def old_macdonald(name):
    upper_first = name[0].capitalize()
    middle = name[1:3]
    upper_fourth = name[3].capitalize()
    rest = name[4:]

    return upper_first + middle + upper_fourth + rest


print(old_macdonald('macdonald'))