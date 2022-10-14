# #Single inheritance

# class A:
#     def __init__(self,name,major):
#         self.name=name
#         self.major=major
    
# class B(A):
#     def __init__(self,name,major,gpa,roll):
#         A.__init__(self,name,major)
#         self.gpa=gpa
#         self.roll=roll

#     def details(self):
#         print(self.name)
#         print(self.major)
#         print(self.gpa)
#         print(self.roll)

# b=B("Bimochan","CompSci",3.2,317)
# b.details()


# #Multiple inheritance

# class A:
  
#     def __init__(self,name,major):
#         self.name=name
#         self.major=major
    
# class B:

#     def __init__(self,gpa,roll):
#         self.gpa=gpa
#         self.roll=roll
    
# class C(A,B):

#     def __init__(self, name, major,gpa,roll):
#         A.__init__(self,name,major)
#         B.__init__(self,gpa,roll)

#     def details(self):
#         print(self.name)
#         print(self.major)
#         print(self.gpa)
#         print(self.roll)

# c=C("Kushal","IT",3.3,1234)
# c.details()

# #hierarchical inheritance

# class A:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll

    
# class A1(A):
#     def __init__(self, name, roll,gpa):
#         A.__init__(self,name,roll)
#         self.gpa=gpa

#     def details(self):
#         print(self.name)
#         print(self.roll)
#         print(self.gpa)

# class A2(A):
#     def __init__(self, name, roll,major):
#         A.__init__(self,name,roll)
#         self.major=major

#     def details(self):
#         print(self.name)
#         print(self.roll)
#         print(self.major)    

# class A3(A):
#     def __init__(self, name, roll,hobby):
#         A.__init__(self,name,roll)
#         self.hobby=hobby

#     def details(self):
#         print(self.name)
#         print(self.roll)
#         print(self.hobby)

# a1=A1("Bimochan",317,3.2)
# a1.details()

# a2=A2("Bimochan",317,"CompSci")
# a2.details()

# a3=A3("Bimochan",317,"Cricket")
# a3.details()

# # #Multilevel inheritance


# class A:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll

# class B(A):
#     def __init__(self,name,roll,major,gpa):
#         A.__init__(self,name,roll)
#         self.major=major
#         self.gpa=gpa

# class C(B):
#     def __init__(self,name,roll,major,gpa,hobby):
#         B.__init__(self,name,roll,major,gpa)
#         self.hobby=hobby

#     def details(self):
#         print(self.name)
#         print(self.roll)
#         print(self.major)
#         print(self.gpa)
#         print(self.hobby)

# c=C("Bimochan",317,"CompSci",3.2,"Cricket")
# c.details()


# #hybrid inheritance


# class A:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll

# class B(A):
#     def __init__(self,name,roll,major,gpa):
#         A.__init__(self,name,roll)
#         self.major=major
#         self.gpa=gpa

# class C(B):
#     def __init__(self,name,roll,major,gpa,hobby):
#         B.__init__(self,name,roll,major,gpa)
#         self.hobby=hobby

#     def details(self):
#         print(self.name)
#         print(self.roll)
#         print(self.major)
#         print(self.gpa)
#         print(self.hobby)

# class D(B):
#     def __init__(self,name,roll,major,gpa,address):
#         B.__init__(self,name,roll,major,gpa)
#         self.address=address

#     def details(self):
#             print(self.name)
#             print(self.roll)
#             print(self.major)
#             print(self.gpa)
#             print(self.address)

# c=C("Bimochan",317,"CompSci",3.2,"Cricket")
# d=D("Kushal",318,"IT",3.6,"Football")
# c.details()
# d.details()











        
        