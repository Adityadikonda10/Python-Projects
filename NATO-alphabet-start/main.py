# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
NATO_file = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_data_frame = pandas.DataFrame(NATO_file)

nato_index_dict = {row.letter:row.code for (index, row) in NATO_data_frame.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# my method
# word = input("Enter a word: ").upper()
# word_list = [l for l in word]
# run = True
# try:
#     for letter in word:
#         nato_index_dict[letter]
# except KeyError:
#     while run:
#         print("Sorry, only letters and alphabets please!")
#         word = input("Enter a word: ").upper()
#         word_list = [l for l in word]
#         try:
#             for letter in word:
#                 nato_index_dict[letter]
#         except KeyError:
#             run = True
#         else:
#             print(word_list)
#             phonetic_list = [nato_index_dict[letter] for letter in word]
#             print(phonetic_list)
#             run = False
#
# else:
#     print(word_list)
#     phonetic_list = [nato_index_dict[letter] for letter in word]
#     print(phonetic_list)

# trainers method
def generate_phonetic():
    word = input("Enter a word: ").upper()
    word_list = [l for l in word]
    try:
        phonetic_list = [nato_index_dict[letter] for letter in word_list]
    except KeyError:
        print("Sorry, only letters and alphabets please!")
        generate_phonetic()
    else:
        print(phonetic_list)
generate_phonetic()