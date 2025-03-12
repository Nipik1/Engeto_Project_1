"""
main.py: první projekt do Engeto Online Python Akademie

author: David Nipauer
email: davidnipauer@gmail.com
"""
import string # Nahrál jsem modul string, proto pozdější odstranění interpunkce

def analyza_textu(text, cislo_textu): #funkce pro zkrácení kodu. Dále by bylo potřeba v if statementu vypisovat všechny loopy znovu a znovu.
    
    pocet_slov = len(text.split()) #počet slov v textu

    velke_prvni_pisemno = 0  #pocet velkých písmen na začátku slova
    for word in text.split():
        if word.istitle():
            velke_prvni_pisemno += 1
    
    velke_slovo = 0          #pocet slov psané velkým písmenem
    for word in text.split():
        if word.isupper():
            velke_slovo += 1
    
    male_slovo = 0           #pocet slov psané malým písmenem
    for word in text.split():
        if word.islower():
            male_slovo += 1

    cisla_v_textu = 0       #pocet ciselných řad
    for word in text.split():
        if word.isnumeric():
            cisla_v_textu += 1

    vysledek = 0            #celkový součet
    for word in text.split():
        if word.isdigit():
            vysledek += int(word)
    
    print(f"There are {pocet_slov} words in the selected text.")
    print(f"There are {velke_prvni_pisemno} titlecase words.")
    print(f"There are {velke_slovo} uppercase words.")
    print(f"There are {male_slovo} lowercase words.")
    print(f"There are {cisla_v_textu} numeric strings.")
    print(f"The sum of all the number {vysledek}")





def delka_slov_bez_interpunkce(text): # funkce pro očištění textu o interpukci, zde použijeme modul string.punctuation
    delky_slov = {}

    for word in text.split():
        clean_word = word.strip(string.punctuation)  
        length = len(clean_word)
        
        if length > 0:
            delky_slov[length] = delky_slov.get(length, 0) + 1

    return delky_slov


def zobraz_vysledek(text): # Výpis tabulky po analýze vybraného textu
    delky_slov = delka_slov_bez_interpunkce(text)
    print(dots)
    print("LEN |   OCCURENCES   | NR.")
    print("-" * 35)

    for length in sorted(delky_slov): #seřazení slovníku od nejmenší po největší
        print(f"{length:2}  | {'*' * delky_slov[length]:<15} | {delky_slov[length]}") #Zarovnání - přiznávám, že tady jsem si velmi pomohl googlem.
    
    

#Tady jsem rozdělil jeden text na 3 různé pro snadnější práci
TEXT1 = """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley."""
TEXT2 = """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick."""
TEXT3 = """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present."""




users = [
        {"user": "bob", "password": "123"},
        {"user": "ann", "password": "pass123"},
        {"user": "mike", "password": "password123"},
        {"user": "liz", "password": "pass123"}
    ]
dots = "-" * 35

def prihlaseni(username, password): #funkce pro volání přihlášení

    for user in users: #smyčka pro ověření loginu a hesla
        if user["user"] == username and user["password"] == password:
            return True
    return False


user_input = input("username: ")
password_input = input("password: ")

if prihlaseni(user_input, password_input): #volání funkce
    print(dots)
    print(f"Welcome to the app, {user_input.capitalize()}\nWe have 3 texts to be analyzed.") #.capitalize, opět jen pro hezčí output
    print(dots)
else:
    print("unregistred user, terminating program...")
    exit() #ukončení celého programu

while True:
    try: #try/except v případě, že by uživatel zadal něco jiného než číslo. Konverze inputu na integar
        choice = int(input("Enter a number btw. 1 and 3 to select: "))
        print(dots)
        if choice == 1:
            analyza_textu(TEXT1, 1) #volání funkce pro jednotlivé texty
            zobraz_vysledek(TEXT1) #zobrazení diagramu pro text 1
            print(dots) 
        elif choice == 2:
            analyza_textu(TEXT2, 2)
            zobraz_vysledek(TEXT2)
            print(dots)
        elif choice == 3:
            analyza_textu(TEXT3, 3)
            zobraz_vysledek(TEXT3)
            print(dots)
        else:
            print("Error, please try again.")
            continue
    except ValueError:
        print("Please enter a number.") 
        continue
    

    while True: # Možnost pro uživatele zkontrolovat jiný text, bez nutnosti se znovu přihlašovat.
        pokracovat = input("Do you wish to continue? Y/N: ").strip().lower()

        if pokracovat == "n":
            print("Thank you and have a nice day.")
            exit()
        elif pokracovat == "y":
            break
        else:
            print("Please select Y for continue or N to end the program")
            continue
 
