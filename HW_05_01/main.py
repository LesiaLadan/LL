# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True



import keyword

x = input('Enter a string to check if it valid for variable name: \n')

var_ok = (
    x 
    and not x[0].isdigit()
    and x not in keyword.kwlist
    and not (x.count('_') == len(x) and len(x) > 1)
    and " " not in x
    and all(c.islower() or c.isdigit() or c == "_" for c in x)
)

print(var_ok)
