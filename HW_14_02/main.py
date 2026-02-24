from student import Student
from group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 30, 'Steve', 'Jobs', 'AN142') 

assert st1 == st3
assert st1 != st2

assert hash(st1) == hash(st3)
assert hash(st1) != hash(st2)
assert (st1 == "Some String") is False

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')

assert gr.find_student('Taylor') is None
assert gr.find_student('Jobs') == st1

print(gr)  

assert len(gr.group) == 1

