'''
do

  swapped = false

  for i = 1 to indexOfLastUnsortedElement-1

    if leftElement > rightElement

      swap(leftElement, rightElement)

      swapped = true; ++swapCounter

while swapped
'''

list = [2,5,1,6,3,7,9,4,8]
print("Unsorted list: " + str(list))

while True:
    swapped = False
    for i in range(0,len(list)-1):
        if list[i] > list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
            swapped = True
    if not swapped:
        break

print("Sorted list: " + str(list))