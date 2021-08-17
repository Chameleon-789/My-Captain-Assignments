print("________________________________________________________")
num1 = int(input("The first number: "))

num2 = int(input("The second number: "))

num3 = int(input("The third number: "))

num4 = int(input("The fourth number: "))

num5 = int(input("The fifth number: "))

list = [num1, num2, num3, num4, num5]
print("________________________________________________________")

for x in list:
    if x >=0:
        print(x)
        x=x+1

print("are positive")
print("________________________________________________________")
