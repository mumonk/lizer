import re

def counter(value, unit):
   #find all non-whitespace
   list = re.findall(value , unit)
   return len(list)

def wordCount(book):
  results = []
  in_file = open(book, "r")
  wordcount = 0
  uwordlist = []
  uwordcount = 0
  for line in in_file:
    wordcount = wordcount + counter("(\S)", line)
    #redl is the line split into a list to iter w/out chars
    redline = line.split()
    for entry in redline:
        uwordlist.append(entry)
  uwordlist = set(uwordlist)
  #count uniq words using length of list
  uwordcount = len(uwordlist)
  return [wordcount, uwordlist]

  return wordcount
  in_file.close()

def uwordcomp(s1, s2):
  #sets 1 and 2 are compared to see words in common
  #great and least are used to prevent length errors in iteration
  if len(s1) > len(s2):
    great = s1
    least = s2
  else:
    great = s2
    least = s1
  #initialize new set for words in common
  common = []
  for word in great:
    word = word.strip()
    if word in least and len(word) > 3:
      common.append(word)
  return(common)

def oneAuthorComparison():
  #Just like two authors, but one
  book1 = input ("Enter name of first file")
  book2 = input ("Enter name of second file")
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
  #commonW gives
  commonW = uwordcomp(uwords1, uwords2)

  print("")
  print(book1, "wordcount:", wC1, "uniqwords:", numUs1)
  print(book1, "the rate of unique word frequency is", (numUs1/wC1) * 100)
  print("")
  print(book2, "wordcount:", wC2, "uniqwords:", numUs2)
  print(book2, "unique word frequency is", (numUs2/wC2) * 100)
  print("")
  print("Unique words in common:", len(commonW))
  print("")

def twoAuthorComparison():
  #This function runs when comparing the works of two authors
  #Enter name of books
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")

  #Enter names of authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  #store total word counts from results
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
  #commonW gives
  commonW = uwordcomp(uwords1, uwords2)

  print("")
  print(author1, "wordcount:", wC1, "uniqwords:", numUs1)
  print(author1, "the rate of unique word frequency is", (numUs1/wC1) * 100)
  print("")
  print(author2, "wordcount:", wC2, "uniqwords:", numUs2)
  print(author2, "unique word frequency is", (numUs2/wC2) * 100)
  print("")
  print("Unique words in common:", len(commonW))
  print("")

def main():
  #main will be used for asking user purpose and then calling for purpose
  print("Lizer is an application intended to analyze .txt files")
  print("")
  print("For self-analysis, enter 1")
  print("For multi-author comparison, enter 2")
  print("Compare with the classics: 3")
  print("")
  #unput is what they type next
  #initializing user input
  unput = eval(input("Choose an option by using the corresponding number: "))
  #making sure they're actually selecting something
  while unput < 1 or unput > 3 or isinstance(unput, float):
    #the input prompt is generalized for less lines
    unput = eval(input("Please choose an option by entering an integer between 1 and 3: "))
  if unput == 1:
    print("Initalizing single-author analysis")
    oneAuthorComparison()
  if unput == 3:
    print("To be honest, I only have 1 and 2 available right now.")
    print("Initializing multi-author comparison")
    print("/n")
    twoAuthorComparison()
main()
