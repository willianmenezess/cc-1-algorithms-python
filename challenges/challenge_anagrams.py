def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right, array.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    if not first_string and not second_string:
        return ('', '', False)
    is_anagram = True
    if len(first_string) == len(second_string):
        for letter in first_string.lower():
            if letter not in second_string.lower():
                is_anagram = False
    else:
        is_anagram = False

    first_sorted_list = merge_sort(list(first_string.lower()))
    second_sorted_list = merge_sort(list(second_string.lower()))
    first_sorted = ''.join(first_sorted_list)
    second_sorted = ''.join(second_sorted_list)
    return (first_sorted, second_sorted, is_anagram)


if __name__ == '__main__':
    print(is_anagram('amoR', 'roma'))
    print(is_anagram('amor', 'amora'))
    print(is_anagram('', ''))
