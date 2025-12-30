#lst = ['a', 'b', 'c', 'd', 'e']
#lst = [True,'a', 'b', 'c', 'd', ['q', 'w']]
#lst = [12, 3, 4, 10, 8]
#lst = []
lst = [1]


if len(lst) == 0:
    print()
    print(lst)
    print()
else:    
    x = lst.pop()
    lst.insert(0, x)
    print()
    print(lst)
    print()