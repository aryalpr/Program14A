__author__="Priyanka Aryal, Rojina Amatya, Elias Eid"
__date__="4/22/2016"

"""
Priyanka - 1, 4 
Rojina - 2, 5
Elias - 3, 9
Masson - 6, 7, 8
"""
class CustomSet:
    def __init__(self, tmpSetList):
        self._setList = []
        for listElement in tmpSetList:
            if listElement not in self._setList:
                self._setList.append(listElement)

    
    def __str__(self):
        '''
        Definition:allow sets to be converted to a string with the elements
        surrounded by { } --created by Elias Eid
        Precondition: None
        Posrcondition: None
        '''

        tmpStr = '{ '
        for element in self._setList:
            if self._setList.index(element) != len(self._setList) - 1:
                tmpStr += str(element) + ', '
            else:
                tmpStr += str(element)
        tmpStr += ' }'
        return tmpStr

    def __and__(self, otherSet):
        '''
        Definition: returns a new set with elements common to the first and
        second sets. --created by Elias Eid
        Precondition: otherSet is a CustomSet
        Postcondition: None
        '''
        interList = [ element for element in self._setList if element in otherSet._setList]
        newSet = CustomSet(interList)

        return newSet

    def __add__(self,tmpList):
        """
        Description: This function returns the new list with the elements from
                     both first and the second sets
        Pre- condition:None
        Post- condition:None
        """
        for ct in self._setList:
            if ct not in tmpList._setList:
                tmpList._setList.append(ct)
        return tmpList._setList

    

    
