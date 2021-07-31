"""x = int(input("Enter a number:"))
a=0
while a<x:
    a = a + 1
    if a%10==0:
        continue
    elif a>100:
        break
    else:
        print(a)"""
x=str(input("enter a string:")).split(' ')
y=str(input("enter a word:"))
for i in x:
    if y == i:
        print("word {} "is found"),format(y)
        break
    else:print("word not found")



