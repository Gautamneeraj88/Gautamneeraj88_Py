"""
10.Write a function that takes a sentence as input from the user and calculates the frequency of each letter.
Use a variable of dictionary type to maintain the count.
"""
all_freq = {}
def frequency(sentence):
    for i in sentence:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

sentence = input("Enter your sentence: \n")
frequency(sentence)
print(all_freq)