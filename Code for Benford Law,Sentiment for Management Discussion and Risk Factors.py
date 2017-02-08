from scipy.stats import ks_2samp
from pandas import Series, DataFrame
from collections import Counter
import pandas as pd
import numpy as np
import math as m
import random
import re






#Code for Benford's Law





# All numbers
anf = re.findall(r'\d+(?:,\d+)?', open('<insert file name>', 'r').read())

# Remove comma's between numbers
anf = [int(x.replace(',', '')) for x in anf]

numexp = re.compile(r'\d+(\.\d+)?([eE]\d+)?')
leading = set("123456789")

actual_anf = [] 
for item in anf:
    for match in numexp.finditer(str(item)):
        for digit in match.group(0):
            if digit in leading:
                actual_anf.append(int(digit))
                break

# Expected frequency (Benford's Law)            
e = [30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6]

ks_cutoff = float(1.36/m.sqrt(len(actual_anf)))
print "KS Cutoff: {}\n".format(ks_cutoff)

a_x = [float(actual_anf.count(i))*100/len(actual_anf) for i in range(1,10)]
print "Actual Frequency (x): {}\n".format(a_x)

ks1 = max(abs(a_x[0]-e[0]),abs((a_x[0]+a_x[1])-(e[0]+e[1])),abs((a_x[0]+a_x[1]+a_x[2])-(e[0]+e[1]+e[2]))
            ,abs((a_x[0]+a_x[1]+a_x[2]+a_x[3])-(e[0]+e[1]+e[2]+e[3]))
            ,abs((a_x[0]+a_x[1]+a_x[2]+a_x[3]+a_x[4])-(e[0]+e[1]+e[2]+e[3]+e[4]))
            ,abs((a_x[0]+a_x[1]+a_x[2]+a_x[3]+a_x[4]+a_x[5])-(e[0]+e[1]+e[2]+e[3]+e[4]+e[5]))
            ,abs((a_x[0]+a_x[1]+a_x[2]+a_x[3]+a_x[4]+a_x[5]+a_x[6])-(e[0]+e[1]+e[2]+e[3]+e[4]+e[5]+e[6]))
            ,abs((a_x[0]+a_x[1]+a_x[2]+a_x[3]+a_x[4]+a_x[5]+a_x[6]+a_x[7])-(e[0]+e[1]+e[2]+e[3]+e[4]+e[5]+e[6]+e[7]))
            ,abs((a_x[0]+a_x[1]+a_x[2]+a_x[3]+a_x[4]+a_x[5]+a_x[6]+a_x[7]+a_x[8])-(e[0]+e[1]+e[2]+e[3]+e[4]+e[5]+e[6]+e[7]+e[8])))

print "KS Statistic (x): {}\n".format(float(ks1/100))

if(float(ks1/100)>ks_cutoff):
    print "Evidence of potential manipulation"
else:
    print "No evidence of manipulation"
    
    
    
 
    
          
#Sentiment Analysis for Management and Discussion    
 
    
       
             
    
pos = set(re.findall('[A-Za-z0-9-]+', open('HW7_LM_pos_words.txt', 'r').read()))
neg = set(re.findall('[A-Za-z0-9-]+', open('HW7_LM_neg_words.txt', 'r').read()))

# All words + numbers
a = re.findall('[A-Za-z0-9-]+', open('ANF-MD&A-P22-36-2016-10K.txt', 'r').read())

# Remove numbers
a2 = [x for x in a if not (x.isdigit())]

# Check for single alphabet strings
a3 = [x for x in a2 if len(x)==1]

# Remove single alphabet strings
a4 = [x for x in a2 if x not in a3]

# Add back one "a", taken to be feasible word of all in w3
a4 += "a"

# Keep only unique words
a5 = list(set(a4))

# Convert words to lowercase
a6 = map(lambda x:x.upper(), a5)
print "Unique words: {}\n".format(len(a6))

# Convert to set
a6 = set(a6)

# Positive word count
pos_cnt = set.intersection(pos,a6)
print "Positive words: {}\n".format(pos_cnt)

# Negative word count
neg_cnt = set.intersection(neg,a6)
print "Negative words: {}\n".format(neg_cnt)

I = (float(len(pos_cnt)-len(neg_cnt)))/len(a6)
print "Sentiment score I: {}\n".format(I)

II = float(len(neg_cnt))/len(a6)
print "Sentiment score II: {}\n".format(II) 

print "Number of 'no': {}\n".format(re.findall("no",str(a6)))

print "Number of 'not': {}\n".format(re.findall("not",str(a6)))

print "Number of 'never': {}\n".format(re.findall("never",str(a6)))     






#Sentiment Analysis for Risk Factors






pos = set(re.findall('[A-Za-z0-9-]+', open('HW7_LM_pos_words.txt', 'r').read()))
neg = set(re.findall('[A-Za-z0-9-]+', open('HW7_LM_neg_words.txt', 'r').read()))

# All words + numbers
a = re.findall('[A-Za-z0-9-]+', open('ANF-RiskFactors-2016-10K.txt', 'r').read())

# Remove numbers
a2 = [x for x in a if not (x.isdigit())]

# Check for single alphabet strings
a3 = [x for x in a2 if len(x)==1]

# Remove single alphabet strings
a4 = [x for x in a2 if x not in a3]

# Add back one "a", taken to be feasible word of all in w3
a4 += "a"

# Keep only unique words
a5 = list(set(a4))

# Convert words to lowercase
a6 = map(lambda x:x.upper(), a5)
print "Unique words: {}\n".format(len(a6))

# Convert to set
a6 = set(a6)

# Positive word count
pos_cnt = set.intersection(pos,a6)
print "Positive words: {}\n".format(pos_cnt)

# Negative word count
neg_cnt = set.intersection(neg,a6)
print "Negative words: {}\n".format(neg_cnt)

I = (float(len(pos_cnt)-len(neg_cnt)))/len(a6)
print "Sentiment score I: {}\n".format(I)

II = float(len(neg_cnt))/len(a6)
print "Sentiment score II: {}\n".format(II)

print "Number of 'no': {}\n".format(re.findall("no",str(a6)))

print "Number of 'not': {}\n".format(re.findall("not",str(a6)))

print "Number of 'never': {}\n".format(re.findall("never",str(a6))) 

