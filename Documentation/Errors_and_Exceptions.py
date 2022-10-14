#Syntax error--compile time error
#exception--run time error

# try:
#     x=int(input("Please enter a number: "))
#     y=x/0

# except ValueError as val:
#     print("Value error!!") #user defined
#     print(val) #python given
# except ZeroDivisionError as zero:
#     print("Cannot divide by zero")
#     print(zero)
# except Exception as err:
#     print(err)
# finally:
#     print("Hey!!!") #finally is executed in any condition

# print("Bimochan")
#we can use else in try except block too
#If an exception occurs during 
# execution of the try clause, 
# the rest of the clause is skipped. 
# Then, if its type matches the 
# exception named after the except 
# keyword, the except clause is 
# executed, and then execution 
# continues after the try/except block.

#if we don't use try except, the flow of program will be completely disrupted 
#using them will not affect the code that follows the exception.

# try:
#     raise ZeroDivisionError("Divided by zero")
# except Exception as e:
#     print(e)


    