a= int (input("enter a number: "))
b= int (input("enter another number: "))
print("1=add \n2=sub \n3=mul \n4=divide")
c=int(input("enter your choice: "))


if c==1:
    s =a+b
    print("answer is: ", s)
elif c==2:
    sum =a-b
    print("answer is: ", sum)
elif c==3:
    sum = a*b
    print("answer is: ", sum)
elif c==4:
    sum = a/b
    print("answer is: ", sum)
else:
    print("invalid input")

