with open("words-list.txt") as file:
    words = file.read().splitlines()

correct_letters = ["", "", "", "", ""]

possible_letters = []

impossible_letters = []

possible_words = []

impossible_words = []

print("soare")

for i in range(6):
    correct_words = []

    for i in range(5):
        correct = input("Enter if correct: ")
        if correct_letters[i] == "":
            correct_letters[i] = correct
        possible = input("Enter if possible: ")
        if possible not in possible_letters and possible != "":
            possible_letters.append(possible)
        impossible = input("Enter if not possible: ")
        if impossible not in impossible_letters and impossible != "":
            impossible_letters.append(impossible)


    for word in words:
        possible_letter_count = 0
        possible_letter_counts = len(possible_letters)
        for possible_letter in possible_letters:
            if possible_letter in word:
                possible_letter_count += 1
        if possible_letter_count == possible_letter_counts:
            possible_words.append(word)

    for possible_word in possible_words:
        impossible_word_bool = False
        for impossible_letter in impossible_letters:
            if impossible_letter in possible_word:
                impossible_word_bool = True
        if impossible_word_bool == False:
            impossible_words.append(possible_word)

    for impossible_word in impossible_words:
        correct_letter_count = 0
        chars = [char for char in impossible_word]
        for correct_letter in correct_letters:
            char_index = correct_letters.index(correct_letter)
            if correct_letter == chars[char_index]:
                correct_letter_count += 1
        nonblank_correct_letters = [i for i in correct_letters if i != ""]
        if correct_letter_count == len(nonblank_correct_letters):
            if impossible_word not in correct_words:
                correct_words.append(impossible_word)

    print(correct_words)
    
    if len(correct_words) == 1:
        break
