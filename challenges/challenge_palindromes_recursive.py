def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if not isinstance(word, str) or word == '':
        return False
    # caso de parada
    if low_index >= high_index:
        return True
    # caso recursivo
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False


if __name__ == '__main__':
    word = ''
    result = is_palindrome_recursive(word, 0, len(word) - 1)
    print(result)
