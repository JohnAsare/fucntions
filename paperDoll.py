# John Asare
# Jun 18 2020

"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii' """


def paper_doll(text):
    reformat = ' '
    for char in text:
        reformat += (char * 3)
    return reformat


print((paper_doll('Hello')))
print(paper_doll('Mississippi'))
