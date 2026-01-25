def second_index(text, some_str):
    first_match = text.find(some_str)
    if first_match == -1:
        return None
    second_match = text.find(some_str, first_match + 1)
    if second_match == -1:
        return None
    return second_match

assert second_index("sims", "s") == 3, 'Test1' 
assert second_index("find the river", "e") == 12, 'Test2' 
assert second_index("hi", "h") is None, 'Test3' 
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

