
# Variables here

user_name = input("Type in your name: ")
if user_name == "Beno":
    print("Prdeno ")
gender = input("Male or Female or something else: ")

conv_rate = 0.62
km = None
cont = True
cont_string = "y"
price_rate = 0.99
km_total = 0.0

#Beeps and Boops here

if gender == "Male":
    print("Hello, " + "Mr. " + user_name)
elif gender == "Female":
    print("Hello, " + "Ms. " + user_name)

while cont_string == "y":
    km = float(input("Enter kilometers: "))
    km_total = km_total + km
    print(km * conv_rate, "miles")
    print(km_total, "km talley.")
    cont_string = input("Type y to continue: ")

print(user_name + ", thank you for using UnitConverter(tm). Your Credit Card has been charged 99c per unit of km converted as per User License Agreenment. Which amounts to ",price_rate * km_total,"€ total.")
print("Thank you for using UnitConverted(tm) patent pendint. Have a fantastic day!")


