# Time complexity: logarithmic, O(log n)
# Space complexity: logarithmic, O(log n)

def binary_rec_search(values: list, target: int, idx_offset: int = 0, comment_flg: bool = False) -> int:
    """
    Function that implements a recursive binary search algorithm on a ascending sorted list of values
    Parameters:
        values: a list of sorted values to search through (sorted ascending)
        target: the value to search for
        idx_offset: value to keep track of true index by offsetting the index of given subarrays
        comment_flg: flag indicating whether the print debug comments out or not
    Returns:
        The index of the target value if it exists in the given set of values, None otherwise
    """

    # Constant time and space complexity O(1)
    start = 0
    end = len(values) - 1
    midpoint = len(values) // 2
    print(f"Start point: {start}, end point: {end}: midpoint: {midpoint}, offset: {idx_offset}") if comment_flg else None
    print(f"Value start point: {values[start]}, value end point: {values[end]}, value midpoint: {values[midpoint]}") if comment_flg else None

    if len(values) == 0:
        print("No values left to return, target did not exist in values array, halting function") if comment_flg else None
        return None
    elif values[midpoint] == target:
        print(f"\nTarget value ({target}) found at index {midpoint + idx_offset} (midpoint: {midpoint}, index offset: {idx_offset})") if comment_flg else None
        return midpoint + idx_offset
    else:
        if values[midpoint] > target:
            print(f"Value of midpoint ({values[midpoint]}) is greater than target {target}") if comment_flg else None
            print(f"New values array: {values[:midpoint]}\n") if comment_flg else None
            return binary_rec_search(values=values[:midpoint], target=target, idx_offset=idx_offset, comment_flg=comment_flg)
        elif values[midpoint] < target:
            print(f"Value of midpoint ({values[midpoint]}) is less than target {target}") if comment_flg else None
            print(f"New values array: {values[midpoint + 1:]}\n") if comment_flg else None
            return binary_rec_search(values=values[midpoint + 1:], target=target, idx_offset=idx_offset + midpoint + 1, comment_flg=comment_flg)


if __name__ == "__main__":
    assert binary_rec_search([1, 2, 3, 4, 5], 4, 0, False) == 3
    assert binary_rec_search([i for i in range(100)], 89, 0, False) == 89
    assert binary_rec_search([i * 2 for i in range(100)], 100, 0, False) == 50
    assert binary_rec_search([i * 3 for i in range(100)], 198, 0, False) == 198 / 3
    print(f"All checks passed")