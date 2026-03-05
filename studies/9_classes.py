import statistics

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26, 59, -2]


class Stat:
    def __init__(self):
        pass
    
    def median(self, nums):
        
        return statistics.median(nums)

    def range(self, nums):
        max_num = max(nums)
        min_num = min(nums)
        return max_num - min_num 

    def max_min_nums(self, nums):
        max_num = max(nums)
        min_num = min(nums)
        return f"Minimum number is {min_num}, also the maximum is {max_num}"

    def sum(self, nums):
        summary = 0
        for i in nums:
            summary += i
        return summary
    
    def odd_or_even_len(self, nums):
        nums_len = len(nums)
        if (nums_len % 2) == 0:
            return "Even count"
        elif (nums_len % 2) != 0:
            return "Odd count"

stats = Stat()

print(stats.median(ages))
print(stats.range(ages))
print(stats.max_min_nums(ages))
print(stats.sum(ages))
print(stats.odd_or_even_len(ages))