def numberReverse(n):
    rev=0
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
rev= numberReverse(123856)
print("Reverse is;",rev)

def myFunction(*name):
    l=len(name)
    for i in range(l):
        print(name[i])
myFunction("RAM","SHAM")
myFunction("RAM","SHAM","RITIK")
myFunction("RAM","SHAM","DIM","JHDJFK")
from functools import reduce
def product(x,y):
    return x*y
ans=reduce(product,[2,3,4,67,8879])
print(ans)

class myclass:
    x=5
p1=myclass()
print(p1.x)
class sarita:
    x=24
b1=sarita()
print(b1.x)


class student:
    def __init__ (self,rollno,name):
     self.rollno = rollno
     self.name = name
s1=student(1,"sarita")
s2=student(2,"sid")
s3=student(3,"ritik")
print(s1.rollno)
print(s2.name)
print(s3.name,s3.rollno)

class cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self) :
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

a=int(input("enter the first no"))
b=int(input("enter the second no"))
obj=cal(a,b)
choice=1
while choice!=0:
    print("o.Exit")
    print("1.Add")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

numpy