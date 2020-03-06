#!/usr/bin/env python
# coding: utf-8

# # HMW1

# ## Lists
# 1)	Create a list with the following color names: ‘blue’, ‘white’, ‘green’, ‘red’, ‘pink’, ‘yellow’.

# In[1]:


list = ['blue', 'white', 'green', 'red', 'pink', 'yellow']


# 2)	Print the number of elements in the list.

# In[2]:


print(list)


# 3)	Search for the ‘blue’ element in the list. Search for the ‘purple’ element in the list

# In[3]:


for i in list:
    if i == 'blue':
        print('blue is in the list!')


# In[4]:


for i in list:
    if i == 'purple':
        print('purple is in the list!')


# 4)	Print the index for the element ‘white’ and ‘black’ in the list. Use an exception handler to deal with the error when the element is not in the list.

# In[5]:


try:
    print('white index is: ' + str(list.index('white')))
except ValueError:
    print('white is not an element of list')

try:
    print('black index is: ' + str(list.index('black')))
except ValueError:
    print('black is not an element of list')


# 5)	Add the following elements to the list ‘violet and ‘grey’.

# In[6]:


list.extend(['violet', 'grey'])
print(list)


# 6)	Add the following list to the color list, [‘brown’, ‘black’]

# In[7]:


list.append(['brown', 'black'])
print(list)


# 7)	Replace the first three elements of the list with the element ‘cyan’

# In[8]:


list[0] = 'cyan'
del list[1:3]


# In[9]:


print(list)


# 8)	Add the element ‘orange’ to the list that is in the list:

# In[10]:


list[6].append('orange')


# 9)	Delete all the elements from the list, except the first two.

# In[11]:


del list[2:]


# 10)	Create a the following 2D list
# [[0, 1, 2, 3, 4],
# [5, 6, 7, 8, 9],
# [10, 11, 12, 13, 14],
# [15, 16, 17, 18, 19],
# [20, 21, 22, 23, 24]]

# In[12]:


list2D = [[0, 1, 2, 3, 4],
[5, 6, 7, 8, 9],
[10, 11, 12, 13, 14],
[15, 16, 17, 18, 19],
[20, 21, 22, 23, 24]]


# 11)	From the following list of lists, print the number of elements from the last list:

# In[13]:


numbers = [[1,2],[3,4],[5,6],[7,8,9]]
print(len(numbers[3]))


# 12)	Create a list which elements are the odd square from 1 to 10:

# In[14]:


listOdd = []
for i in range(1,10):
    if i % 2 == 1:
        listOdd.extend([i * i])
print(listOdd)


# 13)	Create a 2D list which represent the multiplication table of 3 from 1 to 10:

# In[15]:


list3 = []
for i in range (1,11):
    list3 += [[3, i, i*3]]
    
print(list3)


# 14)	Write a Python program to generate a 4 * 3 * 2 3D array whose element are '?'.
# 

# In[16]:


listQ = []
for i in range(1,5):
    listAux = []
    for i in range(1,4):
        listAux.append(['?','?'])
    listQ.append(listAux)
print(listQ)


# ## Dictionaries
# 1.	Create a dictionary which keys are the numbers from 1 to 5 and which individual values are the corresponding letter of the alphabet

# In[17]:


dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(dict)


# 2.	Search for the 4 key in the dictionary. Search for the 7 key in the dictionary. 
# 

# In[18]:


if 4 in dict.keys():
    print(dict[4])

if 7 in dict.keys():
    print(dict[7])


# 3.	Search for the value ‘a’ in the dictionary. Search for the value ‘z’ in the dictionary.
# 

# In[19]:


for val in dict.values():
    if val == 'a' or val == 'z':
        print(val)


# 4.	Add an extra element to the dictionary, which key is 6 and value is f.
# 

# In[20]:


dict[6] = 'f'
print(dict)


# 5.	Delete the element from the dictionary whose key is 2

# In[21]:


del dict[2]
print(dict)


# 6.	Find the maximum and minimum value in a dictionary

# In[22]:


dictNum = {'x':700, 'y':56874, 'z': 990}
maxK = max(dictNum.keys(), key=(lambda key: dictNum[key]))
minK = min(dictNum.keys(), key=(lambda key: dictNum[key]))
print('Max : ' + str(dictNum[maxK]) + '\nMin : ' + str(dictNum[minK]))


# ## Numpy
# 1.	Generate an array from 0 to 19.

# In[23]:


import numpy as np


# 1.	Generate an array from 0 to 19.

# In[24]:


arr = np.arange(20)
print(arr)


# 2.	Generate an array from 30 to 39

# In[25]:


arr = np.arange(30, 39, 1)
print(arr)


# 3.	Generate a 6x6 matrix of 0s

# In[26]:


matZeros = np.zeros((6,6))
print(matZeros)


# 4.	Generate a 4x4 matris of 1s

# In[27]:


matOnes = np.ones((4,4))
print(matOnes)


# 5.	Following the provided numPy array, return an array with the last element of each row:
# 
# sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

# In[28]:


sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
last = sampleArray[:,2]
print(last)


# 6.	Reverse the following array (first element becomes last).
# 
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

# In[29]:


npArray = np.array([12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37])
np.flip(npArray)


# 7.	Create the following matrix and name it CwHwMat:
# 

# In[30]:


CwHwMat = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(CwHwMat)


# From CwHwMat generate the following slice:
#     
# [[2 3]
# [6 7]]
# 

# In[31]:


CwHwMat[[[0,0],[1,1]],[[1,2],[1,2]]]


# 8.	From CwHwMat generate the following slice:

# In[32]:


CwHwMat[[[1,1],[2,2],[3,3]],[[2,3],[2,3],[2,3]]]


# 9.	Slice CwHwMat into two ndarrays, name one as X and the other as y:
# 
# X: 
# array([[ 1,  2,  3],
# [ 5,  6,  7],
# [ 9, 10, 11],
# [13, 14, 15]])
# 
# y:
# array([ 4,  8, 12, 16])
# 

# In[33]:


x = CwHwMat[:,0:3]
y = CwHwMat[:,3]
print('x:')
print(x)
print('y:')
print(y)


# 10.	Split the X into two ndarray named train and test, train will have 75% of the observations and test will have 25%.
# 

# In[34]:


train= x[[1,2,3],:]
test = x[0,:]
print('test:')
print(test)
print('train:')
print(train)

