def get_words_starting_with_vowel(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_words = [word for word in words if word[0].lower() in vowels]
    return vowel_words

input_words = ["apple", "banana", "orange", "bear", "cat"]
result = get_words_starting_with_vowel(input_words)
print(result)