#--------------non-local,global------------

# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)

#------------------------------
# class Employee:
#     pass

# john=Employee()

# john.name="JOhn Doe"
# john.dep="Computer lab"
# john.salary=1000

# print('{} {} {}'.format(john.name,john.dep,john.salary))
#------------------------------------


#---------------Iterators----------

#'for statement' calls iter() on the list,tuple or string
#and so we get and iterator

#but if there is no for we have to 
#manually call iter() method and access 
#them using next()

# lst=[1,2,3,4,5,6,7,8,9,10]
# ite=iter(lst)
# print(next(ite))
# print(next(ite))

# def reverse(data):
#     for index in range(len(data)-1,-1,-1):
#         yield data[index]

# for char in reverse("Bimochan"):
#     print(char)