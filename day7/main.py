"""
Resources:
Bridge Repair [Day 7 - Advent of Code 2024 - Python]. 0xdf. https://youtu.be/Np6ti3t36XA?si=1YDFnYp2vpUxT2GP
"""

class Solution:
    def day7(self):
        filename = "input.txt"
        values = self.read_input(filename)
        # print(values)
        sum1 = 0
        sum2 = 0
        for group in values:
            target = group[0]
            nums = group[1][:]
            if self.isValid(target, nums[:]):
                sum1 += target
            if self.isValidCat(target, nums[:]):
                sum2 += target
        print("Sum of Valid Tests:", sum1)
        print("Sum of Valid2 Tests:", sum2)
    
    def isValidCat(self, target, nums):
        if len(nums) == 1:
            return target == nums[0]
        num = nums.pop()
        
        if target / num == target // num:
            if self.isValidCat(target // num, nums[:]):
                return True
        if target - num >= 0:
            if self.isValidCat(target - num, nums[:]):
                return True
        
        target_str = str(target)
        num_str = str(num)
        if target_str.endswith(num_str) and len(target_str) > len(num_str):
            new_target = int(target_str[:-len(num_str)])
            if self.isValidCat(new_target, nums[:]):
                return True
        return False
    
    def isValid(self, target, nums):
        if len(nums) == 1:
            return target == nums[0]
        num = nums.pop()
        if target / num == target // num:
            if self.isValid(target // num, nums[:]):
                return True
        if target - num >= 0:
            if self.isValid(target - num, nums[:]):
                return True

    def read_input(self, file_path):
        values = []
        try:
            with open(file_path, 'r') as file:
                lines = list(map(str.strip, file.readlines()))
                for line in lines:
                    target = int(line.split(":")[0])
                    nums = list(map(int, line.split(": ")[1].split(" ")))
                    values.append((target, nums))
            return values
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

if __name__ == "__main__":
    solution = Solution()
    solution.day7()