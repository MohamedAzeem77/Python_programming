def replaceSpacewithCharacters(string,ch):
    text=" "
    for r in string:
        if r==' ':
            text=text+ch
        else:
            text=text+r

    return text

print(replaceSpacewithCharacters('h llo v ryon ','e'))



def leftRotate(li,po):
    return li[po:]+li[:po]

print(leftRotate([1,2,3,4,5],2))


def RightRotate(li,po):
    return li[-po:]+li[:-po]

print(RightRotate([1,2,3,4,5],2))



def arrowProgram(n):

    for i in range(0,n):
        print('*'*i)

    for j in range(n,0,-1):
        print("*"*j)


    for k in range(0,n):
        print(" "*(n-k)+"*"*k)

    for l in range(n,0,-1):
        print(" "*(n-l)+"*"*l)


    for r in range(0,n):
        print(" "*(n-r)+"*"*(2*r-1))

    for s in range(n,0,-1):
        print(" "*(n-s)+"*"*(2*s-1))

arrowProgram(5)



def swapping(a,b):
    temp=a
    a=b
    b=temp
    return f"a = {a} || b = {b} "

print(swapping(1,0))


def primeBetweennumbers(num):
    for g in range(0,num):
        if g>1:
            for i in range(2,g):
                if g%i==0:
                    break
            else:
                print(g,end=" ")


primeBetweennumbers(99)

print()



def findEvenNumbers(func):
    def inner(li):
        res=func(li)
        return res
    return inner

@findEvenNumbers
def func(li):
    for w in li:
        if w%2==0:
            print(w,end=" ")
        

func([f for f in range(1,20)])



def findSecondlarest(li):
    max=li[0]
    sec=li[0]
    for t in range(len(li)):
        if li[t]>max:
            sec=max
            max=li[t]
        elif li[t]>sec:
            sec=li[t]

    return sec

print(findSecondlarest([1,2,3,4,5,6,7]))