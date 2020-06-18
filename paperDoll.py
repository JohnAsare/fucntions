# John Asare
# Jun 18 2020

"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii' """


def paper_doll(text):
    for char in text:
        print(char * 3)

print((paper_doll('Hello')))
paper_doll('Mississippi')