#a= 4
#b=3
#c =a//b
#print(c)

class Student:
    '''This class is developed by Durga Sir'''

    def __init__(self,rollno,name):
       self.rollno=rollno
       self.name=name
    def talk(self):
       print("hello My Name is:", self.name)
       print("My Rollno is:", self.rollno)

s = Student(100,'Ankit')
print(s.name)
print(s.rollno)
s.talk()

s1 = Student(150,'Aditi')
print(s.name)
print(s.rollno)
s1.talk()

s2 = Student(130,'Abhishek')
print(s.name)
print(s.rollno)
s2.talk()

s3 = Student(140,'Ankita')
print(s.name)
print(s.rollno)
s3.talk()



