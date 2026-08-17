#    ...............     OOPS (Classes and Objects)     ................   #1,2
# Class (blueprint of object)
# class Student:
#     sub= 'python'
#     colg='govt college'
#     year='4th'

# # Objects of the class
# stu1=Student()
# stu2=Student()
# stu3=Student()

# print(stu1.sub, stu1.year)
# print(stu2.sub, stu2.colg)

# .................      Constructor init Method          ........................  #4

# class Student:
#     def __init__(self, name,age):
#         self.name=name
#         self.age=age

# stu1=Student('Hamza', 25)
# print(stu1.name, stu1.age)
# stu2=Student('tom', 45)
# print(stu2.name,stu2.age)


#    .........     #5
# class Student:
#     def __init__(self, name,age):
#         self.name=name
#         self.age=age
#     def get_age(self):       # instance methods 
#         return self.age

# stu1=Student('Hamza', 25)
# print(f'{stu1.name} has age of {stu1.get_age()}')


#     ..............     Attributes(class and instance)  ................. #6
# class stu:
#     college='govt college'     # class attributes

#     def __init__(self,name, age):
#         self.name= name           # instance attributes
#         self.age=age

# stud1=stu('hamza',27)
# print(stud1.name,stud1.college, stu.college)  # last 2 give same answer 

#    ..............      Methods (Instance , Class, Static Method)...............   #7,8,9

# class Laptop:
#     storage='ssd'

#     def __init__(self, name, ram):
#         self.name=name
#         self.ram=ram

#     @classmethod            # class method
#     def get(cls):   # class method use cls parameter
#         print(f'the storage of class Laptop is {cls.storage}')   

#     @staticmethod             # Static method 
#     def cal(price, discount):
#         f_price=price-(discount*price/100)
#         print(f_price)

#     def get_info(self):
#         print(f'the name is {self.name} and ram is {self.ram} which is {self.storage}')

# lap1=Laptop('lenovo', '256gb')
# lap1.get_info()
# lap2=Laptop('dell', '512ssd')
# # print(lap2.name, lap2.ram)
# lap2.get_info()


# lap1=Laptop('lenovo', '256gb')
# # Laptop.get()    # or
# # lap1.get()     # both give us the same answer

# Laptop.cal(4000, 20)


#    ...................    problem for all previous concepts  . .............  #10
# class product:
#     count=0

#     def __init__(self, name, price):
#         self.name=name
#         self.price=price
#         product.count+=1

#     def get_info(self):
#         print(f'the product name is {self.name} and price is Rs.{self.price}')

#     @classmethod
#     def coun(cls):          # it will tell us how much object we created
#         print(f'the nmber of object created is {cls.count}')

# p1=product('mobile', 10000)
# p2=product('laptop', 50000)

# p1.get_info()
# product.coun()


#   ..............     oops pillars  (1. Encapsulation)    ..............    #11

# class Bank:
#     def __init__(self,name, balance):
#         self.name=name
#         self._bal=balance      # this is the protected data
#         self.__balance= balance     # private data

#     def get(self):     # it can give us the private value of balance
#         return self.__balance

#     def set(self, new_bal):     # it can set the new balance 
#         self.__balance=new_bal

# ac1=Bank('Hamza', 500000)
# print(ac1.get())
# ac1.set(7700000)
# print(ac1.get())


#     .................     2.Inheritance  .....................  #12
# class Employe:
#     s_time='10am'
#     e_time='5am'

# class teacher(Employe):
#     def __init__(self, name, subject):
#         self.name=name
#         self.subject=subject


# t1=teacher('Hamza', 'ML')
# print(t1.name,t1.subject,t1.s_time)


#     ...............    Type of Inheritance     ................   #13
# this is the example of multi layer inheritance
# class employe:
#     s_time='10am'
#     e_time='6pm'

# class admin(employe):
#     def __init__(self,role):
#         self.role=role

# class account(admin):
#     def __init__(self, salery, role):
#         super().__init__(role)
#         self.salery=salery

# ac1=account(40000,'manager')
# print(ac1.salery,ac1.role, ac1.s_time)

#  Multipe inheritance  
# class teacher:
#     def __init__(self,subject):
#         self.subject=subject

# class student():
#     def __init__(self,gpa):
#         self.gpa=gpa

# class teacher_assistant(teacher, student):
#     def __init__(self, subject, gpa, name):
#         super().__init__(subject)
#         student.__init__(self,gpa)
#         self.name=name

# ta1=teacher_assistant('machine learning', 3.23, 'Hamza')
# print(f'The name of student is {ta1.name} and his subject is {ta1.subject} got {ta1.gpa}gpa in it')


#     ................    Abstraction    ................   #14
# from abc import ABC, abstractmethod
# class animal(ABC):      # we create this abstract class just to use it in child classes
#     @abstractmethod   # ab animal class ko paata he ke ye neche abstract method he abstract method ka apne class me implementation nahi hota oska use child classes me hota he
#     def make_sound(self):     # this is function and esko ham neche parents me use karenge es leye pass kia he
#         pass 

# class lion(animal):
#     def make_sound(self):   # eska matlab he ke opar wale make sound ko ab implement karo yaha
#         print('roar')

# class cat(animal):
#     def make_sound(self):
#         print('meow')

# li=lion()
# li.make_sound()
# ca=cat()
# ca.make_sound()



#    ..............       Polymosrphism (ist type Function Overriding)  ............    #15

# class employe:
#     def get_data(self):
#         print('the designition is Employee')

# class teacher(employe):    
#     def get_data(self):
#         print('the designition is Teacher')   # here we do function overriding in this child class

# t1=teacher()
# t1.get_data()


#     ................     Polymorphism 2nd type Duck Typing   ............   #16
class employe:
    def get_data(self):
        print('the designition is Employee')

class teacher():    
    def get_data(self):        # dono function ka same sa kam he es leye esko duck typing kehte he
        print('the designition is Teacher')

e1=employe()
e1.get_data()

t1=teacher()
t1.get_data()