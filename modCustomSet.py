__author__="Priyanka Aryal, Rojina Amatya, Elias Eid, Masson Price"
__date__="4/22/2016"

"""
Priyanka - 1, 4 
Rojina - 2, 5
Elias - 3, 9
Masson - 6, 7, 8
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
        '''Description: subtracting one list from the other
        Pre-Condition: tmpRoomType should be a string and rest should be integer
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
