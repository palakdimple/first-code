def add():
    a= int(input("enter 1st value"))
    b= int(input("enter 2nd value"))
    print(a+b)
def sub():
    a= int(input("enter the 1st value"))
    b= int(input("enter the 2nd value"))
    print(a-b)
def mul():
    a= int(input("enter the 1st value"))
    b= int(input("enter hte 2nd value"))
    print(a*b)
def div():
    a= int(input("enter the 1st value"))
    b= int(input("enter the 2nd value"))
    print(a/b)
print("this is a calculator made by me")
value= input("what you want to do +,-,*,/")
if value=="+":
    add()
elif value=="-":
    sub()
elif value=="*":
    mul()
elif value=="/":
    div()
else:
    print("not valid")