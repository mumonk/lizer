#"C:\ProgramData\Anaconda3
# coding: utf8
import re
import string
import random
import os, sys
from collections import Counter

def inRange(item, range):
    #function takes a given input and checks if is a number within an implicit range
    #range is specified depending on menu
    try:
        tryItem = int(item)
    except ValueError:
        return False
        
    if tryItem < 1 or tryItem > range:
        return False
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


def uwordcomp(s1, s2):
  getLengthStats(s1)
  getLengthStats(s2)
  #sets 1 and 2 are compared to see words in common
  #great and least are used to prevent length errors in iteration
  if len(s1) > len(s2):
    great = s1
    least = s2
  else:
    great = s2
    least = s1
  #a Counter object can be broken into pairs
  greatestPairs = great.items()
  leastWords = set(least)
  sharedWords = []
  #I take a pair from Greatest and check if it is in Least. If so, it gets kept.
  for freqPair in greatestPairs:
    if freqPair[0] in leastWords:
        sharedWords.append(freqPair)
  #convert the list of pairs into a dict and then add to the least
  dict(sharedWords)
  return(Counter(dict(sharedWords)))
def classicsComparison():
    #listing all .txt. in the classics directory
    currentFolder = os.getcwd()
    currentFilenames = []
    counter = 1
    print("Plaintext files in project folder:")
    for alphaFile in os.listdir(currentFolder):
        if alphaFile[-4:] == '.txt' and alphaFile!= 'IgnoredWords.txt':
            currentFilenames.append(alphaFile)
            print(str(counter) + '. ' + alphaFile)
            counter += 1
    #listing all .txt in the Classics directory
    
    classicsFolder = currentFolder + "/Classics"
    print("\n----------")
    print("A selection of classic writings from the Public Domain:")
    for betaFile in os.listdir(classicsFolder):
        if betaFile[-4:] == ".txt":
            currentFilenames.append(betaFile)
            print(str(counter) + '. ' + betaFile)
            counter += 1
    titleOne = input("Enter the number of the first file to analyze: ")
    while inRange(titleOne, len(currentFilenames)) is False:
        titleOne = input("Choose an option by using the corresponding whole number: ")
    #subtraction to fit it to a zero index.
    titleOne = int(titleOne) - 1
    
    titleTwo = input("Enter the number of the second file to analyze: ")
    while inRange(titleTwo, len(currentFilenames)) is False:
        titleTwo = input("Choose an option by using the corresponding whole number: ")
    
    titleTwo = int(titleTwo) - 1
    book1 = currentFilenames[titleOne]
    book2 = currentFilenames[titleTwo]
    #determine whether to path the classics folder
    package_dir = os.path.dirname(os.path.abspath(__file__))
    
    if len(currentFilenames) > 6:
        #minus seven to re-index to zero
        if titleOne <= len(currentFilenames) - 6:
            book1 =  '/Classics/' + currentFilenames[titleOne]
        if titleTwo <= len(currentFilenames) - 6:
            book2 = '/Classics/' + currentFilenames[titleTwo]
            
    else:
        book1 =  'Classics/' + currentFilenames[titleOne]
        book2 = 'Classics/' + currentFilenames[titleTwo]
    #store word counts of files
    res1 = wordCount(book1)
    res2 = wordCount(book2)
    wC1 = res1[0]
    wC2 = res2[0]
    #store all unique words
    uwords1 = res1[1]
    uwords2 = res2[1]
    #get len of unique words
    numUs1 = len(uwords1)
    numUs2 = len(uwords2)
    #commonW is a Counter object
    commonW = uwordcomp(uwords1, uwords2)
    b1Length = getLengthStats(uwords1)
    b2Length = getLengthStats(uwords2)
    print("")
    print(book1, "Word Count:", wC1, "Unique Words:", numUs1)
    print(book1, "The percentage of words that are unique:", (round((numUs1/wC1), 4) * 100))
    print("Average Word Length:", b1Length[0],"\nMost Common Lengths:", b1Length[1], "\nLeast Common Lengths:", b1Length[2])
    print("--")
    print(book2, "Word Count:", wC2, "Unique Words:", numUs2)
    print(book2, "The percentage of words that are unique:", (round((numUs2/wC2), 4) * 100))
    print("Average Word Length:", b2Length[0],"\nMost Common Lengths:", b2Length[1], "\nLeast Common Lengths:", b2Length[2])
    print("--")
    print("Unique words in common:", len(commonW))
    print("Top 20 Shared Words:")
    for pair in commonW.most_common(20):
        print(pair[0], ":", pair[1])
    print("--")

def main():
  #main calls specific functions, as defined by the user
  print("Lizer is an application intended to analyze .txt files")
  print("")
  print("Place your files in the folder you are running Lizer from, or use some of the classics provided.")
  print("")
  classicsComparison()
main()
