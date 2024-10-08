# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# dynamic programming algo: yet to review


def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# Example Input:
nums = [10, 9, 2, 5, 3, 7, 101, 18]

# Example Output:
print(length_of_lis(nums))  # Output: 4
