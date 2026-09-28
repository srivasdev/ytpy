# num = int(input("Enter any three digit number:-"))

# a = num % 10
# num = num // 10

# b = num % 10
# num = num // 10

# c = num % 10

# reverse = a * 100 + b*10 + c

# print("Reverse =" , reverse) 


num = int(input("Enter any four digit number:-"))

a = num % 100
num = num // 100

b = num % 100
num = num // 100

c = num % 100
num = num // 100

d = num % 100

reverse = a*1000 + b*100 + c*10 + d