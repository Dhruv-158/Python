# class Person:
#   name = "Harry"
#   occupation = "Software Developer"
#   networth = 10
#   def info(self):
#     print(f"{self.name} is a {self.occupation}")


# a = Person()
# b = Person()
# c = Person()

# a.name = "Shubham"
# a.occupation = "Accountant"

# b.name = "Nitika"
# b.occupation = "HR"

# # print(a.name, a.occupation)
# a.info()
# b.info()
# c.info()

class animal:
    def __init__(self,n,N):
        self.animalname = n
        self.name = N
    
    def info(self):
        print(f"it is a {self.animalname} his name is {self.name}")       
   
a = animal("Dog","tomy")
b = animal("Cat","citty")
print(a,b)    

a.info()  
b.info()

