# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


l = 1
l_in_pass = ("")
while l <= nr_letters:
    l_in_pass += letters[random.randint(0, 51)]
    l += 1

n = 1
n_in_pass = ("")
while n <= nr_numbers:
    n_in_pass += numbers[random.randint(0, 9)]
    n += 1

s = 1
s_in_pass = ("")
while s <= nr_symbols:
    s_in_pass += symbols[random.randint(0, 8)]
    s += 1

# check = int(input("input number"))
password = [l_in_pass + n_in_pass + s_in_pass]
# print(final_pass)
# print(final_pass[check - 1])

# print(l_in_pass)
# print(n_in_pass)
# print(s_in_pass)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# check_letters = []
# i = 1
# num_used = []
# final_pass = ("")
# random_num = ("")
# final_random_num = ("")
# while i <= len(password):
#     # for x in check_letters:
#     #     y = x
#     #     for z in password:
#     #         if z in y:
#     #
#     if i > 1:
#         for n in num_used:
#             random_num = random.randint(0, len(password))
#             if n == random_num:
#                 new_random_num = random.randint(0, len(password))
#                 final_random_num = new_random_num
#                 num_used.append(final_random_num)
#                 final_pass += password[final_random_num - 1]
#             else:
#                 final_random_num = random_num
#                 random_num += final_random_num
#                 num_used.append(final_random_num)
#                 final_pass += password[final_random_num - 1]
#     else:
#         random_num = random.randint(0, len(password))
#         final_random_num = random_num
#         num_used.append(final_random_num)
#
#     print(password)
#     final_pass += password[final_random_num - 1]
#
#     i += 1
#
# # print(type(int(password)))
print(random.shuffle(password))