from typing import List


list1 = ['Bench press', 'deadlift', 'squat']
list2 = ['3x12', '5x5', '3x8']
list3 = [120, 360, 360]

lists = zip(list1, list2, list3)
print(*lists)