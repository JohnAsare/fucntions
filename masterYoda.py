# John Asare
# Jun 17 2020


"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We' """


def master_yoda(text):
    splt = text.split()
    return ' '.join(splt[::-1])


print((master_yoda('I am home')))
print(master_yoda('We are ready'))
print(master_yoda('John Asare is going to school'))