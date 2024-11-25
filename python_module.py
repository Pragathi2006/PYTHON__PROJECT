def abc():
    sum=0
    for i in range(5,11):
        sum=sum+i
    print(sum)
abc()
def xyz():
    even=0
    for i in range(5,11):
        if i%2==0:
            even=even+i
    return even
xyz()
def demo():
    odd=0
    for i in range(5,11):
        if i%2!=0 or i%2==1:
            odd=odd+i
    return odd
demo()
def factor(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print (fact)
factor(5)
def fib(n):
    a=0
    b=1
    for i in range(0,n):
        print(a,end=" ")
        a,b=b,a+b
fib(45)
def palindrome(n):
    if(n==n[::-1]):
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
n=input("enter the string:-")
print(palindrome(n))
def hcf(a,b):
    while b:
        a,b=b,a%b
    return a
hcf(36,60)
def maximum():
    x=int(input("enter the number"))
    y=int(input("enter the number"))
    z=int(input("enter the number"))
    if x>y and x>z:
        print("x is greater")
    elif y>x and y>z:
        print("y is greater")
    elif z>x and z>y:
        print("z is greater")
maximum()