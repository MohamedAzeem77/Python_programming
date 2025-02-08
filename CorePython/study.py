def fibo(myfunc):
    def inner(val):
        res=myfunc(val)
        return res
    return inner


@fibo
def myfunc(val):
    n1=0
    n2=1
    count=0
    while count<val:
        print(n1,end=" ")
        n1,n2=n2,n1+n2
        count+=1


myfunc(11)



li1=[x for x in range(2,10)]
print(li1)


se=lambda s:s**2
print(se(3))


def evenOrOdd(li):
    for t in li:
        if t%2==0:
            yield t


for r in evenOrOdd([1,2,3,4,5,6,7,8]):
    print(r,end=" ")
