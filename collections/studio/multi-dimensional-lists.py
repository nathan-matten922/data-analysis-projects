food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

multi = [food,equipment,pets,sleep_aids]
# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food = food.split(",")
food.sort()
equipment = equipment.split(',')
equipment.sort()
pets = pets.split(',')
pets.sort
sleep_aids = sleep_aids.split(",")
sleep_aids.sort

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food,equipment,pets,sleep_aids]
print(cargo_hold)


# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
i = input("Select the cabinet you would like to access (0-3):")
i = int(i)



# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
if i > 3 or i < 0:
    print("INVALID ENTRY (you dunderhead)")
else:
    print(cargo_hold[i])


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”

c, value = input("Select the cabinet (1-4) and list the item you're looking for:").split()
c = int(c) - 1
for cabinet in cargo_hold:
    if cabinet == cargo_hold[c]:
        print(cabinet)
        if value not in cabinet:
            print(f"Cabinet {c + 1} DOES NOT contain {value}")
        else:
            print(f"Cabinet {c + 1} DOES contain {value}")
