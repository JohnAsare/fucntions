# John Asare
# Jun 16 2020


""" ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with
same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False """


def animal_crackers(text):
    separate_text = text.split()

    for letter in range(len(separate_text[0])):
        return letter

print(animal_crackers('Levelheaded Llama'))
#print(animal_crackers('Crazy Kangaroo'))