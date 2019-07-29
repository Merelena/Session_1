# Making a tuple
def get_digits(num: int) -> list:
    return tuple(str(num))


print(get_digits(12345465))