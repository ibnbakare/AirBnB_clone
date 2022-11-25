class employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def full_name(self):
        print(self.first_name + " " + self.last_name)
        
    def __str__(self):
        return 'employee("{}", "{}", {})'.format(self.first_name, self.last_name, type(self).__name__)
    
    def __class__(cls):
        return "<class '{}'>".format(type(cls).__name__)
    
    # def __repr__(self):
    #     return self.first_name + " " + self.last_name
        
class ganitor(employee):
    def __init__(self, first_name, last_name, pay):
        super().__init__(first_name, last_name)
        self.pay = pay
        

emp_1 = employee("Abiodun", "Shittu")
emp_2 = employee("Ridhwan", "Bakare")
gan_1 = ganitor("John", "Doe", 40000)
print(emp_1)
print(emp_2)

print(emp_1.first_name)
print(emp_2.last_name)
print(gan_1.pay)

emp_1.full_name()
gan_1.full_name()

emp_4 = emp_1.__dict__
emp_4["__class__"] = emp_1.__class__.__name__
print(emp_4)

