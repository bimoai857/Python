lst=["apple","pineapple","banana","mango"]

#----------List---append,extend,insert,remove,pop,clear,index,
# count,sort,sorted,reverse,copy,del----------------------

#list are mutable i.e their content can be changed after
#they are declared and assigned values, the can be indexed


# lst.append("Guava")# appends at the end of the list.
# print(lst)

# lst.append(["pineapple"])
# print(lst)

# lst.extend("Jack fruit")#iterates through the 
# #data type and appends to the end of the list
# print(lst)

# lst.extend(["grapes"])
# print(lst)

# lst.insert(0,"Cardamom")
# print(lst)

# lst.remove("Cardamom")
# print(lst)

# lst.pop()
# print(lst)

# lst.pop(1)
# print(lst)

# lst.clear()
# print(lst)

# a=lst.index("mango")
# print(a)

# b=lst.count("mango")
# print(b)

# lst.sort()
# print(lst)

# c=sorted(lst)
# print(c)

# lst.reverse()
# print(lst)

# d=lst.copy()
# print(d)

# del lst[0]
# print(lst)

# del lst[0:2]
# print(lst)

# del lst
# print(lst)


#------------using list as stack and queue------------

#we can use list a a stack using append and pop

# from collections import deque

# queue=deque(["Eric","John","Michael"])
# queue.append("Terry")#Terry arrives
# queue.append("Graham")#Graham arrives

# a=queue.popleft()
# print(a)
# print(queue)

#---------------List Comprenhensions------------------

# squares=list(map(lambda x: x**2,range(10)))
# print(squares)

# squares=[i**2 for i in range(10)]
# print(squares)

# friends=["Kushal "," Samyog "]
# new_friends=[friend.strip() for friend in friends]
# print(new_friends)

# numbers=[(i,j)for i in [1,2,3,4,5] for j in [3,4,5,6] if i!=j]
# print(numbers)

# numbers=[0,1,2,3]
# friends=["Kushal","Anurag","Yogesh"]
# tup=list(zip(numbers,friends))
# #zip returns an iterator of tuples
# print(tup)

#-------------------------------Tuples-----------

#tuples are non mutable but can be indexed
#tuples can contain collection of mutable types like list
#they can be accessed via unpacking or via indexing
# tupless=('Bimochan',)
# print(tupless)

# tupless1='Bimochan',
# print(tupless1)

# tupless2='Bimochan','Shrestha',101 #tuples packing

# tup1,tup2,tup3=tupless2#tuples unpacking

# print(tup1,tup2,tup3)


#--------------------Set------------------------------

#set are unindexable because they are unordered,immutable
#and doesnot allow duplicate entry
#union,intersection,difference,symmetrical difference

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)  

# print('orange' in basket) #membership testing

# a=set("Bimochan")
# b=set("Shrestha")

# print(a)
# print(b)

# print(a-b)
# print(a|b)
# print(a&b)

#similar to list comprehension, set comprehension is also allowed

#---------------------Dictionary------------------------------

#dictionary is a data structure that contains collection of key value pairs
#they are mutable
#tuples can be used as keys if they do not contable mutable objects like list
#{} is used for empty dictionary not empty set

# tel = {'jack': 4098, 'sape': 4139}
# tel['guido']=4127
# print(tel)

# del tel['jack']

# print(tel)

# print(list(tel))

# print('sape' in tel)


# a=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(a)

#similar to list comprehension dictionary comprehension can also be used

# d={a:a**2 for a in (range(10)) }#(range(10)) is an iteraor tuple
# print(d)

#if the keys are simple strngs then

# d=dict(sape=4139, guido=4127, jack=4098)
# print(d)

#----------------Looping techniques----------------

# lst={1:"Bimochan",2:"Kushal",3:"Anurag"}
# for a,b in lst.items():
#     print(a,b)

# for a,b in enumerate(['tic','tac','toe']):
#     print(a,b)

# questions=["What's your name","What's your age"]
# answers=["BImochan",25]

# for i,j in zip(questions,answers):
#     print(i,j)

# for i in reversed(range(1, 10, 2)):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)



# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)): #removing duplicates
#     print(f)


# for i in {1:"Bimochan",2:"Shrestha"}:
#     print(i)

#------------split-----

#split splits a string based on the argument 
#provided and returns a list.

# name="Bimochan Shrestha"
# print(name.split(" "))
