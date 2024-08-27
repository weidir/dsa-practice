# Time complexity: linear, O(n)
# Space complexity: linear, O(n)

def linear_search(values: list, target) -> int:
    """
    Function that implements a linear search algorithm on a list of values
    Parameters:
        values: a list of values to search through
        target: the value to search for
    Returns:
        The index of the target value if it exists in the given set of values, None otherwise
    """

    for idx, value in enumerate(values):
        if value == target:
            return idx
        
    return None