proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
connectors = [',',';'," "]
'''for string in strings:
    if ';' in string:
        print(f"This list {string} has a ;")
    elif ',' in string:
        print(f"This list {string} has a ,")
    else:
        print(f"This list {string} is separated by a space")'''

for string in strings:
    for connector in connectors:
        if connector in string:
            if connector == " ":
                print(f"This string {string} is separated by a space")
            else:
                print(f'This string {string} is separated by {connector}')


# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
new_string = ""
flip_string = ""
delimeter = ""
final_string = ""
for string in strings:
    if "," in string:
        if " " not in string:
            new_string = string.split(",")
            flip_string = new_string[::-1]
            final_string = ",".join(flip_string)
            print(final_string)
'''        else:
            new_string = string.split(", ")
            flip_string = new_string[::-1]
            final_string = ",".join(flip_string)
            print(final_string)'''


# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
alphabet_string = ""
for string in strings: 
    if ";" in string:
        alphabet_string = string.split(";")
        alphabet_string.sort()
        final_string = ",".join(alphabet_string)
        print(final_string)


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

space_string = "" 
for string in strings: 
    if " " in string:
        if "," not in string: 
            space_string = string.split(' ')
            space_string.sort(reverse= True)
            final_string = " ".join(space_string)
            print(final_string)

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
comma_space = ""
for string in strings:
    if ", " in string:
        comma_space = string.split(", ")
        flip_string = comma_space[::-1]
        final_string = ",".join(flip_string)
        print(final_string)