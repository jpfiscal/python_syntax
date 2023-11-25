def print_upper_words(words, must_start_with={"h","y"}):
    """accepts a list of strings and prints each entry in the list in upper case on separate lines."""
    for word in words:
        for letter in must_start_with:
            print(word.upper()) if (word.startswith(letter.lower()) or word.startswith(letter.upper())) else next
    
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words(["hello", "exquisite!", "goodbye", "Echo", "yes"], must_start_with={"h","e", "y"})