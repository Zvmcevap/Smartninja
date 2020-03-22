import csv
# Vards
suspect_dna = ""
criminal = {"Name": "None"}
found_criminal = {"Name": "None"}
# Dna translation
Hair_color = {
    "Black": "CCAGCAATCGC",
    "Brown": "GCCAGTGCCG",
    "Blonde": "TTAGCTATCGC"
}

Facial_shape = {
    "Square": "GCCACGG",
    "Round": "ACCACAA",
    "Oval": "AGGCCTCA"
}

Eye_color = {
    "Blue": "TTGTGGTGGC",
    "Green": "GGGAGGTGGC",
    "Brown": "AAGTAGTGAC"
}

Gender = {
    "Female": "TGAAGGACCTTC",
    "Male": "TGCAGGAACTTC"
}

Race = {
    "White": "AAAACCTCA",
    "Black": "CGACTACAG",
    "Asian": "CGCGGGCCG"
}
dna_meta = [Gender, Race, Hair_color, Eye_color, Facial_shape]

# The peoples
Eva = {
    "Name": "Eva",
    "Gender": "Female",
    "Race": "White",
    "Hair_color": "Blonde",
    "Eye_color": "Blue",
    "Face_shape": "Oval"
}

Larisa = {
    "Name": "Larisa",
    "Gender": "Female",
    "Race": "White",
    "Hair_color": "Brown",
    "Eye_color": "Brown",
    "Face_shape": "Oval"
}

Matej = {
    "Name": "Matej",
    "Gender": "Male",
    "Race": "White",
    "Hair_color": "Black",
    "Eye_color": "Blue",
    "Face_shape": "Oval"
}

Miha = {
    "Name": "Miha",
    "Gender": "Male",
    "Race": "White",
    "Hair_color": "Brown",
    "Eye_color": "Green",
    "Face_shape": "Square"
}

suspects = [Matej, Eva, Miha, Larisa]


# Send the data to a CSV file
with open("crooks.csv", "w", newline="") as people:
    fields = ["Name", "Gender", "Race", "Hair_color", "Eye_color", "Face_shape"]
    writer = csv.DictWriter(people, fieldnames=fields)
    writer.writeheader()
    for person in suspects:
        writer.writerow(person)
# Done with crooks


# Definitions
def print_suspects():
    for suspect in suspects:
        print(suspect["Name"], suspect["Gender"])


def print_a_supect(name):
    for sus in suspects:
        if name == sus["Name"].lower():
            for s in sus:
                print(s, sus[s])


def get_suspect_dna():
    with open("dna.txt", "r") as dnatext:
        dna = dnatext.read()
        return dna


def analyze_dna(input_dna):
    if input_dna != "":
        guilty = {
            "Gender": "",
            "Race": "",
            "Hair_color": "",
            "Eye_color": "",
            "Face_shape": ""
            }
        print("\nSAMPLE ANALYSIS: ")
        for category in dna_meta:
            x = dna_meta.index(category)
            print(f"---- {x + 1} ----")
            for value in category:
                if input_dna.find(category[value]) > -1:
                    print(f"DNA MATCH! --- {value}")
                    if x == 0:
                        guilty["Gender"] = value
                    elif x == 1:
                        guilty["Race"] = value
                    elif x == 2:
                        guilty["Hair_color"] = value
                    elif x == 3:
                        guilty["Eye_color"] = value
                    elif x == 4:
                        guilty["Face_shape"] = value
                else:
                    print("DNA not a MATCH!")
        print("\nRESULT:")
        for g in guilty:
            print(f"{g} : {guilty[g]}")
        guilty["Name"] = "None"
        return guilty
    else:
        print("---- NO DNA SAMPLE LOADED ----")
        pancake = {"Name": "None"}
        return pancake


def compare_data(sus, crim):
    if "Gender" in crim and len(sus) > 0:
        print(f"\nDNA ANALYSIS: ")
        quilty = {"Name": "None"}
        for suspect in sus:
            if suspect["Gender"] == crim["Gender"] and suspect["Race"] == crim["Race"] and \
                    (suspect["Hair_color"] == crim["Hair_color"] and suspect["Eye_color"] == crim["Eye_color"] and
                     (suspect["Face_shape"] == crim["Face_shape"])):
                print(f'{suspect["Name"]} ---- DNA MATCH FOUND!')
                quilty = suspect
            else:
                print(f"{suspect['Name']} ---- NOT A MATCH!")
        print(f"\nRESULT: ")
        print(f'\nCONFIRMED MATCH: {quilty["Name"]}')
        if quilty["Name"] != "None":
            print("---- MATCH FOUND ----\n")
            for q in quilty:
                if q == "Name":
                    print(f'{q}: {quilty[q]}')
                else:
                    print(f'{q}: {quilty[q]} ---- 100% MATCH')
            return quilty
        else:
            pan = {"Name": "None"}
            print("---- NO MATCH ----")
            return pan
    else:
        print("---- NO DATA TO COMPARE ----")
        cake = {"Name": "None"}
        return cake


cop_name = input("Name: ")
cop_badge = input("Badge number: ")
print(f'\nLogged in:\n{cop_name}\nBN: {cop_badge}')

while True:
    print("\n---- COMMANDS ----")
    print("ls= load dna sample, as= analyze dna sample, ps= print suspects, fm= find dna match")
    print("type suspects name to see their profile, g= guilty profile, x= exit program")
    command = input("Command: ").lower()
    if command == "ls":
        suspect_dna = get_suspect_dna()
    elif command == "as":
        criminal = analyze_dna(suspect_dna)
    elif command == "fm":
        found_criminal = compare_data(suspects, criminal)
    elif command == "ps":
        print_suspects()
    elif command == "x":
        break
    elif command == "g":
        if found_criminal["Name"] != "None":
            for c in found_criminal:
                print(c, found_criminal[c])
        else:
            print("---- NO CRIMINAL FOUND ----")
    else:
        print_a_supect(command)
