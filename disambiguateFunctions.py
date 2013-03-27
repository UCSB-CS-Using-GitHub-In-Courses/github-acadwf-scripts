#!/usr/bin/python

import unittest



def containsDuplicates(aList):
    """Does list contain a duplicate
    
    >>> containsDuplicates(['foo','bar','fum'])
    False
    >>> containsDuplicates(['foo','foo','fum'])
    True
    >>> containsDuplicates(['foo','fum','foo'])
    True
    >>> containsDuplicates(['bar','foo','bar'])
    True
    """
    
    aList.sort()
    
    for i in range(len(aList)-1):
        if aList[i]==aList[i+1]:
            return True
    return False
    
def firstNamesWithNCharsOfLastName(userList, indices, n):
    "return list of new first names"

    names = []
    for i in range(len(indices)):
        names.append(userList[indices[i]]['first'] + "_" + 
                     userList[indices[i]]['last'][0:n])
        
    return names

def disambiguateFirstNamesOfTheseIndices(userList,indices):
    "return a new userList with certain first names disambiguated"
    
    newList = list(userList)
    
    needed = 1;  # Need up through 0 only (i.e. 1 char)
    
    firstNames = firstNamesWithNCharsOfLastName(userList,indices,needed)
    
    while( containsDuplicates(firstNames) ):
        print("firstNames=",firstNames,"needed=",needed)
        needed = needed + 1
        firstNames = firstNamesWithNCharsOfLastName(userList,indices,needed)
        
    for i in range(len(indices)):
        newList[indices[i]]['first'] = firstNames[i]

    return newList

def nameInFirstMatchingPairOfFirstNames(userList):
    "returns the first name that occurs more than once, or False if no dup first names" 

    for i in range(len(userList)):
        for j in range(i+1,len(userList)):
            if userList[i]['first'] == userList[j]['first']:
               return userList[i]['first']
    return False
           
def findIndicesOfMatchingFirstNames(userList,name):
    "returns list of the indices of the elements in userList who first names match name"

    indices = []
    for i in range(len(userList)):
        if userList[i]['first'] == name:
            indices.append(i)
            
    return indices
                          

def makeUserDict(first,last,github,email,csil):
    return {'first': first, 'last': last, 'github': github, 'email':email, 'csil':csil }

class TestSequenceFunctions(unittest.TestCase):



    def setUp(self):
        self.userList1 = [ makeUserDict('Chris','Jones','cj','cj@example.org','cj'),
                           makeUserDict('Chris','Smith','cs','cs@example.org','cs'),
                           makeUserDict('Mary Kay','Jones','mkj','mkj@example.org','mkj'),
                           makeUserDict('Mary','Kay','mkay','mkay@example.org','mkay') ]




        self.userList2 = [ makeUserDict('Chris_J','Jones','cj','cj@example.org','cj'),
                           makeUserDict('Chris_S','Smith','cs','cs@example.org','cs'),
                           makeUserDict('Mary Kay','Jones','mkj','mkj@example.org','mkj'),
                           makeUserDict('Mary','Kay','mkay','mkay@example.org','mkay') ]

        self.userList3 = [ makeUserDict('Chris','Jones','cj','cj@example.org','cj'),
                           makeUserDict('Chris','Smith','cs','cs@example.org','cs'),
                           makeUserDict('Mary','Jones','mkj','mkj@example.org','mkj'),
                           makeUserDict('Mary','Kay','mkay','mkay@example.org','mkay'),
                           makeUserDict('Dave','Jones','dj','dk@example.org','dj'),
                           makeUserDict('Dave','Kay','dk','dj@example.org','dk') ]

        self.userList4 = [ makeUserDict('Chris','Jones','cj','cj@example.org','cj'),
                           makeUserDict('Mary','Jones','mkj','mkj@example.org','mkj'),
                           makeUserDict('Dave','Kay','dk','dj@example.org','dk') ]

        self.userList5 = [   makeUserDict('Mary','Jones','mkj','mkj@example.org','mkj'),
                             makeUserDict('Chris','Jones','cj','cj@example.org','cj'),
                             makeUserDict('Chris','Smith','cs','cs@example.org','cs'),
                             makeUserDict('Mary','Kay','mkay','mkay@example.org','mkay'),
                             makeUserDict('Dave','Jones','dj','dk@example.org','dj'),
                             makeUserDict('Dave','Kay','dk','dj@example.org','dk') ]

    def test_firstNamesWithNCharsOfLastName1(self):
        result = firstNamesWithNCharsOfLastName(self.userList1,[0,1,2,3],1)
        self.assertEqual(result, ["Chris_J","Chris_S","Mary Kay_J","Mary_K"])

    def test_firstNamesWithNCharsOfLastName2(self):
        result = firstNamesWithNCharsOfLastName(self.userList1,[0,2],2)
        self.assertEqual(result, ["Chris_Jo","Mary Kay_Jo"])

    def test_disambiguateFirstNamesOfTheseIndices(self):
        result = disambiguateFirstNamesOfTheseIndices(self.userList1,[0,1])
        self.assertEqual(result,self.userList2)


    def test_nameInFirstMatchingPairOfFirstNames1(self):
        result = nameInFirstMatchingPairOfFirstNames(self.userList1);
        self.assertEqual(result,"Chris");

    def test_nameInFirstMatchingPairOfFirstNames3(self):
        result = nameInFirstMatchingPairOfFirstNames(self.userList3);
        self.assertEqual(result,"Chris");

    def test_nameInFirstMatchingPairOfFirstNames4(self):
        result = nameInFirstMatchingPairOfFirstNames(self.userList4);
        self.assertFalse(result);

    def test_nameInFirstMatchingPairOfFirstNames5(self):
        result = nameInFirstMatchingPairOfFirstNames(self.userList5);
        self.assertEqual(result,"Mary");


        

    def test_findIndicesOfMatchingFirstNames1(self):
        result = findIndicesOfMatchingFirstNames(self.userList1,'Chris');
        self.assertEqual(result,[0,1]);

    def test_findIndicesOfMatchingFirstNames3(self):
        result = findIndicesOfMatchingFirstNames(self.userList3,'Mary');
        self.assertEqual(result,[2,3]);

    def test_findIndicesOfMatchingFirstNames4(self):
        result = findIndicesOfMatchingFirstNames(self.userList4,'Dave');
        self.assertEqual(result,[2]);

    def test_findIndicesOfMatchingFirstNames5a(self):
        result = findIndicesOfMatchingFirstNames(self.userList5,'Mary');
        self.assertEqual(result,[0,3]);

    def test_findIndicesOfMatchingFirstNames5b(self):
        result = findIndicesOfMatchingFirstNames(self.userList5,'Chris');
        self.assertEqual(result,[1,2]);


if __name__ == '__main__':
    unittest.main()
    import doctest
    doctest.testmod()

