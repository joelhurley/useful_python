number = int(input("Pick a number: "))

if (number %3 == 0):
    print("Fizz")

if (number %5 == 0):
    print("Buzzzzzzzzzzzzzzzzzzzz")

elif ((number %3 == 0) and (number %5 == 0)):
    print("Fizz buzzzzzzzzzzzzzzzzzzzz")

else:
    print(number)
