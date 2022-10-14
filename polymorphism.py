# #Duck Typing

# class Laptop:
#     def code(self,obj):
#         obj.execute()

# class Vscode:
#     def execute(self):
#         print("This is vscode!!")

# class Pycharm:
#     def execute(self):
#         print("This is pycharm!")

# vscode=Vscode()
# pycharm=Pycharm()

# laptop=Laptop()
# laptop.code(vscode)
# laptop.code(pycharm)


# # #Operator overloading

# # class A:
# #     def __init__(self,name):
# #         self.name=name

# #     def __add__(self,other):
# #         return self.name+other.name


# # a1=A("Bimochan ")
# # a2=A("Shrestha")

# # print(a1+a2)


# #Method overloading

# # class B:
# #     def add(self,a=None,b=None,c=None):
# #         if(a!=None and b!=None and c!=None):
# #             return a+b+c
# #         elif(a!=None and b!=None):
# #             return a+b
# #         elif(a!=None):
# #             return a
# #         else:
# #             return 0
        
# # b=B()
# # print(b.add(1,2,3))
# # print(b.add(2,3))
# # print(b.add(2))
# # print(b.add())

# #Method Overridding

# class A:
#     def execute(self):
#         print("This is A")

# class B(A):
#     pass

# class C(A):
#     def execute(self):
#         print("This is C")

# b=B()
# b.execute()
# c=C()
# c.execute()

    
