"""
Resources:
Advent of Code 2024 | Day 3 Jackie's Python Solution. CS Jackie. https://www.youtube.com/watch?v=8_o4625JK50
"""

import re

class Solution:

    def day3(self):
        filename = "input.txt"
        instructions = self.read_input(filename)
        outSum = self.mulSum(instructions)
        print("Total Sum of Products: ", outSum)
        outActSum = self.activeMulSum(instructions)
        print("Total Sum of Active Products: ", outActSum)
    
    def activeMulSum(self, inputString):
        enabled = True
        pattern = r"mul\((\d+),(\d+)\)"
        totalSum = 0
        
        for line in inputString:
            for i in range(len(line)):
                if line[i:].startswith("do()"):
                    enabled = True
                if line[i:].startswith("don't()"):
                    enabled = False
                matches = re.match(pattern, line[i:])
                if matches is not None:
                    x, y = int(matches.group(1)), int(matches.group(2))
                    if enabled:
                        totalSum += (x * y)
        
        return totalSum


    def mulSum(self, inputString):
        pattern = r"mul\((\d+),(\d+)\)"
        totalSum = 0
        for element in inputString:
            matches = re.findall(pattern, element)
            for x,y in matches:
                totalSum += (int(x) * int(y))
        return totalSum
    
    def read_input(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            return lines
                
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

if __name__ == "__main__":
    solution = Solution()
    solution.day3()