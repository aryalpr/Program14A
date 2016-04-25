__author__="Priyanka Aryal, Rojina Amatya, Elias Eid"
__date__="4/22/2016"

"""
Priyanka - 1, 4, 7
Rojina - 2, 5, 8
Elias - 3, 6, 9
"""
class CustomSet:
    def __init__(self, tmpSetList):
        self._setList = []
        for listElement in tmpSetList:
            if listElement not in self._setList:
                self._setList.append(listElement)


    
