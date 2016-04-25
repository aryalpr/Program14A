__author__="Priyanka Aryal, Rojina Amatya, Elias Eid"
__date__="4/22/2016"

"""
Priyanka - 1, 4 
Rojina - 2, 5
Elias - 3, 9
Masson - 6, 7, 8
"""
from modCustomSet import *
s1 = CustomSet([1,3,5,1])
s2 = CustomSet([1,2,3,4])
#s3 = s1 - s2
#print(s3)


# --Elias Eid

print("Printing s1: ")
print(s1)
print("Printing s2: ")
print(s2)

print("Testing the intersection method on s1 and s2:")
sA = s1 & s2
print(sA)

print("Creating two sets with no elements in common sB and sC:")
sB= CustomSet([40,15,60,80,15])
sC = CustomSet([37,56,17,19,20])
print(sB)
print(sC)
print("Finding the intersection of sB and sC:")
sD = sB & sC
print(sD)



