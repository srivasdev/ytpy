# s = "Python"
# print(s[-1:-6:-1])


# name = str(input("Enter your full name:-"))
# space = name.find(" ")
# first =name[0:space]
# last = name[space+1:]
# print(last+" "+first)


# name reversal
# name = str(input("Enter your Favourite Car name in Reverse:-"))
# rev = name[-1::-1]
# print("Fav. car is:-" , rev)

# check if entered name is palindrome or not.

name = input("Enter your name:-")

chk = name[-1::-1]

if chk == name:
    print("Your name  is palindrome.")
else:
    print("Your name is not palindrome.")

# name = input("Enter your Name:-")
# chk = name[-1::-1]

# if chk == name:
#     print("Your name is palindrome.")
# else:
#     print("Your name is not palindrome.")


