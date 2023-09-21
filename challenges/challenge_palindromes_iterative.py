def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if not isinstance(word, str) or word == '':
        return False
    low_index = 0
    high_index = len(word) - 1

    while high_index >= low_index:
        if word[low_index] != word[high_index]:
            return False
        low_index += 1
        high_index -= 1
    return True


if __name__ == '__main__':
    word = 'socos'
    result = is_palindrome_iterative(word)
    print(result)
