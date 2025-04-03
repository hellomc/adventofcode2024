"""
Resources:
Advent of Code 2024 | Day 04 "Ceres Search". HyperNeutrino. https://www.youtube.com/watch?v=HrsG_e7A0rw&t=367s
"""

class Solution:
    def day4(self):
        filename = "input.txt"
        grid = self.read_input(filename)
        print(grid)
        print(len(grid), len(grid[0]))
        outXCount = self.searchX(grid)
        print("XMAS Count: ", outXCount)
        outAcount = self.searchA(grid)
        print("SHAPE X Count: ", outAcount)

    def searchX(self, grid):
        NR = len(grid)
        NC = len(grid[0])
        print(NR, NC)
        count = 0

        for r in range(NR):
            for c in range(NC):
                if grid[r][c] != "X": continue
                directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                for dr, dc in directions:
                    if not (0 <= r+3*dr < NR and 0 <= c+3*dc < NC): continue
                    if grid[r+dr][c+dc] == "M" and grid[r+2*dr][c+2*dc] == "A" and grid[r+3*dr][c+3*dc] == "S":
                        count += 1
        
        return count

    def searchA(self, grid):
        NR = len(grid)
        NC = len(grid[0])
        count = 0

        for r in range(1, NR-1):
            for c in range(1, NC-1):
                if grid[r][c] != "A": continue
                corners = [grid[r-1][c-1], grid[r-1][c+1], grid[r+1][c+1], grid[r+1][c-1]]
                if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                    count += 1
        
        return count
    
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
    solution.day4()