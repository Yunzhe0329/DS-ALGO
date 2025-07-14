def is_palindrome(s : str) -> bool :
    if not s:
        return False

    return s == s[::-1]
        

print(is_palindrome("12321"))


def find_max(nums : list[int]) -> int:
    if not nums:
        return False
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max
print(find_max([3, 5, 2, 9, 1]))
        
