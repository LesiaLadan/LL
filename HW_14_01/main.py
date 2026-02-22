class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}\nGender: {self.gender}\nAge: {self.age}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}\nGender: {self.gender}\nAge: {self.age}\nRecord book: {self.record_book}"

class GroupLimitError(Exception):
    pass

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError(f"Group size limit exceeded – cannot add student {student.first_name} {student.last_name}")
        else:
            self.group.add(student)
            
    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
    
    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n\n".join(str(student) for student in self.group)
        return f'\nNumber: {self.number}\n\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Smith', 'AN146')
st4 = Student('Female', 28, 'Emma', 'Brown', 'AN147')
st5 = Student('Male', 21, 'Michael', 'Johnson', 'AN148')
st6 = Student('Female', 24, 'Olivia', 'Davis', 'AN149')
st7 = Student('Male', 23, 'David', 'Wilson', 'AN150')
st8 = Student('Female', 26, 'Sophia', 'Moore', 'AN151')
st9 = Student('Male', 29, 'Jack', 'Black', 'AN152')
st10 = Student('Female', 27, 'Isabella', 'Anderson', 'AN153')
st11 = Student('Male', 31, 'Jack', 'White', 'AN154')
st12 = Student('Female', 22, 'Mia', 'Jackson', 'AN155')

gr = Group('PD1')

students = [
    st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11, st12
]

for every in students:
    try:
        gr.add_student(every)
        print(f"Number of students: {len(gr.group)}")
    except GroupLimitError as e:
        print(e)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'
gr.delete_student('Taylor')
print("\n*** After deletion ***")
print(f"Number of students: {len(gr.group)}")  
print("\n*** After deleting the same student by last_name ***")
gr.delete_student('Taylor') 
print(f"Number of students: {len(gr.group)}")