string = "d89%l++5r19o7w *o=l645le9h"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# str_list = [letter for letter in string if letter in letters]
# rev_list = [l for l in str_list[::-1]]
str_list = []
for every_letter in string:
    str_list.append(every_letter)

ascii_excluded_list = []

for letter in str_list:
    if letter in letters:
        ascii_excluded_list.append(letter)
    else:
        pass
print(str_list)
print(ascii_excluded_list)