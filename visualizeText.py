"""
   Visualize data using Matplotlib.
   CSCI 203 project
   Spring 2017
   Student name(s):Judy Peng, Jean Leong and Sarah Eckermann
"""
import numpy as np
import matplotlib.pyplot as plt
import collections
import operator 
from countWords import *

#This sortDictionary function replaces the functions sortForObama and
#sortForBush. We changed this because we didn't realize that we can return 2
#things in the same function. 
def sortDictionary(dBush, dObama):
    '''sortDictionary sorts the dictionary in the
    order specific to the stack step (unfilled) graph we designed to draw. As we
    specified in the overview, Obama will be on the left of the graph, so we will
    find the list of words that are in both dBush and dObama, sort them in frequency
    in Obama’s speeches first and then in alphabetical order. Finally, we take out
    the entries that have common words in both dictionaries in dObama, and append
    those entries at the end of the remaining ones in dObama. Then we return the
    new sorted dictionary.We are going to do the same for the top twenty dictionary of Bush.
    After we have taken out the entries of common top-20 words in Bush’s dictionary,
    sorted them, we are going to reverse the order of the remaining ones in dBush,
    and put the common entries before the revered remaining entries in dBush.
    Then we will return the new sorted dictionary for Bush.
    Input: dBush: (dictionary) the top 20 words dictionary of Bush
	          dObama: (dictionary) the top 20 words dictionary of Obama
    Output: a sorted dictionary for Obama (dObama) and Bush (dBush)

    doctest:
    >>> fileSpeech = "bush_all.txt"
    >>> fileWords = "stopwords.txt"
    >>> dB = createDictionary(readFileUseful(fileSpeech,fileWords))
    >>> ndB = createTopDictionary(dB,20)
    >>> fileSpeech = "obama_all.txt"
    >>> dO = createDictionary(readFileUseful(fileSpeech,fileWords))
    >>> ndO = createTopDictionary(dO,20)
    >>> ndB
    [('america', 209), ('people', 159), ('us', 123), ('world', 119), ('country', 110), ('security', 110), ('congress', 102), ('american', 99), ('help', 96), ('americans', 93), ('nation', 92), ('government', 88), ('health', 83), ('years', 83), ('iraq', 81), ('make', 81), ('freedom', 75), ('good', 73), ('work', 73), ('tax', 72)]
    >>> dBush = [('america', 217), ('people', 147), ('security', 108), ('world', 106), ('congress', 104), ('help', 103), ('country', 100), ('american', 98), ('health', 92), ('americans', 90), ('nation', 87), ('iraq', 85), ('government', 81), ('make', 81), ('years', 80), ('freedom', 78), ('children', 76), ('tax', 75), ('terrorists', 75), ('work', 75)]
    >>> dObama = ndO
    >>> sortDictionary(dBush,dObama)
    (OrderedDict([('right', 110), ('economy', 114), ('like', 116), ('just', 116), ('need', 120), ('time', 123), ('know', 123), ('jobs', 178), ('us', 183), ('america', 202), ('people', 195), ('world', 106), ('congress', 99), ('help', 98), ('country', 114), ('american', 175), ('americans', 141), ('make', 151), ('years', 161), ('work', 155), ('security', 0), ('health', 0), ('nation', 0), ('iraq', 0), ('government', 0), ('freedom', 0), ('children', 0), ('tax', 0), ('terrorists', 0)]), OrderedDict([('right', 0), ('economy', 0), ('like', 0), ('just', 0), ('need', 0), ('time', 0), ('know', 0), ('jobs', 0), ('us', 0), ('america', 217), ('people', 147), ('world', 106), ('congress', 104), ('help', 103), ('country', 100), ('american', 98), ('americans', 90), ('make', 81), ('years', 80), ('work', 75), ('security', 108), ('health', 92), ('nation', 87), ('iraq', 85), ('government', 81), ('freedom', 78), ('children', 76), ('tax', 75), ('terrorists', 75)]))
    '''
    dObama = OrderedDict(reversed(dObama))
    dBush = OrderedDict(dBush)
    dCommonBush = OrderedDict()
    dCommonObama = OrderedDict()
    dBushNoObama = OrderedDict()
    dObamaNoBush = OrderedDict()
    #print ("before we do anything:\n")
    #print(dObama)
    #print(dBush)
    for k, v in dBush.items():
        for k2, v2 in dObama.items(): 
            if k == k2:
                dCommonBush.update(OrderedDict({k: v}))
                dCommonObama.update(OrderedDict({k2: v2}))
    #print ("things they have in common:\n")
    #print(dCommonBush)
    #print(dCommonObama)
    for k in dCommonBush:
        del dBush[k]
        del dObama[k]
    #print ("after removing:\n")
    #print(dBush)
    #print(dObama)
    for k,v in dBush.items():
        dBushNoObama.update(OrderedDict({k: 0}))
    for k,v in dObama.items():
        dObamaNoBush.update(OrderedDict({k: 0}))
    #print ("Things Bush has Obama doesn't:\n")
    #print(dBushNoObama)
    #print ("Things Obama has Bush doesn't:\n")
    #print(dObamaNoBush)
    dObama.update(dCommonObama)
    dObama.update(dBushNoObama)
    dObamaNoBush.update(dCommonBush)
    dObamaNoBush.update(dBush)
    dBush = dObamaNoBush
    #print("\n")
    return dObama, dBush

#Part 3


#Not taking out two words
def separateFileToList(file):
    '''seperateFileToList will read the file “regions.txt” of grouped regions that
    contains the names of the countries and some keywords within that region and
    generate it to separate eight lists.
	Input: a file (In this case, regions.txt)
	outputs: lists of: 
   listNA: the list of all the words/countries in North America
   listME: the list of all the words/countries in Middle East
   listAs: the list of all the words/countries in Asia
   listSA: the list of all the words/countries in South America
   listLA: the list of all the words/countries in Latin America
   listAf: the list of all the words/countries in Africa
   listE: the list of all the words/countries in Europe
   listO: the list of all the other words/countries (e.g. Antarctica…)

   
   doctest:
   >>> separateFileToList("regions.txt")
   (['north america', 'antigua', 'antiguan', 'arawak', 'barbuda', 'barbudan', 'bahamas', 'barbados', 'belize', 'bermuda', 'canada', 'canadian', 'costa rica', 'cuba', 'dominica', 'dominican republic', 'el salvador', 'grenada', 'guatemala', 'haiti', 'honduras', 'jamaica', 'nicaragua', 'st. kitts', 'nevis', 'st. lucia', 'st. vincent', 'the grenadines', 'trinidad', 'tobago'], ['middle east', 'isis', 'bahrain', 'cyprus', 'egypt', 'iran', 'iraq', 'israel', 'jordan', 'kuwait', 'lebanon', 'oman', 'qatar', 'saudi arabia', 'syria', 'turkey', 'united arab emirates', 'yemen', 'islam'], ['asia', 'asian', 'afghanistan', 'armenia', 'azerbaijan', 'bangladesh', 'bhutan', 'brunei', 'burma', 'cambodia', 'china', 'chinese', 'georgia', 'hong kong', 'india', 'indonesia', 'japan', 'kazakhstan', 'korea', 'korean kyrgyzstan', 'laos', 'macau', 'malaysia', 'maldives', 'mongolia', 'mongolian', 'nepal', 'pakistan', 'palestine', 'philippines', 'philippine', 'singapore', 'sri lanka', 'taiwan', 'tajikistan', 'thailand', 'turkmenistan', 'uzbekistan', 'vietnam', 'vietnamese'], ['south america', 'argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador', 'guyana', 'paraguay', 'peru', 'suriname', 'uruguay', 'venezuela'], ['latin america', 'belize', 'costa rica', 'el salvador', 'guatemala', 'honduras', 'nicaragua', 'panama', 'mexico', 'mexican'], ['africa', 'african', 'algeria', 'angola', 'benin', 'botswana', 'burkina faso', 'burundi', 'cameroon', 'cape Verde', 'central african republic', 'chad', 'comoros', 'democratic republic of the congo', 'republic of the congo', "cote d'ivoire", 'djibouti', 'egypt', 'equatorial guinea', 'eritrea', 'ethiopia', 'gabon', 'the gambia', 'ghana', 'guinea', 'guinea-bissau', 'kenya', 'lesotho', 'liberia', 'libya', 'madagascar', 'malawi', 'mali', 'mauritania', 'mauritius', 'morocco', 'mozambique', 'namibia', 'niger', 'nigeria', 'rwanda', 'Sao Tome', 'sao tome', 'principe', 'senegal', 'seychelles', 'sierra Leone', 'somalia', 'south africa', 'sudan', 'swaziland', 'tanzania', 'togo', 'tunisia', 'uganda', 'zambia', 'zimbabwe'], ['europe', 'european albania', 'andorra', 'austria', 'belarus', 'belgium', 'bosnia', 'herzegovina', 'bulgaria', 'croatia', 'czech republic', 'czechs', 'denmark', 'estonia', 'finland', 'france', 'germany', 'greece', 'hungary', 'iceland', 'ireland', 'italy', 'italians', 'italian', 'latvia', 'liechtenstein', 'lithuania', 'luxembourg', 'malta', 'moldova', 'monaco', 'netherlands', 'norway', 'poland', 'portugal', 'portuguese', 'romania', 'russia', 'russian', 'russians', 'san marino', 'serbia', 'Montenegro', 'serbia', 'montenegro', 'slovakia', 'slovenia', 'spain', 'spainish', 'sweden', 'switzerland', 'ukraine', 'ukrainians', 'ukrainian', 'united kingdom', 'uk', 'britain', 'british'], ['other', 'aruba', 'cayman islands', 'australia', 'australian fiji', 'kiribati', 'marshall islands', 'nauru', 'new zealand', 'palau', 'papua new guinea', 'samoa', 'solomon islands', 'tonga', 'tuvalu', 'tuvaluan', 'vanuatu', 'antartica', 'south pole', 'north pole'])
   '''
    count = 1
    fileRegions= open(file,'rt', encoding = 'UTF-8')
    while True: 
        line = fileRegions.readline()
        if not line:  # check for end of file 
            break
        if count == 1:
            listNA = line.strip().split(", ")
            count += 1
            fileRegions.readline()
        elif count == 2:
            listME = line.strip().split(", ")
            count += 1
            fileRegions.readline()
        elif count == 3:
            listAs = line.strip().split(", ")
            count += 1
            fileRegions.readline()
        elif count == 4:
            listSA = line.strip().split(", ")
            count += 1
            fileRegions.readline()
        elif count == 5:
            listLA = line.strip().split(", ")
            count += 1
            fileRegions.readline()
        elif count == 6:
            listAf = line.strip().split(", ")
            count += 1
            fileRegions.readline()
        elif count == 7:
            listE = line.strip().split(", ")
            count += 1
            fileRegions.readline()
        elif count == 8:
            listO = line.strip().split(", ")
            count += 1
            fileRegions.readline()
    return listNA, listME, listAs, listSA, listLA, listAf, listE, listO
def countFrequenciesAccurateHelper(rList, fList):
    #more accurate but way slower
    '''countFrequenciesAccurateHelper counts the total frequencies of each
        word in rList that appears in fList. It is a hepler function for
        
	Inputs: rList: (list) a list representing the words for an region
	        fList: (list) the modified list of all the words in the SOU
	        speech of a President
	Output: (int) the total frequencies of each word in rList that appears
                in fList

	doctest:
        >>> fList = ["i","not","i","kid","i","sure","ice", "cream","ice", "i","cream"]
        >>> rList = ["i","kid","sure","ice cream"]
        >>> countFrequenciesAccurateHelper(rList, fList)
        7
        >>> rList = ["i","kid","sure","ice cream"]
        >>> fList = ["i","not","i","kid","i","sure","ice", "cream","ice", "i","cream","ice"]
        >>> countFrequenciesAccurateHelper(rList, fList)
        7
    '''
    freq = 0
    i = 0
    while i< len(fList):
        for names in rList:
            if " " not in names:
                if names == fList[i]:
                    freq += 1
            elif " " in names:
                nameList = names.split()
                if len(fList) - i >= len(nameList):
                    if fList[i] == nameList[0]:
                        j = 0
                        isSameSequence = True
                        while j < len(nameList):
                            if fList[i+j] != nameList[j]:
                                isSameSequence = False
                                break
                            else:
                                j += 1
                        if isSameSequence:
                            freq += 1
        i += 1         
    return freq

def countFrequenciesAccurate(rList, fList):
    """countFrequenciesAccurate takes in an array with eight lists and applies
        countFrequenciesAccurateHelper to each list, designed specific for us
        to calculate the frequencies of the regions that appears in each
        President's speech.
        input: rList: an array with 8 lists 
               fList: an array with 8 lists
        output: The list freqList 

        doctest:
    >>> rList = [["apple","1","one"],["orange","2","two"],["banana","3","three"],["pineapple","4","four"],["grape","5","five"],["blueberry","6","six"],["strawberry","7","seven"],["kiwi","8","eight"]]
    >>> fList = ["apple","2","happy","blah","8","hahah","banana","3","three","pineapple","4","four","grape","5","lol","blueberry","6","sad","strawberry","7","college","kiwi","8","eight"]
    >>> countFrequenciesAccurate(rList, fList)
    [1, 1, 3, 3, 2, 2, 2, 4]
    """
    freqNA = countFrequenciesAccurateHelper(rList[0], fList)
    freqME = countFrequenciesAccurateHelper(rList[1], fList)
    freqAs = countFrequenciesAccurateHelper(rList[2], fList)
    freqSA = countFrequenciesAccurateHelper(rList[3], fList)
    freqLA = countFrequenciesAccurateHelper(rList[4], fList)
    freqAf = countFrequenciesAccurateHelper(rList[5], fList)
    freqE = countFrequenciesAccurateHelper(rList[6], fList)
    freqO = countFrequenciesAccurateHelper(rList[7], fList)
    
    freqList = [freqNA, freqME, freqAs, freqSA, freqLA, freqAf, freqE, freqO]
    return freqList

def main():
    '''The main function will call the functions above and creates a double bar graph that
    demonstrates the frequency of each of the eight regions that has been brought up by both
    Bush and Obama
    '''
    #create dicts
    rawInformation = mainHelperPartTwo()
    newD = sortDictionary(rawInformation[0], rawInformation[1])   
    keys = []
    valuesO = []
    for k,v in newD[0].items():
        keys += [k]
        valuesO += [v]
    valuesB = []
    for k,v in newD[1].items(): 
        valuesB += [v]
################################
    #plots part 2
    fig = plt.figure()
    ax0 = fig.add_subplot(211)
    x = np.arange(len(valuesO))
    ax0.step(x,valuesO,color='b',label='Obama')
    ax0.step(x,valuesB,color='r',label='Bush')
    ax0.set_xticks(x)
    ax0.set_xticklabels(keys,rotation=90, fontsize=7)
    ax0.set_ylabel('Frequency')
    ax0.set_xlabel('The Top 20 Most Said Words (Note that when the frequency is 0, the word is not in their top twenty)', fontsize = 7)
    ax0.set_title("Part 2: Top 20 SOU Words of Obama and Bush")
    ax0.legend()

################################
    #plots part 3
    ax1 = plt.subplot(212)
    rList = separateFileToList("regions.txt")
    regionsToBeAnalyzed = ["North America\n(no US)","Middle East", "Asia", "South America", "Latin America", "Africa", "Europe", "Other"]
    fListBush = rawInformation[2]
    fListObama = rawInformation[3]
    x = np.arange(len(regionsToBeAnalyzed))
    yObama = countFrequenciesAccurate(rList, fListObama)
    yBush = countFrequenciesAccurate(rList, fListBush)
    width = 0.25
    rects1 = ax1.bar(x, yObama, width)
    rects2 = ax1.bar(x + width, yBush, width, color='r')
    ax1.set_xticks(x + width/2)
    ax1.set_xticklabels(regionsToBeAnalyzed,rotation=25, fontsize=7)
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel('Regions')
    ax1.set_title("Part 3: How Frequent Do Obama and Bush Address These \nFOREIGN Regions in the World?")
    ax1.legend((rects1[0], rects2[0]), ('Obama', 'Bush'))
    plt.tight_layout()
    plt.show()
################################

import doctest 
doctest.testmod() 
    
main()


