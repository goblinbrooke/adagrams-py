import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

# |Letter                        | Value|
# |:----------------------------:|:----:|
# |A, E, I, O, U, L, N, R, S, T  |   1  |
# |D, G                          |   2  |
# |B, C, M, P                    |   3  |
# |F, H, V, W, Y                 |   4  |
# |K                             |   5  |
# |J, X                          |   8  |
# |Q, Z                          |   10 |

LETTER_POOL_VALS = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def display_welcome_message():
    print("Welcome to Adagrams!")

def display_drawn_letters(letters):
    print("You have drawn the letters:")
    print(', '.join(letters))

def display_game_instructions():
    print("Please input your submission for the longest anagram you can come up with")

def display_needs_valid_input_message():
    print("You entered in a word that contains characters not in the letter bank")
    display_game_instructions()

def display_score(score):
    print(f"Your submitted anagram scored {score} points")

def display_retry_instructions():
    print("Should we play another round?")
    print("Enter y to replay")


def display_goodbye_message():
    print("Goodbye!")

display_welcome_message()


def draw_letters():
    return_list = []
    letter_freq = {}
    counter = 0
    
    while counter < 10:

            random_letter_index = random.randint(0,25)
            random_letter_val = list(LETTER_POOL.keys())[random_letter_index]
            if random_letter_val in letter_freq:
                letter_freq[random_letter_val] += 1
            else:
                letter_freq[random_letter_val] = 1

            if letter_freq[random_letter_val] <= LETTER_POOL[random_letter_val]:
                return_list.append(random_letter_val)
                counter += 1

    return return_list
    
print(draw_letters())
#display_drawn_letters(letters)

    # Funtion 1 Comment Walkthrough:
    # While loop to return 10 random letters and their values
    # Choose an integer position random between 1 and 26
    # Add LETTER_POOL[random int] to return_list
    # Grab just the keys of the dictionary and convert those to a list.
    # Then grab the index of that list using the random_letter number (1-26)
    # Because lists are 0-based, we need to subtract 1 otherwise we grab the letter before
    # Before appending the random letter, we need to look up and make sure it is not appearing more than the value in LETTER_POOL
    # Adds selected letter to list
    # Returns list

def uses_available_letters(word, letters):
    letter_found = True
    letter_bank = letters[:]
    
    while letter_found:
        for letter in word:
            if letter in letter_bank:
                letter_found = True
                letter_bank.remove(letter)
            else:
                letter_found = False

        return letter_found
    
    # Function 2 Comment Walkthrough:
    # Check to see if letters are in available word bank
    # Create a while loop to hold the status of whether we found the letter
    # Elif returns True if in bank, False if not
    # *REMOVES* from letter bank so does not CHANGE letter bank
    # The [:] makes a shallow copy of the array, hence allowing you to modify your copy without damaging the original
    
    # all: Return True if all elements of the iterable are true (or if the iterable is empty)
    # .count: returns the number of elements with the specified value.

def score_word(word):
    score = 0
    for letter in word:
        score += LETTER_POOL_VALS.get(letter.upper())
    if len(word) > 6:
        score += 8
    return score

    # Function 3 Comment Walkthrough:
    # Creates dictionary for letters and values
    # If for if letter in word - adds points, or not, does nothing
    # If length of word 8+, adds additional 8 points
    # .upper returns strings where all letters are uppercase
    # .get returns the value associated with a specific key

def get_highest_word_score(word_list):
    # later in this function, we will call the score_word function to assign the word's score
    # word_score = score_word()
    ordered_words = []
    return_words = []

    #1. Create and populate the dictionary with the tuples
    # ordered_words = ["elephant", 33, "chocolate", 42, "xxx, 32]
    for word in word_list:
        ordered_words.append(word)
        ordered_words.append(score_word(word))
    
    #2. Order the dictionary
    #do a loop and create a new return_words off of ordered_words
    for i in range(0,len(ordered_words)):
        if ordered_words[i+1] > return_words[1]:
            return_words.insert(0, return_words.pop(word))
    return return_words

    #mylist.insert(0, mylist.pop(5))

        
    #Lenght of the word only matters if there is a tie,
    #so go looking for ties after you set up all the data in the dictionary -or-
    #do a lookup when you are ordering the dictionary
    
    #3. Return the list

    # Returns tuple - index 0 string of word, index 1 the score of the word: tuple(x, y,)
    # If length of word1 == length of word2, tie break: 
    # Shortest length wins, unless length == 10 letters