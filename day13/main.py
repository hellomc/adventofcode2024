"""
Resources
Advent of Code 2024 | Day 13 "Claw Contraption". HyperNeutrino. https://www.youtube.com/watch?v=-5J-DAsWuJc
"""

import re

class Solution:
    def day13(self):
        filename = "input.txt"
        games = self.read_input(filename)
        # print(games)
        outTokens = self.getTokens(games)
        print("Num Tokens:", outTokens)
        outTokens2 = self.getTokens2(games)
        print("Num Tokens:", outTokens2)
    
    def getTokens2(self, games):
        total = 0
        for game in games:
            # print(game)
            ax, ay, bx, by, px, py = game
            px += 10000000000000
            py += 10000000000000
            # print(px, py)
            count_a = ((px * by) - (py * bx)) / ((ax * by) - (ay * bx))
            count_b = (px - (count_a * ax)) / bx
            if count_a % 1 == count_b % 1 == 0:
                total += int(count_a * 3 + count_b)

        return total

    def getTokens(self, games):
        total = 0
        for game in games:
            # print(game)
            ax, ay, bx, by, px, py = game
            count_a = ((px * by) - (py * bx)) / ((ax * by) - (ay * bx))
            count_b = (px - (count_a * ax)) / bx
            if count_a % 1 == count_b % 1 == 0:
                total += int(count_a * 3 + count_b)

        return total
    
    def read_input(self, file_path):
        games = []
        try:
            with open(file_path, 'r') as file:
                data = file.read().split("\n\n")
                # print(data)
                for block in data:
                    game = list(map(int, re.findall(r"\d+", block)))
                    games.append(game)
                return games  
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

if __name__ == "__main__":
    solution = Solution()
    solution.day13()