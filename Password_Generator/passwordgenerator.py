#Beginner level random password generator project in python
import string
import random

# Generating Password
def random_pass_gen(length):

    print('''Choose character set for password from these : 
            1. Digits
            2. Letters
            3. Special characters
            4. Exit''')

    characterList = ""
    while(True):
        choice = int(input("Pick your choice: "))
        if(choice == 2):
            
            # Adding letters to possible characters
            characterList += string.ascii_letters
        elif(choice == 1):
            
            # Adding digits to possible characters
            characterList += string.digits
        elif(choice == 3):
            
            # Adding special characters to possible
            # characters
            characterList += string.punctuation
        elif(choice == 4):
            break
        else:
            print("Please pick a valid option!")

    password = []

    for i in range(length):

        # Picking a random character from our 
        # character list
        randomchar = random.choice(characterList)
        
        # appending a random character to password
        password.append(randomchar)
    return password

    # printing password as a string
    


if __name__ == "__main__":
    # Getting password length
    length = int(input("Enter password length: "))
    new_password = random_pass_gen(length)
    print("The random password is " + "".join(new_password))