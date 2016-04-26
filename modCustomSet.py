__author__="Priyanka Aryal, Rojina Amatya, Elias Eid, Masson Price"
__date__="4/22/2016"

"""
Priyanka - 1. Constructor, 4. Difference of sets
Rojina - 2. Union of sets,  5. Test for membership 
Elias - 3. Intersection of sets, 9. String method
Masson - 6. Determine subset, 7. Determine Superset, 8. Determine number of elements
"""
class CustomSet:
    def __init__(self, tmpSetList):
        '''Description: initializing/Constructing
        Pre-Condition: tmpSetList should be a list
        Post-Condition: None'''
        self._setList = []
        for listElement in tmpSetList:
            if listElement not in self._setList:
                self._setList.append(listElement)


    def __sub__(self, otherList):
        '''Description: finding the difference of two sets
        Pre-Condition: otherList should be a list
        Post-Condition: None'''
        newList = []
        for char in self._setList:
            if char not in otherList._setList:
                newList.append(char)
                
        return newList

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

    
