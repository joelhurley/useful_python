name = (input("Name: "))
age = int(input("Age: "))
country = (input("Country: "))

if age < 18:
    print(name,"You are not allowed to vote")
elif age >= 18:
    if country == "UK" or country == "Britain":
       print(name,"You are entitled to vote")
    else:
        print("Correct age wrong country")
        

