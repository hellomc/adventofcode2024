"""
Resources
Advent of Code 2024 | Day 10 "Hoof It". HyperNeutrino. https://www.youtube.com/watch?v=layyhtQQuM0

BFS approach with deque.
"""

from collections import deque

class Solution:
    def day10(self):
        filename = "input.txt"
        grid = self.read_input(filename)
        for row in grid:
            print(row)
        loc_trailheads = self.getTrailheads(grid)
        print("Loc Trailheads: ", loc_trailheads)
        sumscore = 0
        ratingscore = 0
        for trailhead in loc_trailheads:
            sumscore += len(self.score(grid, trailhead[0], trailhead[1]))
            ratingscore += self.ratings(grid, trailhead[0], trailhead[1])
        print("Sum of Scores: ", sumscore)
        print("Ratings: ", ratingscore)

    def ratings(self, grid, r, c):
        NR = len(grid)
        NC = len(grid[0])
        q = deque([(r,c)])
        visited = {(r, c): 1}
        trails = 0
        while len(q) > 0:
            cr, cc = q.popleft()
            if grid[cr][cc] == 9:
                trails += visited[(cr, cc)]
            for nr, nc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
                if not (0 <= nr < NR and 0 <= nc < NC): continue
                if grid[nr][nc] != (grid[cr][cc] + 1): continue
                if (nr, nc) in visited:
                    visited[(nr, nc)] += visited[(cr, cc)]
                    continue
                visited[(nr, nc)] = visited[(cr, cc)]
                q.append((nr, nc))
        
        return trails  


    def score(self, grid, r, c):
        NR = len(grid)
        NC = len(grid[0])
        q = deque([(r,c)])
        visited = {(r, c)}
        summits = set()
        while len(q) > 0:
            cr, cc = q.popleft()
            for nr, nc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
                if not (0 <= nr < NR and 0 <= nc < NC): continue
                if grid[nr][nc] != (grid[cr][cc] + 1): continue
                if (nr, nc) in visited: continue
                visited.add((nr, nc))
                if grid[nr][nc] == 9:
                    summits.add((nr,nc))
                else:
                    q.append((nr, nc))
        print(summits)
        return summits


    def getTrailheads(self, grid):
        trailheads = []
        NR = len(grid)
        NC = len(grid[0])

        for r in range(NR):
            for c in range(NC):
                if grid[r][c] == 0:
                    trailheads.append((r, c))
        
        return trailheads
        

    # def findPath(self, grid):
    #     NR = len(grid)
    #     NC = len(grid[0])
    #     path_count = 0

    #     for r in range(NR):
    #         for c in range(NC):
    #             if grid[r][c] != 0: continue
    #             self.dfs(grid, (r, c), 0)
    #             path_count += 1
        
    #     return path_count

    # def dfs(self, grid, start_pt, height):
    #     NR = len(grid)
    #     NC = len(grid[0])
    #     r = start_pt[0]
    #     c = start_pt[1]
    #     visited = [(r, c)]
    #     height += 1
    #     # neighbors = []
    #     directions = {"UP": (-1, 0),
    #                   "RIGHT": (0, 1),
    #                   "DOWN": (1, 0),
    #                   "LEFT": (0, -1)}
        
    #     while height <= 9:
    #         for dr, dc in directions.values():
    #             nr = r + dr
    #             nc = c + dc
    #             if not (0 <= nr < NR and 0 <= nc < NC): continue

    #             if grid[nr][nc] == height:
    #                 visited.append((nr, nc))
    #                 print(visited)
                
    #             height += 1
            #     print(visited)
            #     if height == 9:
            #         return True
            #     self.dfs

        
    #    return False

    
    def read_input(self, file_path):
        grid = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    row = list(line.strip())
                    grid.append(list(map(int, row)))
            return grid
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

if __name__ == "__main__":
    solution = Solution()
    solution.day10()