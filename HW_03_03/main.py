lst = []
# lst = [1]
# lst = [1, 2, 3, 4]
# lst = [1, 2, 3]
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = len(lst)

if not lst:
    new_list = [[], []]
else:
    mid_ind = (n + 1) // 2
    new_list = [lst[:mid_ind], lst[mid_ind:]]

print(new_list)
