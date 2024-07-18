import string
import random

#Ask for length
length = int(input("How many characters do you want your password to have?: "))
#Add all characters (UPPERCASE, LOWERCASE, DIGITS & PUNCTUATION)
characters = string.ascii_letters + string.digits + string.punctuation
#Only generates a password if the lenght is 8 or more. (Security reasons)
if length > 7:
    password = "".join(random.choice(characters) for i in range(length))
    print(f"Your secure password is: {password}")
else:
    print(f"{length} are too little characters. Please try again with 8 or more.")


