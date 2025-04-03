"""
Resources:
Day 6 - Advent of Code 2024 (Solution). James Peralta.  https://youtu.be/6N_FY2UIguk?si=nJmOQzyefpymtqOP
Guard Gallivant [Day 6 - Advent of Code 2024 - Python]. 0xdf. https://www.youtube.com/watch?v=98M4F1agidQ
"""

class Solution:
    def day6(self):
        filename = "input.txt"
        grid = self.read_input(filename)
        for row in grid:
            print(row)
        startpt = self.findGuard(grid)
        print(startpt)
        outPathLength = self.findPath(grid, startpt)
        print("Length of Path: ", outPathLength)
        outObstacleCount = self.getCycle(grid, startpt)
        print("Obstacle Count: ", outObstacleCount)

    def getCycle(self, grid, start):
        NR = len(grid)
        NC = len(grid[0])
        count = 0

        for ro in range(NR):
            for co in range(NC):
                if grid[ro][co] != ".": continue
                grid[ro][co] = "#"
                if self.findCycle(grid, start):
                    count += 1
                grid[ro][co] = "."
        return count
    
    def findCycle(self, grid, start):
        NR = len(grid)
        NC = len(grid[0])

        current_row, current_col, current_nav = start
        orientation = {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}
        path = set()
        path.add((current_row, current_col, current_nav))
        
        while True:
            next_row = current_row + orientation[current_nav][0]
            next_col = current_col + orientation[current_nav][1]
            if not (0 <= next_row < NR and 0 <= next_col < NC):
                return False 
            if grid[next_row][next_col] != "#":
                if (next_row, next_col, current_nav) in path:
                    return True
                path.add((next_row, next_col, current_nav))
                current_row = next_row
                current_col = next_col
            if grid[next_row][next_col] == "#":
                current_nav = self.turnRight(current_nav)
                

        return obstacle_count

    def findPath(self, grid, start):
        NR = len(grid)
        NC = len(grid[0])

        current_row, current_col, current_nav = start
        orientation = {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}
        path = set()
        path.add((current_row, current_col))
        
        while 0 <= current_row < NR or 0 <= current_col < NC:
            next_row = current_row + orientation[current_nav][0]
            next_col = current_col + orientation[current_nav][1]
            if not (0 <= next_row < NR and 0 <= next_col < NC):
                break 
            if grid[next_row][next_col] != "#":    
                path.add((next_row, next_col))
                current_row = next_row
                current_col = next_col
            if grid[next_row][next_col] == "#":
                current_nav = self.turnRight(current_nav)
            
            # print(current_row, current_col, current_nav)
        
        return len(path)

    def turnRight(self, navigation):
        if navigation == "UP":
            return "RIGHT"
        elif navigation == "RIGHT":
            return "DOWN"
        elif navigation == "DOWN":
            return "LEFT"
        else:
            return "UP"

    def findGuard(self, grid):
        NR = len(grid)
        NC = len(grid[0])

        for r in range(NR):
            for c in range(NC):
                if grid[r][c] == "^":
                    return [r, c, "UP"]
        
        return -1

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
    solution.day6()