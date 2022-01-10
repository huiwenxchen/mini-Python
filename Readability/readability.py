from cs50 import get_string

    
def main():
    # Prompt user to input text
    text = get_string("Text: ")

    # Calculate the Coleman-Liau value
    L = lettercount(text) / wordcount(text) * 100
    S = sentencecount(text) / wordcount(text) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Print the corresponding grade level 
    if index >= 1 and index <= 16:
        print(f"Grade: {index}")

    elif index < 1:
        print("Before Grade 1")

    else: 
        print("Grade 16+")


# Function to calculate the number of letters
def lettercount(text):
    # Initialize the number of letters 
    letters = 0
    n = len(text)
    # Iterate through all characters in the text input 
    for i in range(n):
        # Count the number of alphabetic characters
        if text[i].isalpha():
            letters += 1
    return letters


# Function to calculate the number of words
def wordcount(text):
    # Initialize the number of words and find the length 
    words = 1
    n = len(text)
    # Iterate through all characters in the text input 
    for i in range(n):
        # Count the space to calculate the number of words
        if text[i].isspace():
            words += 1
    return words


# Function to calculate the number of sentences
def sentencecount(text):
    # Initialize the number of sentences
    sentences = 0
    n = len(text)
    # Check the punctation to calculate the number of sentences
    for i in range(n):
        if text[i] in ["!", "?", "."]:
            sentences += 1
    return sentences


main()
