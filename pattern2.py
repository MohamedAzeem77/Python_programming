n=5


for i in range(1,n):
    print("*"*i)

for i in range(n,0,-1):
    print("*"*i)



for i in range(1,n):
    print(" "*(n-i)+"*"*i)

for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i)

print()

for i in range(1,n):
    print(" "*(n-i)+"*"*(2*i-1))

for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))