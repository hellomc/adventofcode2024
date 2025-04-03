from collections import deque

"""
Resources
Advent of Code 2024 | Day 12 "Garden Groups". HyperNeutrino. https://www.youtube.com/watch?v=KXwKGWSQvS0
"""

class Solution:
    def day12(self):
        filename = "input.txt"
        grid = self.read_input(filename)
        for row in grid:
            print(row)
        print(len(grid), len(grid[0]))
        regions = self.getregion(grid)
        # print(regions)
        # perimeters = [self.getperimeter(region) for region in regions]
        # print(perimeters)
        print(sum(len(region) * self.getperimeter(region) for region in regions))
        # sides = [self.getsides(region) for region in regions]
        # print(sides)
        print(sum(len(region) * self.getsides(region) for region in regions))

    def getsides(self, region):
        edges = {}
        for r, c in region:
             for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                 if (nr, nc) in region: continue
                 er = (r + nr) / 2
                 ec = (c + nc) / 2
                 edges[(er, ec)] = (er - r, ec - c)
        
        visited = set()
        side_count = 0
        for edge, direction in edges.items():
            if edge in visited: continue
            visited.add(edge)
            side_count += 1
            er, ec = edge
            if er % 1 == 0:
                for dr in [-1, 1]:
                    cr = er + dr
                    while edges.get((cr, ec)) == direction:
                        visited.add((cr, ec))
                        cr += dr
            else:
                for dc in [-1, 1]:
                    cc = ec + dc
                    while edges.get((er, cc)) == direction:
                        visited.add((er, cc))
                        cc += dc

        return side_count

   
    def getperimeter(self, region):
        output = 0

        for (r, c) in region:
            output += 4
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (nr, nc) in region:
                    output -= 1

        return output
    
    def getregion(self, grid):
        NR = len(grid)
        NC = len(grid[0])
        regions = []
        visited = set()

        for r in range(NR):
            for c in range(NC):
                if (r, c) in visited: continue
                visited.add((r, c))
                region = {(r, c)}
                q = deque([(r, c)])
                plant = grid[r][c]
                while q:
                    cr, cc = q.popleft()
                    for nr, nc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
                        if not (0 <= nr < NR and 0 <= nc < NC): continue
                        if grid[nr][nc] != plant: continue
                        if (nr, nc) in region: continue
                        region.add((nr, nc))
                        visited.add((nr, nc))
                        q.append((nr, nc))
                regions.append(region)
        return regions

    def read_input(self, file_path):
        grid = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    row = line.strip()
                    grid.append(row)
            return grid
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

if __name__ == "__main__":
    solution = Solution()
    solution.day12()