word_without_vowels = ""

user_word = input("Please enter the word: ")
user_word = user_word.upper()
for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A":
        continue
    elif letter == "I":
        continue
    elif letter == "E":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)
