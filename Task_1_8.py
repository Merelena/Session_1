# Creating pairs of words
def pairs(words: list):
    result = []
    length = len(words)
    for index, item in enumerate(words):
        if index != length - 1:
            temp_tuple = item, words[index+1]
            result.append(temp_tuple)
    return result


print(pairs(['o', 'k', 'ey', 'e']))