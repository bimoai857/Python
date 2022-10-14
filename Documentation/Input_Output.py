# #-----Formatting output---------------

# #using formatted string literals

# year=2016.000
# event="Referendum"
# print(f'Result of the {year:.2f} {event}')


# #using str.format()

# a=25.333
# b=26.999
# print("{:.2f} {:.2f}".format(a,b))

# print('{0} and {1}'.format('spam', 'eggs'))

# print('{1} and {0}'.format('spam', 'eggs'))

# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

# #old string format

# import math
# print('The value of pi is approximately %.3f.' % math.pi)


#-----------------File handling----------------------

# with open("text.txt","r+") as f:
#     f_contents=f.readlines()

#     f_contents_new=[]
#     for i in f_contents:
#         f_contents_new.append(i.replace("\n",""))

#     number_1=int((len(f_contents)-1)/2)
#     number_2=number_1+2
#     for i in range(number_1):
#         f.write(str("\n"+f_contents_new[i]+" "+f_contents_new[number_2-1]))
#         number_2+=1

#--------Different modes-------------

# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.

#------read operation----------

# f=open('text.txt','r') #f is a pointer that points to first character of first line

# print(f.read())#simply reads the content

# print(f.readline())#simply reads the first line

# print(f.readlines())#creates list of strings from the contents

# f.close()

#--------write operation--------------

# f=open('text.txt','w')
# f.write("My name is Bimochan Shrestha")
# f.writelines(["\nBimochan\n","Shrestha"])
# f.close

#----------reading and writing------

# with open('text.txt','a+') as f:
#     f.write("\n I did my graduation in CompSci")
#     print(f.tell())#returns the current position of file pointer
#     f.seek(0) #moving the pointer to the beginning of a file
#     print(f.read())

#No need to close when you open a file using 'with' keyword
