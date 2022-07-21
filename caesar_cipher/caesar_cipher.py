import nltk
from nltk.corpus import words

nltk.download("words", quiet=True)

word_list = words.words()

# 1. Set up list of alphabet.  This will be used for indexing via the shift.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# 2. Define a function called "encrypt" that takes in a plain text phrase and
# a numeric shift.
def encrypt(given_string, num_shift):
    # Declare a variable to hold the encrypted string.
    encrypted_string = ""
    # A. Iterate over the plain text phrase.
    for letter in given_string:
        # Check if letter is actually a letter.
        if letter.isalpha():
            # Check if letter is uppercase.
            is_upper = letter.isupper()
            # If true, convert to lowercase.
            if is_upper:
                letter = letter.lower()
            # 1. Using the alphabet list, find the index of the letter.
            index = alphabet.index(letter)
            # 2. Shift the index by the number provided.
            index += num_shift
            # 3. Check if the index is > 25.  (List index starts at 0.)
            if index > 25:
                # a. If yes, subtract 26.
                index -= 26
            # 4. Obtain the letter of the new index.
            new_letter = alphabet[index]
            # If originally an uppercase letter, change back to uppercase.
            if is_upper:
                new_letter_upper = new_letter.upper()
                encrypted_string += new_letter_upper
            # If originally a lowercase letter, just add to encrypted_string.
            else:
                encrypted_string += new_letter
        # If not a letter, just add the character to the encryption string.
        else:
            encrypted_string += letter
    return encrypted_string


# 3. Define a function called decrypt.
def decrypt(given_string, num_shift):
    # A. Call the encrypt function.  Pass it the string and numeric shift.
    return encrypt(given_string, -num_shift)


# 4. Define a function called crack.
def crack():
    pass

# Use decrypt function and run each word through using a decrypt key of 1 - 26.
# Check if each word is in the word list.


if __name__ == '__main__':
    encrypt("BANANA!", 1)
