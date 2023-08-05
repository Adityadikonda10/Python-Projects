thousand = 1000
million = 1000000
billion = 1000000000
trillion = 100000000000
quadrillion = 1000000000000000
quintillion = 10000000000000000000


def calculate(number, convert_to, input_scale, output_scale):
    """input the number you want to convert to"""
    if convert_to == "thousand":
        ans = number / thousand
        if input_scale == "kg" and output_scale == "kg":
            ans = ans / 1
            print(f"{ans} thousand kgs")
        elif input_scale == "kg" and output_scale == "tonne":
            ans = ans / 1000
            print(f"{ans} thousand tonnes")
        elif input_scale == "tonne" and output_scale == "tonne":
            ans = ans / 1
            print(f"{ans} thousand tonnes")
        elif input_scale == "tonne" and output_scale == "kg":
            ans = ans * 1000
            print(f"{ans} thousand kgs")
        else:
            print("Invalid input")
    elif convert_to == "million":
        ans = number / million
        if input_scale == "kg" and output_scale == "kg":
            ans = ans / 1
            print(f"{ans} million kgs")
        elif input_scale == "kg" and output_scale == "tonne":
            ans = ans / 1000
            print(f"{ans} million tonnes")
        elif input_scale == "tonne" and output_scale == "tonne":
            ans = ans / 1
            print(f"{ans} million tonnes")
        elif input_scale == "tonne" and output_scale == "kg":
            ans = ans * 1000
            print(f"{ans} million kgs")
        else:
            print("Invalid input")
    elif convert_to == "billion":
        ans = number / billion
        if input_scale == "kg" and output_scale == "kg":
            ans = ans / 1
            print(f"{ans} billion kgs")
        elif input_scale == "kg" and output_scale == "tonne":
            ans = ans / 1000
            print(f"{ans} billion tonnes")
        elif input_scale == "tonne" and output_scale == "tonne":
            ans = ans / 1
            print(f"{ans} billion tonnes")
        elif input_scale == "tonne" and output_scale == "kg":
            ans = ans * 1000
            print(f"{ans} billion kgs")
        else:
            print("Invalid input")
    elif convert_to == "trillion":
        ans = number / trillion
        if input_scale == "kg" and output_scale == "kg":
            ans = ans / 1
            print(f"{ans} trillion kgs")
        elif input_scale == "kg" and output_scale == "tonne":
            ans = ans / 1000
            print(f"{ans} trillion tonnes")
        elif input_scale == "tonne" and output_scale == "tonne":
            ans = ans / 1
            print(f"{ans} trillion tonnes")
        elif input_scale == "tonne" and output_scale == "kg":
            ans = ans * 1000
            print(f"{ans} trillion kgs")
        else:
            print("Invalid input")
    elif convert_to == "quadrillion":
        ans = number / quadrillion
        if input_scale == "kg" and output_scale == "kg":
            ans = ans / 1
            print(f"{ans} quadrillion kgs")
        elif input_scale == "kg" and output_scale == "tonne":
            ans = ans / 1000
            print(f"{ans} quadrillion tonnes")
        elif input_scale == "tonne" and output_scale == "tonne":
            ans = ans / 1
            print(f"{ans} quadrillion tonnes")
        elif input_scale == "tonne" and output_scale == "kg":
            ans = ans * 1000
            print(f"{ans} quadrillion kgs")
        else:
            print("Invalid input")
    elif convert_to == "quintillion":
        ans = number / quintillion
        if input_scale == "kg" and output_scale == "kg":
            ans = ans / 1
            print(f"{ans} quintillion kgs")
        elif input_scale == "kg" and output_scale == "tonne":
            ans = ans / 1000
            print(f"{ans} quintillion tonnes")
        elif input_scale == "tonne" and output_scale == "tonne":
            ans = ans / 1
            print(f"{ans} quintillion tonnes")
        elif input_scale == "tonne" and output_scale == "kg":
            ans = ans * 1000
            print(f"{ans} quintillion kgs")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
        return 0

num_user = input("Enter number you want to convert to \n")
num = []
for n in (num_user):
    num.append(n)
i = 0
for n in (num):
    if n == ",":
        num.remove(",")

    i += 1
xyz = ""
for z in num:
    xyz += z
num_user_gave = int(xyz)
# print(num_user_gave)

convert_to_metric = input("Enter the metric you want to convert to \n")
in_what_ = input("is entered value in kg or tonne \n ")
ans_in_what = input("What scale you want your ans in? \n")
calculate(num_user_gave, convert_to_metric, in_what_, ans_in_what)




# num_user = input("Enter number you want to convert to \n")
# num = []
# for n in (num_user):
#     num.append(n)
# i = 0
# for n in (num):
#     if n == ",":
#         num.remove(",")
#         num[int(i)] = ""
#     i += 1
#
# print(' '.join(num))

