# Given a sorted array of n integers, write a function to search for a target value
# using the Binary Search algorithm. The function should return the index of the target
# if it is found in the array. If the target is not found, return -1.

# Binary Search is an efficient algorithm for finding an item from a sorted list of items.
# It works by repeatedly dividing the portion of the array that could contain the item in
# half until you've narrowed down the possible locations to just one.

# intuition 0: the list has to be sorted for this to work
# intuition 1: two pointers are created at the extremes
# intuition 2: mid value is calculated and value @ mid is checked with target
# intuition 3: left or right is moved towards mid according to above chek


def binary_search(nums, target):
    pass
    # start by creating 2 pointers
    # 0, 8
    # while the right doesn't cross the left
        # get the mid value of the range

        # // will give me floor quotient
        # 0 + (8 - 0) // 2 = 4
        # 5 + (8 - 5) // 2 = 4

        # intuition:

        # Check if target is present at mid

        # If target is greater, ignore the left half
            # move the left to mid + 1

        # If target is smaller, ignore the right half
            # move the right to mid -1

    # Target is not present in the array


# Example Input:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

# Example Output:
index = binary_search(nums, target)
print(
    f"Target {target} is found at index {index}"
)  # Output: Target 7 is found at index 6
