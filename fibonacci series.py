a = int(input("Enter the terms : "))
x = 0
y = 1
print(x,y, end = " ")
for i in range(2,a):
    next = x+y
    print(next,end = " ")
    x = y
    y = next
