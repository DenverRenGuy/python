#Multiply function
def multiplyList(myList, myMultiple):
    newList = [item * myMultiple for item in myList]
    return newList


#Test function

myList = [1,2,3,4,5,6]
myMultiple = 7

print multiplyList(myList, myMultiple)
