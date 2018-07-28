# Program to analysis a book.
# The basic idea is to see how the writing has evolved over time

# author: Amin Ahmadi
# date: July 27, 2018
########################################
import string
import matplotlib.pyplot as pl
import numpy as np
import os

########################################
def word_histogram(file_name):
    """ read a txt file and count number of occurance of words. 
    Each word and number of occurance are stored into a dic
    """
    fin = open(file_name)
    print('========================================')
    lines = fin.readlines()
    print(' Number of lines in this file: ', len(lines))
    print('Preparing the file for analysis ...')
    hist = dict()               # empty dic to store num of words

    for line in lines:
        # split the line into words
        line = line.replace('-', ' ')
        for word in line.split():
            # get rid of white space and punctuation
            word = word.strip(string.whitespace + string.punctuation)
            word = word.lower()
            hist[word] = hist.get(word,0) + 1
    print('Number of unique words: ', len(hist))
    return hist
########################################
def most_common(hist):
    """ find most common words with number of occurance 
    and sort them"""
    t = []
    for key, value in hist.items():
        t.append((value,key))
    t.sort(reverse=True)
    return t
########################################
def total_num_words(hist):
    tot = 0
    for n_val in hist.values():
        tot += n_val
    print(tot)
    return tot

########################################
###             Main Code           ####
########################################
os.chdir('./Bram_Stoker/')
for file_in_dir in os.listdir():
    hist = word_histogram(file_in_dir)
    t = most_common(hist)
    total_num_words(hist)

# file_name = 'TheLadyoftheShroud.txt'
# hist = word_histogram(file_name)
# t = most_common(hist)

# file_name = 'TheJewelofSevenStars.txt'
# hist = word_histogram(file_name)
# t = most_common(hist)

# file_name = 'TheLairoftheWhiteWorm.txt'
# hist = word_histogram(file_name)
# t = most_common(hist)

########################################
###            Plotting              ###
########################################

word_arr = np.zeros((len(t)), dtype=int)
indx = np.ones((word_arr.shape[0]), dtype = int)

for i in range(len(t)):
    word_arr[i] = t[i][0]

for i in range(len(word_arr)):
    indx[i] = i
    

pl.bar(indx[:20], word_arr[:20], width=0.4)
pl.show()
########################################
###        Who is author             ###
########################################

# Learn a model to distinguish the author based on
# the passage (short) that is provided.

# In a simple way it can be done just looking at the
#  vocaburaly that has been used in the passage.

# In the second trial it would be nice to add a Markovian
# algorithm to learn the structure. Then the algorithm must
# be able to determine the author using a short passage.
