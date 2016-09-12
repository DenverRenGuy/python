import time

def bubbleSort(arr):
    temp = 0
    sortCount = 0
    sorted = False
    while sorted == False:
        for count in range(1,len(arr)):
            if arr[count]<arr[count-1]:
                temp = arr[count]
                arr[count] = arr[count-1]
                arr[count-1] = temp
                sortCount += 1
            print arr
        if sortCount == 0:
            sorted = True
        else:
            sortCount = 0

def generateRandomArr():
    import random
    arr = []
    for count in range(0,100):
        arr.append(round(random.randint(0,5000)))
    return arr

#Test Bubble Sort Function
unsorted = generateRandomArr()

start = time.clock()
bubbleSort(unsorted)
end = time.clock()
print '%f seconds' % (end-start)
