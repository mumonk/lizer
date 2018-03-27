import os,sys
from tkinter import filedialog
from tkinter import *
import collections
import re
import string
import random
import statistics as stat
from collections import Counter
import pickle
import csv

def getLengthStats(thisCounter):
    #count length of words in counter and return descriptors
    pairs = thisCounter.items()
    lengths = []
    for word in pairs:
        lengths.append(len(word[0]))
    averaged = sum(lengths) / len(lengths)
    wordLengths = Counter(lengths)
    mostCommon = wordLengths.most_common(5)
    leastCommon = wordLengths.most_common()[:-5:-1]
    return [round(averaged, 2), mostCommon, leastCommon]
    
'''    
def copypasta (pastedText):
  ignoredFile = open('IgnoredWords.txt', 'r', encoding="utf-8")
  ignoredWords = set()
  for line in ignoredFile:
    ignoredWords.add(line.strip())
  ignoredFile.close()
  rmPunc = str.maketrans('', '', string.punctuation)
  wordcount = 0
  uWordList = []
  dividedLine = pastedText.split()
  wordcount = len(dividedLine)
  #redl is the line split into a list to iterate through, ignoring spare characters
  for entry in dividedLine:
    #standardize words and remove punctuation
    entry = entry.lower()
    entry = entry.translate(rmPunc)
    entry.strip()
    if entry not in ignoredWords:
      uWordList.append(entry)
  ignoredFile.close()
  return [wordcount, Counter(uWordList)]
'''  
def wordCount(book):
  #opening the target file and the various words that ought not be counted as unique
  in_file = open(book, "r", encoding="utf-8")
  ignoredFile = open('IgnoredWords.txt', 'r', encoding="utf-8")
  #creating a set of words to be ignored
  ignoredWords = set()
  for line in ignoredFile:
    ignoredWords.add(line.strip())

  #rmPunc will remove puncutation from strings
  rmPunc = str.maketrans('', '', string.punctuation)
  wordcount = 0
  uWordList = []
  for line in in_file:
    #words are counted by the number of whitespaces in each line
    dividedLine = line.split()
    wordcount = wordcount + len(dividedLine)
    #redl is the line split into a list to iterate through, ignoring spare characters
    for entry in dividedLine:
        #standardize words and remove punctuation
        entry = entry.lower()
        entry = entry.translate(rmPunc)
        entry.strip()
        if entry not in ignoredWords:
            uWordList.append(entry)
  #a Counter is a dict that tallies the frequency of set items in a list
  uWordSet = Counter(uWordList)
  in_file.close()
  ignoredFile.close()
  return [wordcount, uWordSet]



root = Tk()
def wordCount(book):
  #opening the target file and the various words that ought not be counted as unique
  in_file = open(book, "r", encoding="utf-8")
  ignoredFile = open('IgnoredWords.txt', 'r', encoding="utf-8")
  #creating a set of words to be ignored
  ignoredWords = set()
  for line in ignoredFile:
    ignoredWords.add(line.strip())

  #rmPunc will remove puncutation from strings
  rmPunc = str.maketrans('', '', string.punctuation)
  wordcount = 0
  uWordList = []
  for line in in_file:
    #words are counted by the number of whitespaces in each line
    dividedLine = line.split()
    wordcount = wordcount + len(dividedLine)
    #redl is the line split into a list to iterate through, ignoring spare characters
    for entry in dividedLine:
        #standardize words and remove punctuation
        entry = entry.lower()
        entry = entry.translate(rmPunc)
        entry.strip()
        if entry not in ignoredWords:
            uWordList.append(entry)
  #a Counter is a dict that tallies the frequency of set items in a list
  uWordSet = Counter(uWordList)
  in_file.close()
  ignoredFile.close()
  return [wordcount, uWordSet]

def workIt():
  results =  [file, wordCount(file)]
  b1Length = getLengthStats(results[1][1])
  wC1 = results[1][0]
  numUs1 = len(results[1][1])
  book = results[0]
  print("")
  print(book, "Word Count:", wC1, "Unique Words:", numUs1)
  print(book, "The percentage of words that are unique:", (round((numUs1/wC1), 4) * 100), '%')
  for pair in results[1][1].most_common(20):
        print(pair[0], ":", pair[1])
  print("Average Word Length:", b1Length[0],"\nMost Common Lengths:", b1Length[1], "\nLeast Common Lengths:", b1Length[2])
  
root.title("Lizer Text Analysis")
file = filedialog.askopenfilename(parent=root, title='Choose a file', initialdir = os.getcwd())
if file != None:
    print(file)
    
title = Label(root, text="Select Text for Analysis", fg="white", bg="black")
one = Label(root, text="File: ")
two = Label(root, text=file, bg="white", fg="black")

title.grid(row=0, sticky=N, columnspan=2)
one.grid(row=1, column=0)
two.grid(row=1, column=1)    

c = Button(root, text="Analyze text file")
c.grid(columnspan=2)
c.bind('<Button-1>', workIt())
    
root.mainloop()