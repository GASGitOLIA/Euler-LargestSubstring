# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:11:46 2017

@author: rmaskus
"""

f = open("input.txt", "r")

numberList = [] 
highest13 = []
current13 = []
highest = 0
current = 1

for ch in iter(lambda: f.read(1), ''):
    num = int(ch)
    numberList.append(num)


i = 0
j = 0

x = len(numberList) -13

while i < x:
    j = 0
    current13 = numberList[i:i+13]
    while j < len(current13):
        current = current * current13[j]
        j += 1
    
    if current > highest:
        highest = current
        highest13 = current13
    current = 1
    i += 1

print(highest)
print(highest13)

f.close()
