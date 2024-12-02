# open the input


file = open("input.txt", "r")
array_left = []
array_right = []
for line in file:
    left, right = line.split("  ")
    array_left.append(left)
    array_right.append(right)

array_ans = []
array_left.sort()
array_right.sort()
for i in range(len(array_left)):
    array_ans.append(abs(int(array_left[i]) - int(array_right[i])))

ans = sum(array_ans)
print(ans)
