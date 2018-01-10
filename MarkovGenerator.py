# Yury Namgung
# CS Black 
# HW 8: Markov Text Generation
# Due: 30 Oct 2017

import random
punctuations = ['.', '?', '!']

"""Put k number of dollar signs before each sentence"""
def dollarify(wordList, k):
    dollarList = ['$']*k
    finList = ['$']*k
    #insert dollarList between sentences
    for i in range(0, len(wordList)):
        finList.append(wordList[i])
        if wordList[i][-1] in punctuations:
            finList+= dollarList
    return finList

"""making dictionary of what words come after k # of words put together"""
def markov_model(wordList, k):
    dict = {} #make new dictionary
    dWordList = dollarify(wordList, k)

    """go thru dWordList assigning key, next word is assigned to that key
    if the assigned word has a punctuation, the next key is $ (not that word)"""
    keyCount = 0
    while keyCount < len(dWordList) - k:
        #make tuple for dict value
        tup = ()
        for word in range(keyCount, keyCount+k):
            tup += (dWordList[word],) 
        assignedWord = dWordList[keyCount + k] #the word correlating w key

        if tup in dict:
            dict[tup].append(assignedWord)
        else:
            dict[tup] = [assignedWord]
        
        #skip assignedWords w punctions
        if assignedWord[-1] in punctuations:
            keyCount += k
        keyCount += 1
    return dict

"""generates a sentence from the markov model"""
def gen_from_model(mmodel, numWords):
    """starts with $ and finds next word thru dict, etc"""
    
    for i in mmodel:
        k = len(i) #number of words dict puts together
        break
    
    key = ('$',)*k #start w beg of sent

    #go thru keys, find $
    count = 0
    while count < numWords:
        nextWord = random.choice(mmodel[key])
        print(nextWord, end =' ')
        if nextWord[-1] in punctuations:
                key = ('$',)*k
        else: key = key[1:] + (nextWord,)
        count += 1
    
    """end paragraph w a punctuation"""
    nextWord = random.choice(mmodel[key])
    if nextWord[-1] in punctuations: 
        print(nextWord, end=' ')
    else:
        print(nextWord + random.choice(punctuations))
    return 

"""opens file, reads contents, and generates markov output"""
def markov(fileName, k, length):
    f1 = open(fileName, 'r') #read in words from file to train markov
    inputList = f1.readlines()
    f1.close()
    cleanList = list(map(lambda x: x.strip("\n"), inputList))

    """make wordList (split the str in cleanList)"""
    wordList = []
    for strings in cleanList:
        wordList += strings.split()
    #debug
    #print(wordList)

    """make a markov model and paragraph w length words from it"""
    mmodel = markov_model(wordList, k)
    #debug
    print(mmodel)
    finPara = gen_from_model(mmodel, length)
    return finPara


