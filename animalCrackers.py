# John Asare
# Jun 16 2020


""" ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with
same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False """


def animal_crackers(text):
    separate_text = text.split()
    first_word = separate_text[0]
    last_word = separate_text[1]


    for letter in first_word:
        for x_letter in last_word:
            if letter == x_letter:
                return True
            else:
                return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))