x = int(input("Enter the number :"))
for i in range (2,x):
    if (x%i)==0:
        print("It is a non prime number")
        break
    else:
        print("It is a prime number")
        break
