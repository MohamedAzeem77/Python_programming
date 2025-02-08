def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
print(f"The factorial of {5} is : {fact(5)}")



def fibo(n,count):
    n1=0
    n2=1
    while count<n:
        print(n1,end=" ")
        n1,n2=n2,n1+n2
        count+=1
    
fibo(11,0)


def leapyear(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        print(f"{n} is a leap year")
    else:
        print(f"{n} is not a leap year")


leapyear(2027)



def palindrome(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
    
n=124
sol=palindrome(n)

if sol==n:
    print("palindrome number")
else:
    print("not a palindrome number")


def palindromeString(text):
    string=""
    for t in text:
        string=t+string
    return string

text="malayalams"
ans=palindromeString(text)

if text==ans:
    print("palindrome string")
else:
    print("not a palindrome string")



def check_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

if check_prime(16):
    print("prime number")
else:
    print("not a prime number")



def findfrequency(li):
    ma={}
    for t in li:
        if t in ma:
            ma[t]+=1
        else:
            ma[t]=1

    return ma

print(findfrequency([1,1,2,3,5,3,7,8,9,4,3]))



def findduplicates(li):
    ma={}
    le=[]
    for t in li:
        if t in ma:
            ma[t]+=1
            if ma[t]==2:
                le.append(t)
        else:
            ma[t]=1

    return le

print(findduplicates([2,3,4,5,6,7,1,2,3,9,2,3,1]))


def removeduplicates(li):
    ma={}
    lr=[]
    for t in li:
        if t in ma:
            ma[t]+=1
        else:
            ma[t]=1
            lr.append(t)

    return lr

print(removeduplicates([1,4,5,6,7,2,3,4,1,9,5,7,3,4]))


def replaceSpaceWithCharacter(text,ch):
    string=" "
   
    for t in text:
        if t == " ":
            string=string+ch
        else:
            string=string+t
    
    return string

print(replaceSpaceWithCharacter("H ppy ge",'a'))



def leftRotate(li,po):
    return li[po:]+li[:po]


print(leftRotate([1,2,3,4,5],2))


def Rightrotate(li,po):
    return li[-po:]+li[:-po]

print(Rightrotate([1,2,3,4,5],2))



def StarPattern(n):

    for t in range(0,n):
        print('*'*t)

    for s in range(n,0,-1):
        print('*'*s)

    for u in range(0,n):
        print(' '*(n-u)+'*'*u)

    for v in range(n,0,-1):
        print(' '*(n-v)+'*'*v)

    
    for e in range(0,n):
        print(" "*(n-e)+"*"*(2*e-1))

    for d in range(n,0,-1):
        print(" "*(n-d)+"*"*(2*d-1))

StarPattern(5)



l=lambda s:s*5
print(l(5))


l1=list(map(lambda d:d,[1,2,3,4,5,6,7,8,8]))
print(l1)

l2=list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10]))
print(l2)

from functools import reduce

l3=reduce(lambda d,t:d+t,[1,2,3,4,5,6,7,8])
print(l3)


class FibonacciSeries:
    def __init__(self,a=0,b=1,count=0,n=11):
        self.a=a
        self.b=b
        self.count=count
        self.n=n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count<self.n:
            cu=self.a
            self.a,self.b=self.b,self.a+self.b
            self.count+=1
            return cu
        else:
            raise StopIteration
    
iterator=FibonacciSeries()

for t in iterator:
    print(t,end=" ")