"""
using a function to cycle through a computer created list(myUniqueList),
The function addToList takes a user input to check the computer created list(myUniqueList)
if the input is equal to an index in myUniqueList the input is added to MyLeftOvers and returns false
if the input is unigue then it adds the input to myUniqueList and returns true

"""
myUniqueList = []
for x in range(10):
   myUniqueList.append(x + 1)

MyLeftOvers = []


def addToList(x):  
    if (x in myUniqueList):
        MyLeftOvers.append(x)
        return False
    else:
        myUniqueList.append(x)
        return True

addToList(10)
addToList(15)
addToList(1)
addToList(2)
addToList(3)
addToList("hello world")
addToList([7])
addToList([7])
print(myUniqueList)
print(MyLeftOvers)






