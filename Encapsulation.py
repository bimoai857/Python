class A:
    def __init__(self):
        self._name="Bimochan Shrestha"  #name is protected(This can be accessed by the member function or the derived class's member function)
        self.age=25 #public variables can be accessed by anyone through the object.
        self.__major="CompSci"#private variables cannot be accessed outside of a class and can be accesed by only the member function.
    
    def p(self):
        print(self.__major)

class B(A):
    def __init__(self):
        A.__init__(self)

    def prt(self):
        print(self.age)
        print(self._name)

    

b=B()
b.prt()
a=A()
a.p()