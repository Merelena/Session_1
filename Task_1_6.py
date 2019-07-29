# Looking for the longest word
def longest_word(text: str):
    return max(text.split(' '), key=len)


print(longest_word(input('Please, enter your text: ')))