input = int(input("Enter a 5-digit number: "))
output = 0
while input > 0:
    digit = input%10
    output = (output * 10) + digit
    input = output/10
print(output)
