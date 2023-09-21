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


def find_duplicate(nums):
    """Faça o código aqui."""
    if len(nums) <= 1 or not isinstance(nums, list):
        return False
    ordered_nums = merge_sort(nums)

    for index in range(len(ordered_nums) - 1):
        if not isinstance(ordered_nums[index], int) or ordered_nums[index] < 0:
            return False
        if ordered_nums[index] == ordered_nums[index + 1]:
            return ordered_nums[index]
    return False


if __name__ == "__main__":
    print(find_duplicate([1, 2, 6, 4, 5, 3, 7, 9, 9, 8]))  # 9
    print(find_duplicate([1, 2, 3, 4, 5, 7, 7, 7]))  # 7
    print(find_duplicate([1]))  # False
    print(find_duplicate([1, 1]))  # 1
    print(find_duplicate([1, 2, 3, 4, -5, -5, 7, 8, 9, 9]))  # False
    print(find_duplicate([]))  # False
    print(find_duplicate([1, 2, 3, 4, 5, 6, 7]))  # False
    print(find_duplicate(['a', 'b']))  # False
    print(find_duplicate(['a', 'a']))  # False
