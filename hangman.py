import random

with open("words.txt", "r") as file:
    allText = file.read() 
    words = list(map(str, allText.split()))
    word = random.choice(words)

word = word.lower()
starting_word = word
helping_word = ""
print("I wanna play a game!\nI came up with a word that has", len(word), "letters.\nYou guess word or letter.\nYou have 15 tries before I hang you!\nGood luck!")
print(helping_word)
for i in range(15, -1, -1):
    guess = input("Your guess(" +str(i) + " more):")
    tmp_list = []
    if len(guess) == 1 and guess in word:
        #Counts how many of letters are there in word
        for j in word:
            if j == guess:
                helping_word += j
                tmp_list.append(j)
        print("Your guess is in my word", len(tmp_list), "times!")
        word = word.replace(guess, "", len(tmp_list))
        if len(word) == 0:
            print("You got every letter what is the word?")

    elif guess == word:
        print("Congrats!")
        break
    else:
        print("Nope!")
        continue
    print("Guessed letters: " + helping_word)


print("The word was \"" + starting_word + "\"")