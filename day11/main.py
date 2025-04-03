"""
Resources

Plutonian Pebbles [Day 11 - Advent of Code 2024 - Python]. 0xdf. https://www.youtube.com/watch?v=JxIAqiUJraE
Advent of Code 2024 Day 11. Jonathan Paulson. https://www.youtube.com/watch?v=dfZ4uxqgT6o&t=7s
"""
import sys
from functools import lru_cache

class Solution:
    def day11(self):
        sys.setrecursionlimit(10**6)
        filename = "input.txt"
        stones = self.read_input(filename)
        # print(stones)
        blink_num = 25
        new_stones = self.blink(stones, blink_num)
        print(len(new_stones))
        num_stones75 = sum(self.blink2(stone, 75) for stone in stones)
        print(num_stones75)
    
    @lru_cache(maxsize=None)
    def blink2(self, stone, blink_num):
        dp = {}
        if (stone, blink_num) in dp:
            return dp[(stone, blink_num)]
        if blink_num == 0:
            ret = 1
        elif stone == 0:
            ret = self.blink2(1, blink_num-1)
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            len_str_stone = len(str_stone)
            left = int(str_stone[:(len_str_stone // 2)])
            right = int(str_stone[(len_str_stone // 2):])
            ret = self.blink2(left, blink_num - 1) + self.blink2(right, blink_num - 1)
        else:
            ret = self.blink2(stone * 2024, blink_num - 1)
        dp[(stone, blink_num)] = ret
        return ret
    
    def blink(self, stones, blink_num):
        for _ in range(blink_num):
            new_stones = []
            for stone in stones:
                if stone == 0:
                    new_stones.append(1)
                elif len(str(stone)) % 2 == 0:
                    str_stone = str(stone)
                    mid = len(str_stone) // 2
                    new_stones.append(int(str_stone[:mid]))
                    new_stones.append(int(str_stone[mid:]))
                else:
                    new_stones.append(stone * 2024)
            stones = new_stones

        return stones

    def read_input(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = file.read().split(" ")
                data = list(map(int, data))
            return data
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

if __name__ == "__main__":
    solution = Solution()
    solution.day11()