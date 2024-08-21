#----------------Factorial-------------------------------------------
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
    
num=int(input("Enter num value : "))
print(f"The factorial of {num} is ",fact(num))

#---------------------Fibonacci series-------------------------------

def fibo(num1):
    n1,n2=0,1
    count=0
    while count<num1:
        print(n1,end=" ")
        n1,n2=n2,n1+n2
        count+=1
    
print(fibo(11))

#----------------------Palindrome num/reverse num---------------------

def palindrome_num(num):
    rev=0
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev

num=121
res=palindrome_num(num)

if num==res:
    print("It is palindrom number")
else:
    print("not a palindrome number")


#-------------------------------prime_number--------------------------

def check_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
        return True
    
if check_prime(67):
    print("It is a prime number")
else:
    print("Not a prime number")


#-----------------------------leap year---------------------------------

def check_leapyear(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

print(check_leapyear(2026))

#----------------------------Reverse a string/palindrome string----------

def reverse_string(str1):
    str2=""
    for t in str1:
        str2=t+str2
    
    return str2

str1="MalayalaM"
res=reverse_string(str1)

if str1==res:
    print("It is a palindrome string")
else:
    print("It is not a palindrome string")


#------------------------find frequency in list-------------------------

def find_frequency(li):
    ma={}

    for i in li:
        if i in ma:
            ma[i]+=1
        else:
            ma[i]=1

    return ma

print(find_frequency([1,2,1,7,9,4,9,3,6,2,5]))


#------------------------find duplicates----------------------------------

def find_duplicates(li):
    ma={}
    l=[]


    for t in li:
        if t in ma:
            ma[t]+=1
            if ma[t]==2:
                l.append(t)
        else:
            ma[t]=1
    return l

print(find_duplicates([1,6,8,3,2,5,1,8,5,2,9,2]))

#------------------------remove_duplicates---------------------------------

def remove_duplicates(li):
    ma={}
    lk=[]

    for d in li:
        if d in ma:
            ma[d]+=1
        else:
            ma[d]=1
            lk.append(d)
    return lk

print(remove_duplicates([1,4,7,2,5,3,8,4,6,2,1,9]))


#-------------------------Decorators-----------------------------------------

def decorator_program(find_duplicates):
    def wrapper(li):
        res=find_duplicates(li)
        return res
    return wrapper

@decorator_program
def find_duplicates(li):
    ma={}
    fr=[]
    for t in li:
        if t in ma:
            ma[t]+=1
            if ma[t]==2:
                fr.append(t)
        else:
            ma[t]=1
    return fr

print(find_duplicates([1,2,4,7,9,32,17,1,2,4,6,5]))

#---------------------------Generator------------------------------------

def fibo(num):
    i,j=0,1
    count=0
    while count<num:
        yield i
        i,j=j,i+j
        count+=1

for t in fibo(11):
    print(t,end=" ")

#--------------------------map,filter,reduce----------------------------------------

la=list(map(lambda f:f**3,[f for f in range(1,7)]))
print(la)

de=list(filter(lambda v:v,[r for r in range(1,11) if r%2==0]))
print(de)


from functools import reduce
from typing import Any
ew=reduce(lambda c,d:c+d,[s for s in range(1,11) if s%2!=0])
print(ew)

#--------------------------lambda-----------------------------------------------------

rt=lambda f:f**5
print(rt(2))

#-------------------------list/set/dict/tuple comprehension---------------------------

li=[o for o in range(2,10) if o%2==0]
print(li)


se=(g for g in range(2,10) if g%2==0)
print(tuple(se))


di={r for r in range(2,100,15) if r%2==0}
print(di)

er={l:h for l,h in enumerate(range(3,30)) if l%3==0}
print(er)


#---------------------------iterator---------------------------------------------------

class program_for_iterator:
    def __init__(self,n1=0,n2=1,num=11):
        self.n1=n1
        self.n2=n2
        self.num=num
        self.count=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count<self.num:
            cu=self.n1
            self.n1,self.n2=self.n2,self.n1+self.n2
            self.count+=1
            return cu
        else:
            raise StopIteration
        

iterator=program_for_iterator(num=10)
for value in iterator:
    print(value,end=" ")


#-------------------------------Inheritance------------------------------------------

class Father:
    def __init__(self,father_name,property):
        self.father_name=father_name
        self.property=property

    def show(self):
        return f"I am {self.father_name} owning {self.property}"
    

    
class Son(Father):
    def __init__(self, father_name, property,my_name):
        super().__init__(father_name, property)
        self.my_name=my_name

    def show(self):
        return f"I am {self.my_name} , and my father is {self.father_name} who owns {self.property} "


s=Son("Ajay","100 acres","Deepak")

print(s.show())


#---------------------------------Abstraction------------------------------------------------

from abc import ABC,abstractmethod

class automobile(ABC):

    @abstractmethod
    def show_axle(self):
        pass

    @abstractmethod
    def display(self):
        pass


class Car(automobile):

    def show_axle(self):
        print("I am having two axle")

    def display(self):
        print("I am in blue colour......")


c=Car()
c.display()
c.show_axle()



#--------------------------------------encapsulation----------------------------

class maths_calculation():
    def __init__(self,a,b):
        self.__a=a
        self._b=b


    def __repr__(self):
        return f"{self.__a} & {self._b}"
    

class child_for_maths(maths_calculation):
    def __init__(self, a, b):
        super().__init__(a, b)

    
    def get_a(self):
        return self._maths_calculation__a
    
    def set_b(self,value):
        self._maths_calculation__a=21
        


c=child_for_maths(15,2)

print(c._b)
print(c.get_a())

        

#-----------------------------------------polymorphism with Functions & objects-------------------------------------------------------

class Fruit():
    def colour(self):
        print("It is fruit color")

    def taste(self):
        print("It is a tasty fruit")



class Vegetable():
    def colour(self):
        print("It is vegetable color")

    def taste(self):
        print("It is a tasty vegetable")





def myfunc(obj):
    obj.colour()
    obj.taste()


f=Fruit()
myfunc(f)

v=Vegetable()
myfunc(v)

#------------------------>polymorphism with class & methods---------------------

class Fruit():
    def colour(self):
        print("It is fruit color")

    def taste(self):
        print("It is a tasty fruit")



class Vegetable():
    def colour(self):
        print("It is vegetable color")

    def taste(self):
        print("It is a tasty vegetable")


o1=Fruit()
o2=Vegetable()


for t in (o1,o2):
    t.colour()
    t.taste()




#-------------------------polymorphism with inheritance / method overriding--------------------

class Bird:
  def intro(self):
    print("There are many types of birds.")
    
  def flight(self):
    print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
    
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
    
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

    

        


