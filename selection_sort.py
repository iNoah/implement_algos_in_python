'''
repeat (numOfElements - 1) times

  set the first unsorted element as the minimum

  for each of the unsorted elements

    if element < currentMinimum

      set element as new minimum

  swap minimum with first unsorted position
'''
list = [3,44,38,5,47,15,36,36,26,27,2,46,4,19,50,48]
print("Unsorted list: " + str(list))

for i in range(0,len(list)-1):
    minium = list[i]
    new_minium_index = i
    for j in range(i+1,len(list)):
        if list[j] < minium:
            minium = list[j]
            new_minium_index = j
    temp = list[i]
    list[i] = minium
    list[new_minium_index] = temp

print("Sorted list: " + str(list))
