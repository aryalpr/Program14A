__author__="Priyanka Aryal, Rojina Amatya, Elias Eid"
__date__="4/22/2016"

"""
Priyanka - 1, 4, 7
Rojina - 2, 5, 8
Elias - 3, 6, 9
"""
from modCustomSet import *
s1 = CustomSet([1,3,5,1])
s2 = CustomSet([1,2,3,4])
s3 = s1 - s2
print(s3)
