import pickle
import copyreg


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.dummy = 'dummy'  # dummy 속성을 신규로 추가한다!!


def pickle_student(student):
    kwargs = student.__dict__
    return unpickle_student, (kwargs, )


def unpickle_student(kwargs):
    return Student(**kwargs)


copyreg.pickle(Student, pickle_student)

with open('student.p', 'rb') as f:
    student = pickle.load(f)  # unpickle_student 함수가 호출된다.

print(student.dummy)  # 오류가 발생하지 않고 'dummy' 가 출력된다.
