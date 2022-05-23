"""
mark first element as sorted

for each unsorted element X

  'extract' the element X

  for j = lastSortedIndex down to 0

    if current element j > X

      move sorted element to the right by 1

    break loop and insert X here
"""
list = [3,7,1,2,5,9,8,3.4,6]
print("Unsorted list: " + str(list))
for i in range(1,len(list)):
  temp = list[i]
  for j in range(i-1,-1,-1):
    if list[j] > temp:
      list[j+1] = list[j]
      list[j] = temp
print("Sorted list: " + str(list))