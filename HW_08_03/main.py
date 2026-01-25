def find_unique_value(some_list): 
    for i in some_list:
        counter = 0
        for j in some_list:
            if i == j:
                counter += 1
        if counter == 1:
            return i        


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1' 
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2' 
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3' 
assert find_unique_value([1, 5, 5, 5, 2, 2, 0.5]) == 1, 'Test3' 

print("ОК")
