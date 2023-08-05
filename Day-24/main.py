#TODO: Create a letter using starting_letter.txt

with open("./input/letters/starting_letter.txt") as sl:
    content_sl = sl.read()


with open("./input/names/invited_names.txt", "r") as inv:
    invited_guests = inv.readlines()
for name in invited_guests:
    new_letter = content_sl.replace("[name]", name.strip())
    with open(f"./output/readytosend/{name}.txt", "w") as name:
        name.write(new_letter)







#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp