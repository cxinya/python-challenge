# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:03:03 2017

@author: Cynthia
"""



import re
import glob
import os

# Number of files starting with "paragaph" in directory
numFiles = len(glob.glob1("raw_data/", "paragraph*"))


# Create new folder for analyzed text

os.mkdir("analyzed_text")

for i in range(1,(numFiles+1)):
    
    path = "raw_data/paragraph_" + str(i) + ".txt"
    file = open(path, "r").read()
    
    newFileName = "analyzed_text/newParagraph_" + str(i) + ".txt"
    newFile = open(newFileName, "w")
    
    paragraphs = file.split("\n")      # Split into paragraphs
    
    for para in paragraphs:
        
        # Remove punctuation from paragraph
        paraNoPunc = para.replace(",","").replace('"', '').replace("'","") \
                    .replace(".","").replace("-","").replace("(","") \
                    .replace(")","").replace(">","").replace("<","")
                    
        # Split paragraph into words with no punctuation (for letter count)
        wordList = paraNoPunc.split()
        
        # Split paragraph into sentences
        sentenceList = re.split('[?.!] +', para)
        
        if len(wordList) > 1:
        
            # Find average letter count
            letterCount = 0
            for word in wordList:
                letterCount = letterCount + len(word)
            letterAvg = round(letterCount/len(wordList),2)
            
            # Find average sentence length
            wordsInSent = 0
            for sentence in sentenceList:
                wordsInSent = wordsInSent + len(sentence.split())
            wordsAvg = round(wordsInSent/len(sentenceList),2)
            
            print(para)
            print("\n\tParagraph Analysis")
            print("\t-----------------------")
            print("\tApproximate Word Count: " + str(len(wordList)))
            print("\tApproximate Sentence Count: " + str(len(sentenceList)))
            print("\tAverage Letter Count: " + str(letterAvg))
            print("\tAverage Sentence Length: " + str(wordsAvg) + "\n")
            print("------------------------------------------" + "\n")

            # Create new files with paragraph analysis summary
            newFile.write(para)
            newFile.write("\n\n\tParagraph Analysis\n")
            newFile.write("\t-----------------------\n")
            newFile.write("\tApproximate Word Count: " + str(len(wordList)) + "\n")
            newFile.write("\tApproximate Sentence Count: " + str(len(sentenceList)) + "\n")
            newFile.write("\tAverage Letter Count: " + str(letterAvg) + "\n")
            newFile.write("\tAverage Sentence Length: " + str(wordsAvg) + "\n\n")
            
    newFile.close()

