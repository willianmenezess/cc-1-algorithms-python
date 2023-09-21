def find_duplicate(nums):  # O(n log n) + O(n) = O(2n) = O(n)
    """Faça o código aqui."""
    if len(nums) <= 1 or not isinstance(nums, list):
        return False
    ordered_nums = sorted(nums)

    for index in range(len(ordered_nums) - 1):  # O(n)
        if isinstance(ordered_nums[index], str) or ordered_nums[index] < 0:
            return False
        if ordered_nums[index] == ordered_nums[index + 1]:
            return ordered_nums[index]
    return False


# if __name__ == "__main__":
#     print(find_duplicate([1, 2, 6, 4, 5, 3, 7, 9, 9, 8]))  # 9
#     print(find_duplicate([1, 2, 3, 4, 5, 7, 7, 7]))  # 7
#     print(find_duplicate([1]))  # False
#     print(find_duplicate([1, 1]))  # 1
#     print(find_duplicate([1, 2, 3, 4, -5, -5, 7, 8, 9, 9]))  # False
#     print(find_duplicate([]))  # False
#     print(find_duplicate([1, 2, 3, 4, 5, 6, 7]))  # False
#     print(find_duplicate(['a', 'b']))  # False
#     print(find_duplicate(['a', 'a']))  # False
