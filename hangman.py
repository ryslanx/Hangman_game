import random
print("H A N G M A N\n")
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
list_word = list(word)
first_time_flag = True
letter_list = []
inputted_list = []
attempts = 8
for index in range(len(word)):
    letter_list.append('-')
while True:
    while first_time_flag or attempts == 0:
        user_input = input('Type "play" to play the game, "exit" to quit:')
        if user_input == 'exit':
            exit()
        if user_input == 'play':
            first_time_flag = False
            break
    new_string = ''.join(letter_list)
    print(new_string)
    inputted_letter = input("Input a letter:")
    ascii_check = inputted_letter.isascii()
    lower_check = inputted_letter.islower()
    if inputted_letter in inputted_list:
        print('You already typed this letter\n')
        continue
    if len(inputted_letter) != 1:
        print("You should input a single letter\n")
        continue
    elif not ascii_check or not lower_check:
        print("It is not an ASCII lowercase letter\n")
        continue
    inputted_list.append(inputted_letter)
    if inputted_letter in word:
        for _ in range(list_word.count(inputted_letter)):
            word_index = list_word.index(inputted_letter)
            list_word[word_index] = '-'
            letter_list[word_index] = inputted_letter
        print("\n")
        if '-' not in letter_list:
            print(word)
            print("You guessed the word!\nYou survived!\n")
            break
    else:
        attempts -= 1
        if attempts == 0:
            print("No such letter in the word\nYou are hanged!\n")
        else:
            print("No such letter in the word\n")