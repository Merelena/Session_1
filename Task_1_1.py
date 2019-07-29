# Looking for ' and " and changing to vice versa
def mod(text:str) -> str:
    tmp = text.maketrans('\'\"', '\"\'')
    result = text.translate(tmp)
    return result