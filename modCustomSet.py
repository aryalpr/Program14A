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

    
