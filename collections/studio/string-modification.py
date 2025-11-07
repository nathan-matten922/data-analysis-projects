my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
my_string2 = my_string[3:] + my_string[:3]
print(my_string2)


# Use a template literal to print the original and modified string in a descriptive phrase.
print(f"Pig latin for {my_string} is {my_string2}")
print("Pig latin for {} is {}".format(my_string,my_string2))


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
i = input("Please enter the number of letters to move to the back:")
i = int(i)
if i <= len(my_string):
    print(f"Your new word is: {my_string[i:] + my_string[:i]}")


# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.

elif i > len(my_string):
    print(f"The word is too long. Defaulting to {my_string[3:] + my_string[:3]}")