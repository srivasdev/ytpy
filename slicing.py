# s = "Python"
# print(s[-1:-6:-1])


name = str(input("Enter your full name:-"))
space = name.find(" ")
first =name[0:space]
last = name[space+1:]
print(last+" "+first)

