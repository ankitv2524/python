class Student:
    '''This class is Developed for demo purpose'''
#print(Student.__doc__)
    def __init__ (self):
        print(id(self))

s = Student()
print(id(s))

s2 = Student()
print(id(s2))