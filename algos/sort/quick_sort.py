

def quick_sort(values):
    """
    
    """
    if len(values) <= 1:
        return values
    
    left, pivot_val, right = pivot(values)
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)

    return merge(left_sorted, pivot_val, right_sorted)


def pivot(values):
    
    if not values:
        return values

    pivot_val = values[0]
    left = []
    right = []

    for val in values[1:]:
        if val < pivot_val:
            left.append(val)
        else:
            right.append(val)
    
    return left, pivot_val, right


def merge(left: list, pivot_val: int, right: list):
    print(f"Left: {left}, pivot: {pivot_val}, right: {right}")

    merged = left
    merged.append(pivot_val)
    merged.extend(right)

    return merged


if __name__ == "__main__":
    
    values_list = [27, 98, 13, 10, 3, 165]

    left, pivot_val, right = pivot(values_list)
    print(left, pivot_val, right)

    merged = merge(left, pivot_val, right)
    print(merged)