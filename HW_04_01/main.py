# lst = [0, 1, 0, 12, 3]
# lst = [0]
# lst = [1, 0, 13, 0, 0, 0, 5]
lst = [9, 0, 7, 0, 0, 0, 31, 55, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


n = len(lst)
i = 0
while i < n:
    if lst[i] != 0:
        i +=1
        continue
    else:
        lst.pop(i)
        lst.append(0)
        n -= 1
        continue
print(lst)


# alternative solution

# lst[:] = [x for x in lst if x != 0] + [0] * lst.count(0)
# print(lst)