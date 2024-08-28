# Time complexity: logarithmic, O(log n)
# Space complexity: 

def binary_iter_search(values: list, target: int, comment_flg: bool) -> int:
    """
    Function that implements an iterative binary search algorithm on a ascending sorted list of values
    Parameters:
        values: a list of sorted values to search through (sorted ascending)
        target: the value to search for
        comment_flg: flag indicating whether the print debug comments out or not
    Returns:
        The index of the target value if it exists in the given set of values, None otherwise
    """

    # Constant time and space complexity O(1)
    start = 0
    end = len(values) - 1
    midpoint = (end - start) // 2

    # Logarithmic time complexity O(log n)
    while end > start:
        print(f"Start point: {start}, end point: {end}: midpoint: {midpoint}") if comment_flg else None
        print(f"Value start point: {values[start]}, value end point: {values[end]}, value midpoint: {values[midpoint]}") if comment_flg else None
        if values[midpoint] == target:
            print(f"\nTarget value ({target}) found at index {midpoint}") if comment_flg else None
            return midpoint
        elif values[midpoint] > target:
            print(f"Value of midpoint ({values[midpoint]}) is greater than target {target}\n") if comment_flg else None
            end = midpoint
            midpoint = (end - start) // 2
        elif values[midpoint] < target:
            print(f"Value of midpoint ({values[midpoint]}) is less than target {target}\n") if comment_flg else None
            start = midpoint
            midpoint = ((end - start) // 2) + start


if __name__ == "__main__":
    assert binary_iter_search([1, 2, 3, 4, 5], 4, False) == 3
    assert binary_iter_search([i for i in range(100)], 89, False) == 89
    assert binary_iter_search([i * 2 for i in range(100)], 100, False) == 50
    assert binary_iter_search([i * 3 for i in range(100)], 198, True) == 198 / 3
    print(f"All checks passed")