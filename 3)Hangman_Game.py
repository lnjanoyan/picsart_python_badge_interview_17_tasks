import random

f = open(r"C:\Users\Admin\Desktop\words.txt")
word = random.choice([word for word in f])[:-1]
print('Welcome to Hangman game, try to guess the word ')
limit = 0
guess = '_' * len(word)
print(guess)
while guess != word:
    letter = input('Enter a letter: ')
    if letter in word:
        cnt = word.count(letter)
        start = 0
        for i in range(cnt):
            ind = word.index(letter, start)
            guess = guess[:ind] + letter + guess[ind + 1:]
            start += ind
        print(guess)

    elif limit <= 5:
        print("Wrong answer!")
        limit += 1
        print('{} incorrect answer(s), You have {} more chance(s)'.format(limit, 6 - limit))
    else:
        print('Game ended! You lose!  Word was {} '.format(word))
        break
else:
    print('Congratulations!!! You WIN !!!')
