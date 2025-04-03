"""
Resources:
Advent of Code 2024 | Day 1 Jackie's Python Solution. CS Jackie. https://www.youtube.com/watch?v=CM70wu-STZU&t=108s
"""

import math

class Solution():
    
    def day1(self):
        filename = 'input.txt'
        list1, list2 = self.extractlists(filename)
        outDist = self.totalDistance(list1, list2)
        print("totalDistance: ", outDist)

        outScore = self.similarityScore(list1, list2)
        print("similarityScore: ", outScore)
    
    def similarityScore(self, list1, list2):
        num_count = {}
        totalScore = 0

        for num in list2:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        for num in list1:
            if num in num_count:
                score = num * num_count[num]
            else:
                score = 0
            totalScore += score
        
        return totalScore

    def totalDistance(self, list1, list2):
        sorted1 = sorted(list1)
        sorted2 = sorted(list2)
        totalDist = 0

        for i in range(len(sorted1)):
            totalDist += math.fabs(sorted2[i]-sorted1[i])
        
        return totalDist
    
    def extractlists(self, file_path):
        list1 = []
        list2 = []

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if line.strip():
                        numbers = line.split()
                        if len(numbers) == 2:
                            list1.append(int(numbers[0]))
                            list2.append(int(numbers[1]))

        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

        return list1, list2
    
if __name__ == "__main__":
    solution = Solution()
    solution.day1()