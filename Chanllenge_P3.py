from Challenge_P1 import string_normalize


def ngrams_genarate(input_string):
    word_normalize = string_normalize(input_string)
    word_array = word_normalize.split()
    unigrams = []
    bigrams = []
    trigrams = []
    arr_length = len(word_array)

    for item in word_array:
        unigrams.append([item])

    if arr_length <= 2:
        bigrams.append(word_array)
    else:
        for i in range(0, arr_length - 1):
            bigrams.append([word_array[i], word_array[i + 1]])

    if arr_length <= 3:
        trigrams.append(word_array)
    else:
        for i in range(0, arr_length - 2):
            trigrams.append([word_array[i], word_array[i + 1], word_array[i + 2]])

    return unigrams, bigrams, trigrams


if __name__ == '__main__':
    input_str = "I like   to      Program   in Python Language. Don’t you?"
    unigrams, bigrams, trigrams = ngrams_genarate(input_str)
    print("unigrams= ", unigrams)
    print("bigrams = ", bigrams)
    print("trigrams = ", trigrams)
