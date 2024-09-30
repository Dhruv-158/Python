
#<------------------------------------------------------------------Inheritance----------------------------------------------------------------->

# class employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
        
#     def showDetails(self):
#         print(f"The name of employee : {self.id} is {self.name}\ni am empoly in this company")
        
# e = employee("dhruvik",124)
# e.showDetails()

# class Programer(employee):
#     def info(self):
#         print("i am a python devloper")

# p = Programer("dhruvik",124)
# p.showDetails()
# p.info()


#<----------------------------------------------------------------#Single Inheritance-------------------------------------------------------->

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!")
# print("\n")

# d = Dog("Dog", "Doggerman")
# d.make_sound()

# print("\n")

# a = Animal("Dog", "Dog")
# a.make_sound() 

# class Cat(Animal):
    
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Cat")
#         self.breed = breed 
#         self.name = name
    
#     def make_sound(self):
#         print(f"{self.name} which breed is {self.breed} and it said meows.")

# print("\n")       
# c = Cat("tom","British Shorthair")
# c.make_sound()

#<----------------------------------------------------------------#Multiple Inheritance-------------------------------------------------------->


# class Employee:
#   def __init__(self, name):
#     self.name = name
#   def show(self):
#     print(f"The name is {self.name}")

# class Dancer:
#   def __init__(self, dance):
#     self.dance = dance

#   def show(self):
#     print(f"The dance is {self.dance}")

# class DancerEmployee(Employee, Dancer):
#   def __init__(self, dance, name):
#     self.dance = dance
#     self.name = name

# o  = DancerEmployee("Kathak", "Shivani")
# print(o.name)
# print(o.dance)
# o.show() 
# print(DancerEmployee.mro())
# method resolution order

# <----------------------------------------------------------------Multilevel Inheritance------------------------------------------------------->

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
        
# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Breed: {self.breed}")
        
# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retriever")
#         self.color = color
        
#     def show_details(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")

# o = Dog("tommy", "Black")
# o.show_details()
# print(GoldenRetriever.mro())

# <----------------------------------------------------------------Hybrid Inheritance -------------------------------------------------------->

# class BaseClass:
#   pass

# class Derived1(BaseClass):
#   pass  

# class Derived2(BaseClass):
#   pass  

# class Derived3(Derived1, Derived2):
#   pass

#<----------------------------------------------------------------#Hierarchical Inheritance-------------------------------------------------------->

# class BaseClass:
#   pass

# class D1(BaseClass):
#   pass

# class D2(BaseClass):
#   pass

# class D3(D1):
#   pass

#<----------------------------------------------------------------------Access Modifiers------------------------------------------------------->

#<----------------------------------------------------------------------Public------------------------------------------------------->


# class Student:
#     # constructor is defined
#     def __init__(self, age, name):
#         self.age = age               # public variable
#         self.name = name             # public variable

# obj = Student(21,"Harry")
# print(obj.age)
# print(obj.name)

#<----------------------------------------------------------------------Private------------------------------------------------------->

# class Student: 
#     def __init__(self, age, name): 
#         self.__age = age      # An indication of private variable
        
#         def __funName(self):  # An indication of private function
#             self.y = 34
#             print(self.y)

# class Subject(Student):
#     pass

# obj = Student(21,"Harry")
# obj1 = Subject

# # calling by object of class Student
# print(obj.__age)
# print(obj.__funName())

# # calling by object  of class Subject
# print(obj1.__age)
# print(obj1.__funName())

#<----------------------------------------------------------------------Protected------------------------------------------------------->

# class Student:
#     def __init__(self):
#         self._name = "Harry"

#     def _funName(self):      # protected method
#         return "CodeWithHarry"

# class Subject(Student):       #inherited class
#     pass

# obj = Student()
# obj1 = Subject()

# # calling by object of Student class
# print(obj._name)      
# print(obj._funName())     
# # calling by object of Subject class
# print(obj1._name)    
# print(obj1._funName())