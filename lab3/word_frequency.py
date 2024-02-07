def word_frequency(input_string):
    words = input_string.split()
    word_freq = {}
    for word in words:
        word = word.strip(",.!?").lower()  
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq


input_string = "Hello, how are you? This is a test. Hello, world!"
frequency_dict = word_frequency(input_string)
print("Word frequencies in the input string:")
for word, freq in frequency_dict.items():
    print(word, ":", freq)