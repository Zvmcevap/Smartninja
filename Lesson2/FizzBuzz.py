import math

stevilka = int(input("Enter between 1 - 100: "))
if stevilka > 100:
    stevilka = 100

for stevilka in range(stevilka + 1):
    if math.fmod(stevilka, 5) == 0 and math.fmod(stevilka, 3) == 0 and stevilka != 0:
        print("Fizzbuzz!")

    elif math.fmod(stevilka, 5) == 0 and stevilka != 0:
        print("Buzz!")

    elif math.fmod(stevilka, 3) == 0 and stevilka != 0:
        print("Fizz!")

    else:
        print(stevilka)

malecrke = input("Vtipkaj besedilo z vElIkimI črkami: ")

print(malecrke.lower())
