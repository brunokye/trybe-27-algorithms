def find_duplicate(nums):
    seen = set()

    for num in nums:
        if isinstance(num, str) or num < 0:
            return False
        if num in seen:
            return num
        seen.add(num)

    return False
