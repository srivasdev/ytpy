# reverse of string.

# name = str(input("Enter your full name:-"))
# space = name.find(" ")
# first = name[0:space]
# last = name[space+1:]
# print(last+" "+first)

# occurance of A in name.

name = str(input("Enter yourr name"))
count = 0

for i in name:
    if i == "A":
      count += 1

print("Occurance of A=" , count)
