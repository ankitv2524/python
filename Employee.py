class Employee:
    ''' Doc String Description'''
    def __init__ (self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr
    def info(self):
        print('Employee Number:', self.eno)
        print('Employee Name:', self.ename)
        print('Employee Salary:', self.esal)
        print('Employee Address:', self.eaddr)
        print('*'*20)

e1 = Employee(100, 'Ankit', 100000000, 'Ranchi')
e2 = Employee(120, 'Roshan', 12000, 'Banglore')
e3 = Employee(130, 'Chandan soni', 20000000, 'Singapore' )
print(e1.info()) 
print(e2.info())
print(e3.info())
