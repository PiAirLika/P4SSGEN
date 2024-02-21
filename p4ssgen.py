from itertools import combinations

print("\033[34m" + r".______    _  _         _______.     _______.  _______  _______ .__   __. " + "\033[0m")
print("\033[34m" + r"|   _  \  | || |       /       |    /       | /  _____||   ____||  \ |  | " + "\033[0m")
print("\033[34m" + r"|  |_)  | | || |_     |   (----`   |   (----`|  |  __  |  |__   |   \|  | " + "\033[0m")
print("\033[34m" + r"|   ___/  |__   _|     \   \        \   \    |  | |_ | |   __|  |  . `  | " + "\033[0m")
print("\033[34m" + r"|  |         | |   .----)   |   .----)   |   |  |__| | |  |____ |  |\   | " + "\033[0m")
print("\033[34m" + r"| _|         |_|   |_______/    |_______/     \______| |_______||__| \__| " + "\033[0m")
print('')

def main():
    print("1- Create a targeted Wordlist")
    print("")
    w = input("Please choose a number : ")
    if w == '1':
        print("To create a custom wordlist, we need informations of your victim\nif you are missing information, press enter")
        print("")
        name = input("Name : ")
        firstn = name[0:1]
        midn = name[0:3]
        sname = input("Surname : ")
        firstsn = sname[0:1]
        midsn = sname[0:3]
        while True:
            birth = input("Date of birth (e.g: '02122024'): ")
            if birth == (''):
                break

            try:
                if len(birth) !=8:
                    print("date of birth must be 8 digits long")
                    continue
                elif int(str(birth)[0:2]) > 31:
                    print("The day is superior than 31")
                    continue
                elif int(str(birth)[2:4]) > 12:
                    print("The month is superior than 12")
                    continue
                else:
                    break
            except ValueError:
                print("Please enter a number")
                continue

        day = birth[0:2]
        month = birth[2:4]
        year = birth[4:8]
        secyear = birth[6:8]
        print(day, month, year, sep="/")
        dad = input("Father's name : ")
        mom = input("Mother's name : ")
        pet = input("Pet's name : ")
        while True:
            state = input("ZIP Code : ")
            if state == (''):
                break
            try:
                int(state)
                break
            except ValueError:
                print("Please enter a number")
                continue

        supp = []
        while True:
            plus = input("If you want to add special words (brother, hobbys...) add them here ( type 'end' to finish ) : ")
            if plus == ('end'):
                break
            supp.append(plus)
        wdlist = [name, sname, birth, day, month, year, secyear, dad, mom, pet, state] # liste avec tous les mots input
        wdlist.extend(supp) # ajout de mots supplémentaires à la liste principale
        wdprec = [birth, firstn, firstsn, midn, midsn, day, month, secyear]

        filename = createwl(wdlist, supp)
        precision(wdprec, filename)
        organisetxt(wdlist, supp, filename)
        addspechars(wdlist, filename)
        removespace(filename)

        print(f"Wordlist created ! name : \033[32m{filename}\033[0m")

def createwl(wdlist, supp):
    counter = 1
    while True:
        try:
            filename = f"wordlist_{counter}.txt" if counter > 1 else "wordlist.txt"
            customwl = open(filename, "x")
            break  # Sortie de la boucle si le fichier a été créé avec succès
        except FileExistsError:
            counter += 1
        except Exception as e:
            print(f"An unexpected error occurred while creating the wordlist file: {e}")
            return None

    customwl.close()
    return filename  # Return le nom du fichier créé

def organisetxt(wdlist, supp, filename):
	with open(filename, "a") as customwl:
		for n in range(1, len(wdlist) + 1):
			for combo in combinations(range(len(wdlist)), n):
				line = ''.join(wdlist[i] for i in combo)
				if 8 <= len(line) <= 32:
					customwl.write(line + "\n")

def addspechars(wdlist, filename):
	listspechars = ['?', '*', '$', '%', '+', '-', '@', '/', '!', '#', "(", ")",":", ";"]
	with open(filename, "a") as customwl:
		for n in range(1, len(wdlist) + 1):
			for combo in combinations(range(len(wdlist)), n):
				base_word = ''.join(wdlist[i] for i in combo)
				for spechars in listspechars:
					line = base_word + spechars
					if 8 <= len(line) <= 32:
						customwl.write(line + "\n")

def removespace(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            if line.strip():
                file.write(line)

def precision(wdprec, filename):
    with open(filename, "a") as customwl:
        for n in range(1, len(wdprec) +1):
            for combo in combinations(range(len(wdprec)), n):
                line = ''.join(wdprec[i] for i in combo)
                if 8 <= len(line) <= 32:
                    customwl.write(line + "\n")

if __name__ == '__main__':
    main()
