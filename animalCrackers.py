# John Asare
# Jun 16 2020


""" ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with
same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False """


def animal_crackers(text):
    last_char = -1

    if text[0] != text[last_char]:
        last_char -= 1

    elif text[0] == text[last_char]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))
#print(animal_crackers('Crazy Kangaroo'))