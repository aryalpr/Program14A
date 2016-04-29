__author__="Priyanka Aryal, Rojina Amatya, Elias Eid, Masson Price"
__date__="4/22/2016"

"""
Priyanka - 1. Constructor, 4. Difference of sets
Rojina - 2. Union of sets,  5. Test for membership 
Elias - 3. Intersection of sets, 9. String method
Masson - 6. Determine subset, 7. Determine Superset, 8. Determine number of elements
"""
from modCustomSet import *
s1 = CustomSet([1,3,5,1])
s2 = CustomSet([1,2,3,4])

print("Testing the difference of two sets: ")
s3 = s1 - s2
s4 = s2 - s1
print("s1 - s2 : ", s3)
print("s2 - s1 : ", s4)

    
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

#-- Rojina Amatya
print("\n")
U1= CustomSet([20,40,60,80])
U2= CustomSet([30,40,50,80,100])
U3= CustomSet([25,89,79,67,12,45])
print("Testing for the Union Method")
print("-"*30)
UA= U1+U2
UB= U2+U3
print("The Union between two sets are:",UA)
print("THe Union between two sets are:",UB)

print("\n")
M1= CustomSet([20,40,60,80])
M2= CustomSet([30,40,50,80,100])
M3= CustomSet([25,89,79,67,12,45])
print("Testing for the Boolean method")
print("-"*45)
print("The result is:",20 in M1)
print("The result is:",28 in M2)
print("The result is:",89 in M3)
print("The result is:",85 in M1)
print("The result is:",100 in M2)
print("The result is:",62 in M3)

#-- Masson Price
print("-"*25)
print("Testing len function")
s1 = CustomSet([1,2,3,4,5,6])
print("Length should be 6: ", len(s1))
s2 = CustomSet([1,3,4])
s3 = CustomSet([7,8,9])
print("Testing subset: ")
print("Should be true: ", s2<=s1)
print("Should be false: ", s3<=s1)
print("Testing superset")
print("Should be true: ", s1>=s2)
print("Should be false: ", s1>=s3)
