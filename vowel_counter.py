# written by James Carvell in python 3.6
# to be run from a terminal
# should ask for a string from user, count the vowels, and return # of vowels

# taking the user input
phrase = input("type a word or phrase without accents and hit enter\n>")

# for better readability in counting. Using list comprehension to convert list of letters to a list of the count of each of those letters
def letter_count_list(letter_list):
    return([phrase.count(i) for i in letter_list])

# lists of vowels and semivowels to be counted
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
semivowels = ["w", "W", "y", "Y"]

# setting count variables to 0
vowel_count = 0
semivowel_count = 0

# counting individual vowels and semivowels with letter_count_list function and summing counts with for loops
for counts in letter_count_list(vowels):
    vowel_count = vowel_count + counts
    
for counts in letter_count_list(semivowels):
    semivowel_count = semivowel_count + counts

# return number of vowels to the user
print(f"There are {vowel_count} vowels and {semivowel_count} semivowels.")