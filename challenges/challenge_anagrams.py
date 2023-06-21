def is_anagram(first_string, second_string):
    if first_string == '' and second_string == '':
        return ('', '', False)

    string_a = sort_word(first_string)
    string_b = sort_word(second_string)
    verify = string_a == string_b

    return (string_a, string_b, verify)


def sort_word(word):
    characters = list(word.lower())

    quicksort(characters, 0, len(characters) - 1)
    sorted_word = "".join(characters)

    return sorted_word


def quicksort(word, start, end):
    if start < end:
        p = partition(word, start, end)
        quicksort(word, start, p - 1)
        quicksort(word, p + 1, end)


def partition(word, start, end):
    pivot = word[end]
    delimiter = start - 1

    for index in range(start, end):
        if word[index] <= pivot:
            delimiter = delimiter + 1
            word[delimiter], word[index] = word[index], word[delimiter]

    word[delimiter + 1], word[end] = word[end], word[delimiter + 1]

    return delimiter + 1


# def sort_word(word):
#     characters = list(word)
#     n = len(characters)

#     for ordered_letters in range(n):
#         sorted = True

#         for letter in range(n - ordered_letters - 1):
#             if (characters[letter] > characters[letter + 1]):
#                 temp = characters[letter]
#                 characters[letter] = characters[letter + 1]
#                 characters[letter + 1] = temp

#                 sorted = False
#         if sorted:
#             break

#     sorted_word = "".join(characters)

#     return sorted_word
