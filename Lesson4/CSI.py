import csv
import random

# Vars
suspects = []
population = []
suspect_dna = ""
criminal = {"Name": "None"}
found_criminals = []
men_names = [
    "Miha", "Matej", "Matic", "Beno", "Rok", "Dean", "Dušan", "Stojan", "Roman", "Habib", "Marjan", "Senko", "Domen"
]
fem_names = [
    "Larisa", "Eva", "Mateja", "Neža", "Klara", "Hana", "Nika", "Nina", "Tina", "Pina", "Nuša", "Zala", "Katja"
]

# Dna translation
nucleobases = "ACGT"
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
# End DNA hows and dos


# Send the data to a CSV file for JUST IN CASE!
def csv_list_for_looking():
    with open("crooks.csv", "w", newline="") as people:
        fields = ["Name", "Gender", "Race", "Hair_color", "Eye_color", "Face_shape"]
        writer = csv.DictWriter(people, fieldnames=fields)
        writer.writeheader()
        for person in suspects:
            writer.writerow(person)


# Functions for stuffs
def populate_suspect_list(p):

    suspicious_characters = []
    for x in range(p):
        individual = {"Gender": random.choice(list(dna_meta[0].keys())),
                      "Race": random.choice(list(dna_meta[1].keys())),
                      "Hair_color": random.choice(list(dna_meta[2].keys())),
                      "Eye_color": random.choice(list(dna_meta[3].keys())),
                      "Face_shape": random.choice(list(dna_meta[4].keys()))}
        if individual["Gender"] == "Male":
            individual["Name"] = random.choice(men_names)
            suspicious_characters.append(individual)
        else:
            individual["Name"] = random.choice(fem_names)
            suspicious_characters.append(individual)
    return suspicious_characters


def print_suspects():
    print("---- SUSPECTS ----")
    for pers in suspects:
        print(f'Name: {pers["Name"]}')
        for k in pers:
            if k != "Name":
                print(f'{k}: {pers[k]}')
        print("---- ---- ----")


def print_a_supect(name):
    x = 0
    for sus in suspects:
        if name == sus["Name"].lower():
            x += 1
            print(f'---- {x} ----')
            print(f'Name: {sus["Name"]}')
            for s in sus:
                if sus[s] != "Name":
                    print(f"{s}: {sus[s]}")
    if x != 0:
        name = name.capitalize()
        print(f'---- found {x} persons with the name: {name} ----')


def get_suspect_dna():
    dna = ""
    for feature in dna_meta:
        for n in range(63):
            dna += random.choice(nucleobases)
        dna += random.choice(list(feature.values()))
    with open("dna.txt", "w") as dnatext:
        dnatext.write(dna)
    print("\n---- DNA SAMPLE OBTAINED ----")
    print(f'---- {len(dna)} nucleobases ----')
    print("---- SAMPLE LOADED ----")
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
    matches = []
    if "Gender" in crim and len(sus) > 0:
        print(f"\nDNA ANALYSIS: ")
        for suspect in sus:
            if suspect["Gender"] == crim["Gender"] and suspect["Race"] == crim["Race"] and \
                    (suspect["Hair_color"] == crim["Hair_color"] and suspect["Eye_color"] == crim["Eye_color"] and
                     (suspect["Face_shape"] == crim["Face_shape"])):
                print(f'{suspect["Name"]} ---- DNA MATCH FOUND!')
                matches.append(suspect.copy())
            else:
                print(f"{suspect['Name']} ---- NOT A MATCH!")
        print(f"\nRESULT: ")
        if len(matches) > 0:
            for m in matches:
                print(f'CONFIRMED MATCH: {m["Name"]}')
        else:
            print("---- NO MATCH ----")
    if len(sus) == 0:
        print("\n---- NO SUSPECTS IN DATABASE ----")
        print("---- ENTER SUSPECT LIST ----")
    if "Gender" not in crim:
        print("\n---- NO DNA COMPARISON ----")
        print("---- ANALYZE DNA SAMPLE ----")
    if len(matches) == 0 or len(matches) > 1:
        print(f'Analysis complete: found {len(matches)} matches!')
    else:
        print(f'Analysis complete: found {len(matches)} match!')
    return matches


cop_name = input("Name: ")
cop_badge = input("Badge number: ")
print(f'\nLogged in:\n{cop_name}\nBN: {cop_badge}')

while True:
    print("")
    if suspect_dna == "":
        print(f'DNA SAMPLE: N/A')
    else:
        print(f'DNA SAMPLE: Ready')
    if "Gender" not in criminal:
        print(f'DNA ANALYSIS: N/A')
    else:
        print(f'DNA ANALYSIS: Complete')
    print(f'Suspects: {len(suspects)}')
    print("\n---- COMMANDS ----")
    print("ls= load dna sample, as= analyze dna sample, fm= find dna match, m= dna matches")
    print("ps= print suspects, pop= populate suspect list")
    print("type suspects name to see their profile, x= exit program: ")
    command = input("Command: ").lower()
    if command == "ls":
        criminal = {"Name": "None"}
        suspect_dna = get_suspect_dna()
    elif command == "as":
        criminal = analyze_dna(suspect_dna)
    elif command == "fm":
        found_criminals = compare_data(suspects, criminal)
    elif command == "ps":
        print_suspects()
    elif command == "x":
        break
    elif command == "m":
        if len(found_criminals) > 0:
            print("---- MATCHES ----")
            for tits in found_criminals:
                print(f'Name: {tits["Name"]}')
                for t in tits:
                    if t != "Name":
                        print(f'{t}: {tits[t]}')
                print("---- ---- ----")
        else:
            print("---- NO MATCHES IN DATABASE ----")
    elif command == "pop":
        while True:
            broj = ""
            numb = input("How many suspects have you found: ")
            for d in numb:
                if d.isdigit():
                    broj += d
            if broj != "":
                broj = int(broj)
                suspects = populate_suspect_list(broj)
                csv_list_for_looking()
                break
            else:
                print("---- Not a valid number ----")
    else:
        print_a_supect(command)
