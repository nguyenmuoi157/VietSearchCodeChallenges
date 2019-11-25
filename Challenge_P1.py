import re


def string_normalize(input_string):
    regex = r"[^a-zA-Z0-9]+"
    result = re.sub(regex, " ", input_string)
    regex = r"\b *a *\b|\b *the *\b|\b *on *\b|\b *in *\b|\b *an *\b|\b *to *\b"
    result = re.sub(regex, " ", result)
    result = result.strip().lower()
    word_arr = result.split(' ')
    word_arr.sort()
    return " ".join(word_arr)


if __name__ == '__main__':
    input_str = "I like   to      Program   in Python Language. Don’t you?"
    output = string_normalize(input_str)
    print(output)
