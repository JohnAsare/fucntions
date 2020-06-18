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

    if first_word[0] == last_word[0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print(animal_crackers('John Asare'))
print(animal_crackers('Akosua Asare'))