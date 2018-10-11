"""
   Count word frequency.
   CSCI 203 project
   Spring 2017
   Student name(s): Judy Peng, Jean Leong and Sarah Eckermann
"""
from collections import OrderedDict       # ordered dictionary for printing
import operator
import doctest 

# ****PLEASE NOTE: doctests are examples using lincon.txt because the number of
#                  unique words in bush_full.txt and obama_full.txt is too large

def readFileUseful(fileSpeech,fileWords):
    """This function will read the file of all the SOU speeches of a President
        and return a modified list representing all the words in the list.
        Ignoring words that have lenth of less than three.
            Inputs: fileSpeech: (file) a file of the speeches, 
                    fileWords: (file) a file of all the stop words
            Output: (list) a modified list of all lowercase words, no stop
            words or punctuations, in the inputted file. (not sorted)
    doctest:
    >>> readFileUseful('lincon.txt', 'stopwords.txt')
    ['rather', 'us', 'dedicated', 'great', 'task', 'remaining', 'us', 'honored', 'dead', 'take', 'increased', 'devotion', 'cause', 'gave', 'last', 'full', 'measure', 'devotion', 'highly', 'resolve', 'dead', 'shall', 'died', 'vain', 'nation', 'god', 'shall', 'birth', 'freedom', 'government', 'people', 'people', 'people', 'shall', 'perish', 'earth']
    """
    fileSOU = open(fileSpeech,'rt', encoding = 'UTF-8')
    listSOU = fileSOU.read().split()
    fileStop = open(fileWords,'rt', encoding = 'UTF-8')
    listStop = fileStop.read().split()
    i = 0
    while i < len(listSOU):
        listSOU[i] = listSOU[i].lower().strip('-,.:;!?')
        for stopWords in listStop:
            if listSOU[i] == stopWords:
                listSOU.remove(listSOU[i])
                i -= 1
                break
        i += 1
    listSOU = list(filter(None, listSOU))
    return listSOU

def takeOutLenTwo(aList):
    """This function takes alist and return a new list with the elements with
        length less than two being taken off.
        Input: aList (list) the original list
        Output: (list) the new list

        doctest:
    >>> aList = ["cat","doggy","and","at","a","icecream","hi"]
    >>> takeOutLenTwo(aList)
    ['cat', 'doggy', 'and', 'icecream']"""
    i = 0
    while i < len(aList):
        if len(aList[i]) <= 2:
            aList.remove(aList[i])
            i -= 1
        i += 1
    aList= list(filter(None, aList))
    return aList

def createDictionary(aList):
    """This function will first generate a dictionary of the word count of each unique word in aList. 
            Input: aList: (list) the list with all words
            Output: a not-sorted dictionary with the number of words
    doctest:
    >>> aList = ['rather', 'dedicated', 'great', 'task', 'remaining', 'honored', 'dead', 'take', 'increased', 'devotion', 'cause', 'gave', 'last', 'full', 'measure', 'devotion', 'highly', 'resolve', 'dead', 'shall', 'died', 'vain', 'nation', 'god', 'shall', 'birth', 'freedom', 'government', 'people', 'people', 'people', 'shall', 'perish', 'earth']
    >>> createDictionary(aList)
    [('people', 3), ('shall', 3), ('dead', 2), ('devotion', 2), ('birth', 1), ('cause', 1), ('dedicated', 1), ('died', 1), ('earth', 1), ('freedom', 1), ('full', 1), ('gave', 1), ('god', 1), ('government', 1), ('great', 1), ('highly', 1), ('honored', 1), ('increased', 1), ('last', 1), ('measure', 1), ('nation', 1), ('perish', 1), ('rather', 1), ('remaining', 1), ('resolve', 1), ('take', 1), ('task', 1), ('vain', 1)]
    """
    d = {}
    for word in aList:
        if word in d:
           d[word] += 1   # increment the frequency
        else:
           d[word] = 1    # first time
    od = OrderedDict(sorted(d.items()))
    od = sorted(od.items(),key = operator.itemgetter(1),reverse = True)
    return od

def countUnique(dic):
    """This function will count the number of entries in a dictionary.
	Input: dic: (dictionary) a dictionary of words
	Output: the integer number of unique words

    doctest:
    >>> dic = [('people', 3), ('shall', 3), ('dead', 2), ('devotion', 2), ('birth', 1), ('cause', 1), ('dedicated', 1), ('died', 1), ('earth', 1), ('freedom', 1), ('full', 1), ('gave', 1), ('god', 1), ('government', 1), ('great', 1), ('highly', 1), ('honored', 1), ('increased', 1), ('last', 1), ('measure', 1), ('nation', 1), ('perish', 1), ('rather', 1), ('remaining', 1), ('resolve', 1), ('take', 1), ('task', 1), ('vain', 1)]
    >>> countUnique(dic)
    28
    """
    return len(dic)


def createTopDictionary(dic,num):
    """This function will take a dictionary and sort it with the most
        frequently used words at the first entry. If two words have the same
        frequency, then they will follow the alphabetical order in the
        dictionary. Only the first num elements in the dictionary will be sorted
        in that way. After the sorting is done, we are only keeping the top
        Num entries of this dictionary and return the modified dictionary.
	Input: dic: (dictionary) a not sorted dictionary
	          num: (int) the desired top num entries of the dictionary
	Output: A dictionary of the top num words with the count of each
                unique word

    doctest:
    >>> dic = [('people', 3), ('shall', 3), ('dead', 2), ('devotion', 2), ('birth', 1), ('cause', 1), ('dedicated', 1), ('died', 1), ('earth', 1), ('freedom', 1), ('full', 1), ('gave', 1), ('god', 1), ('government', 1), ('great', 1), ('highly', 1), ('honored', 1), ('increased', 1), ('last', 1), ('measure', 1), ('nation', 1), ('perish', 1), ('rather', 1), ('remaining', 1), ('resolve', 1), ('take', 1), ('task', 1), ('vain', 1)]
    >>> createTopDictionary(dic,10)
    [('people', 3), ('shall', 3), ('dead', 2), ('devotion', 2), ('birth', 1), ('cause', 1), ('dedicated', 1), ('died', 1), ('earth', 1), ('freedom', 1)]
    """
    newDic = dic[0:num]
    return newDic

def printDictionary(d):
    """This function will print the dictionary
	Input: dic: a collection of the word count of each unique word

    doctest:
    >>> d = [('people', 3), ('shall', 3), ('dead', 2), ('devotion', 2), ('birth', 1), ('cause', 1), ('dedicated', 1), ('died', 1), ('earth', 1), ('freedom', 1)]
    >>> printDictionary(d)
     1.      people   3
     2.       shall   3
     3.        dead   2
     4.    devotion   2
     5.       birth   1
     6.       cause   1
     7.   dedicated   1
     8.        died   1
     9.       earth   1
    10.     freedom   1
    """
    keys = []
    values = []
    for k,v in d:
        keys += [k]
        values += [v]
    i = 1
    while i <= len(d):
        print('{:>4} {:>10} {:>3}'.format((str(i) + ". "),keys[i-1],values[i-1]))
        i += 1
def mainHelperPartTwo():
    """This function is designed for visualizeText.py to get the information
        from this part without reading the disk again
        output: ndB, a new dictionary with the top 20 words of Bush'd speech 
                ndO, a new dictionary with the top 20 words of Obama's speech
                listPart3Bush, a list of words of Bush's file
                listPart3Obama, a list of words of Obama's file
    """ 
    fileSpeechB = "bush_all.txt"
    fileSpeechO = "obama_all.txt"
    fileWords = "stopwords.txt"
    listPart3Bush = readFileUseful(fileSpeechB,fileWords)
    listPart1Bush = takeOutLenTwo(listPart3Bush)
    listPart3Obama = readFileUseful(fileSpeechO,fileWords)
    listPart1Obama = takeOutLenTwo(listPart3Obama)
    dB = createDictionary(listPart1Bush)
    ndB = createTopDictionary(dB,20)
    
    dO = createDictionary(listPart1Obama)
    ndO = createTopDictionary(dO,20)

    return ndB,ndO,listPart3Bush,listPart3Obama

def main():
    ''' The main function prints out the number of unique words count and prints
        the top 20 frequently used words and their count
    '''
    while True:
        choice = input("Which file would you like to analyze? Bush's or Obama's (type 'bush_all.txt' or 'obama_all.txt'.)?  ")
        while choice != "bush_all.txt" and choice != "obama_all.txt":
            choice = input("Please enter 'bush_all.txt' or 'obama_all.txt: ")
        fileSpeech = choice
        fileWords = "stopwords.txt"
        listPart3 = readFileUseful(fileSpeech,fileWords)
        listPart1 = takeOutLenTwo(listPart3)
        d = createDictionary(listPart1)
        print()
        print("Running analysis for \"" + fileSpeech + "\"")
        print("\nUnique words count: ", countUnique(d))
        print("Top 20 frequently used words and their count: ")
        nd = createTopDictionary(d,20)
        printDictionary(nd)
        print()
        ifExit = input("Do you want to do another analysis (type \"n\" to quit)? ")
        if ifExit == "n":
            break
        
        print()
    print("Bye!")


import doctest
doctest.testmod()
main()
