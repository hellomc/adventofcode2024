"""
Resources:
Advent of Code 2024 | Day 08 "Resonant Collinearity". HyperNeutrino. https://www.youtube.com/watch?v=HI2DbMq-t-Y
"""


class Solution:
    def day8(self):
        filename = "input.txt"
        grid = self.read_input(filename)
        for row in grid:
            print(row)
        antennas = (self.findantennas(grid))
        print(antennas)
        outNodes = self.getantinodes(grid,antennas)
        print("Num of Antinodes: ", outNodes)
        outNodes2 = self.getantinodes2(grid, antennas)
        print("Num of Antinodes2: ", outNodes2)

    def getantinodes2(self, grid, antennas):
        NR = len(grid)
        NC = len(grid[0])
        antinodes = set()

        for array in antennas.values():
            for i in range(len(array)):
                for j in range(len(array)):
                    if i == j: continue
                    r1, c1 = array[i]
                    r2, c2 = array[j]
                    dr = r2 - r1
                    dc = c2 - c1
                    r = r1
                    c = c1
                    while (0 <= r < NR and 0 <= c < NC):
                        antinodes.add((r, c))
                        r += dr
                        c += dc
        
        num_antinodes = len(antinodes)

        return num_antinodes
    
    def getantinodes(self, grid, antennas):
        NR = len(grid)
        NC = len(grid[0])
        antinodes = set()

        for array in antennas.values():
            for i in range(len(array)):
                for j in range(i+1, len(array)):
                    r1, c1 = array[i]
                    r2, c2 = array[j]
                    antinodes.add((2 * r1 - r2, 2 * c1 - c2))
                    antinodes.add((2 * r2 - r1, 2 * c2 - c1))
        
        num_antinodes = len([0 for r, c in antinodes if 0 <= r < NR and 0 <= c < NC])

        return num_antinodes
    
    def findantennas(self, grid):
        NR = len(grid)
        NC = len(grid[0])
        antennas = {}

        for r in range(NR):
            for c in range(NC):
                char = grid[r][c]
                if char != ".":
                    if char not in antennas: antennas[char] = []
                    antennas[char].append((r,c))
        
        return antennas

    def read_input(self, file_path):
        grid = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    row = list(line.strip())
                    grid.append(row)
            return grid
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

if __name__ == "__main__":
    solution = Solution()
    solution.day8()
