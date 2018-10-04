
# coding: utf-8

# In[27]:


#In a class on 100 students, 80 students passed in all subjects, 10 failed in one subject, 7 failed in two subjects and 3 failed in three subjects. 
#Find the probability distribution of the variable for number of subjects a student from the given class has failed in.
import numpy as np
import pandas as pd
import numpy.random as randn
total=100
all_pass=80
one_fail=10
two_fail=7
three_fail=3
print("probability of passing all subjects=", all_pass/total)
print("probability of failing in one subjects=", one_fail/total)
print("probability of fialing in two subjects=", two_fail/total)
print("probability of failing in three subjects=", three_fail/total)


# In[14]:


#A test is conducted which is consisting of 20 MCQs (multiple choices questions) with every MCQ having its four options out of 
#which only one is correct.Determine the probability that a person undertaking that test has answered exactly 5 questions wrong.
import numpy as np
import math
probability=((20*19*18*17*16)*(0.25**15)*(0.75**5))/math.factorial(5)
print("probability of correctly answering 5 questions is=",probability)


# In[15]:


#A die marked A to E is rolled 50 times. Find the probability of getting a “D” exactly 5 times.
#n=50
#k=5
#n-k=45
probability=((50*49*48*47*46)*((1/5)**45)*((4/5)**5))/math.factorial(5)
print("probability of getting a “D” exactly 5 times is=",probability)


# In[25]:


import statistics
from statistics import pstdev
x=[1550, 1700, 900, 850, 1000, 950]
y=pstdev(x)
print("standard deviation of the population is=",y)


# In[26]:


import statistics
from statistics import pvariance
x=[3, 21, 98, 203, 17, 9]
y=pvariance(x)
print("variance of the population is=",y)


# In[4]:


#Two balls are drawn at random in succession without replacement from an urn containing 4 red balls and 6 black balls.Find the probabilities of all the possible outcomes.
#Total balls=10
#Total ways to draw the balls= 10C2
#Different combination of drawing the balls= [RR,RB,BR,BB]
#Chances of getting RR=4*3=12
#Chances of getting RB=4*6=24
#Chances of getting BR=6*4=24
#Chances of getting BB=6*5=30
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
x=nCr(10,2)
print("Probability of getting RR=",12/x)
print("Probability of getting RB=",24/x)
print("Probability of getting BR=",24/x)
print("Probability of getting BB=",30/x)



