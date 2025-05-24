# Write a function that have an array of size n and sort the array in place such that all 0s are at the beginning, followed by 1s, and then 2s.
def sort_colors(nums):
    if not nums:
        return

    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

c1=sort_colors([2, 0, 2, 1, 1, 0])
print(c1)  # Output: [0, 0, 1, 1, 2, 2]