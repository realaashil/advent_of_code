dummy = [0] * 100000
file = open("input.txt", "r")
array_left = []
array_right = []
for line in file:
    left, right = line.split("  ")
    array_left.append(int(left))
    array_right.append(int(right))

array_ans = []
array_left.sort()
array_right.sort()
j = 0
for i in array_left:
    if j >= len(array_right):
        break
    while j < len(array_right) and i > array_right[j]:
        j += 1
    while j < len(array_right) and i == array_right[j]:
        j += 1
        dummy[i] += 1

similar = 0
for i in array_left:
    similar += dummy[i] * i
print(similar)
