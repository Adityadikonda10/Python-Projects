# ------------------------------------------- Q2# ------------------------------------------- #

# imput_integer = int(input("Enter a number to check if it exists in power of 2: "))
#
# power_2 = [2**i for i in range(0,100)]
#
# for num in power_2:
#     if imput_integer in power_2:
#         print("true")
#         break
#     else:
#         print("false")
#         break


# ------------------------------------------- Q3# ------------------------------------------- #

# num = [int(n) for n in input("Enter numbers for a list to sort: ")]
# print(f"List of entered number is: {num}")
# for n in num:
#     if n != 0:
#         pass
#     else:
#         num.remove(n)
#         num.append(n)
# print(f"Sorted list is: {num}")


# ------------------------------------------- Q4# ------------------------------------------- #
#
# test_dict = {
#     "a": 3,
#     "b": 7,
#     "c": 10,
#     "d": 6,
#     "e": "CS"
# }
#
# K = 7
#
# def check_K():
#     for key in test_dict:
#         if test_dict[key] > K:
#             del test_dict[key]
#             test_dict.update()
#
#
# try:
#     check_K()
# except RuntimeError:
#     print(test_dict)
# check_K()


# # ------------------------------------------- Q5# ------------------------------------------- #
# input = "d89%l++5r19o7w *o=l645le9h"
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
#
# ascii_excluding = [letter for letter in input if letter in letters]
# sorted_letters = [letter for letter in ascii_excluding[::-1]]
# output = ""
# for letter in sorted_letters:
#     output += letter
# print(output)





