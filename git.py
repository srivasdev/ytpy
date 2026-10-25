# n = int(input("Enter which number's you want to print:-"))

# a = range(1,11,1)

# for i in a:
#     print(i*n)

# a = range(1,89,2)

# for i in a:
#     print(i)

# a = range(89,-1,-1)

# for i in a:
#     print(i)

# a = range(59,88,2)
# for i in a:
#     print(i)

# a =  range(4,54,3)
# for i in a:
#     print(i)


n = int(input("Enter a 3-digit number"))
hundreds = n // 100
tens = (n // 100) % 10
units = n % 10
print("Sum od digits =" , hundreds + tens + units)