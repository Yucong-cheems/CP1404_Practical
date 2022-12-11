"""
hex_colours
Estimate: 15 minutes
Actual:   18 minutes
"""


dictionary_count = {"dog": 2, "cat": 3, "lion": 5, "whale": 6, "tiger": 8}
print(dictionary_count)

input_word = input("Enter a word: ")

while input_word != " ":
    if input_word in dictionary_count:
        print(input_word, ":", dictionary_count[input_word])

    else:
        print("the word is not in the dictionary")

    input_word = input("Enter a word: ")
