lst = [0, 1, 7, 2, 4, 8]
# lst = [1, 3, 5]
# lst = [6]
# lst =[]
# lst = [9, 7, 96, 0]

# if not lst:
#     result = 0
#     print (result) 
# else:
#     result = sum([x for i, x in enumerate(lst) if i % 2 == 0]) * lst[-1]
#     print (result)

# # Alternative solution

# if not lst:
#     result = 0
#     print (result) 
# else:
#     result = sum([x for x in lst[::2]]) * lst[-1]
#     print (result)
number = 0
while number <= 10:
    number = number + 2
    if number == 5:
        break 
    print(number, end=', ')