# have a python dictiorary that as a key/value pair that represents a word and it's definition
# collect input from the user, input is a word
# check if the word is in the dictionary
# print de definition
#TODO: Instalar PyDictionary y volver a hacer el proyecto

def main():
    word_dictionary = {
        'hi': 'a way of greeting',
        "eyes": 'an organ for seeing',
        'earth': 'a planet in space'
    }
    while True:
        word = input("Enter a word: ")
        if word == '':
            breack
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])


main()
