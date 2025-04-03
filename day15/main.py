"""
Resources
Advent of Code 2024 | Day 15 "Warehouse Woes". HyperNeutrino. https://www.youtube.com/watch?v=aCqtVmSSkUs
"""

class Solution:
    def day15(self):
        filename = "input.txt"
        grid, moves = self.read_input(filename)
        # posx, posy = self.find_start(grid)
        # print(posx, posy)
        # newgrid = self.move_robot(grid, moves, posx, posy)
        # outScore = sum(100*r + c for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == "O")
        # print(outScore)

        dblgrid = self.resize_grid(grid)
        # for row in dblgrid:
        #     print(row)
        posx2, posy2 = self.find_start(dblgrid)
        print(posx2, posy2)
        finalgrid = self.move_robot2(dblgrid, moves, posx2, posy2)
        # for row in finalgrid:
        #     print(row)
        outScore2 = sum(100 * r + c for r in range(len(finalgrid)) for c in range(len(finalgrid[0])) if finalgrid[r][c] == "[")
        print(outScore2)
    
    def move_robot2(self, grid, moves, r, c):
        for move in moves:
            dr = {"^": -1, "v": 1}.get(move, 0)
            dc = {"<": -1, ">": 1}.get(move, 0)
            targets = [(r,c)]
            go = True
            for cr, cc in targets:
                nr = cr + dr
                nc = cc + dc
                if (nr, nc) in targets: continue
                char = grid[nr][nc]
                if char == "#":
                    go = False
                    break
                if char == "[":
                    targets.append((nr, nc))
                    targets.append((nr, nc + 1))
                if char == "]":
                    targets.append((nr, nc))
                    targets.append((nr, nc - 1))
            if not go: continue

            copy = [list(row) for row in grid]
            grid[r][c] = "."
            grid[r + dr][c + dc] = "@"
            for br, bc in targets[1:]:
                grid[br][bc] = "."
            for br, bc in targets[1:]:
                grid[br + dr][bc + dc] = copy[br][bc]
            r += dr
            c += dc
        
        return grid

    def resize_grid(self, grid):
        NR = len(grid)
        NC = len(grid[0])
        change = {"#": "##", "O": "[]", ".": "..", "@": "@."}

        for r in range(NR):
            for c in range(NC):
                char = grid[r][c]
                grid[r][c] = change[char]

        dblgrid = []    
        for row in grid:
            line = list("".join(row))
            dblgrid.append(line)
        
        return dblgrid
    
    def move_robot(self, grid, moves, r, c):
        for move in moves:
            dr = {"^": -1, "v": 1}.get(move, 0)
            dc = {"<": -1, ">": 1}.get(move, 0)
            targets = [(r,c)]
            cr = r
            cc = c
            go = True
            while True:
                cr += dr
                cc += dc
                char = grid[cr][cc]
                if char == "#":
                    go = False
                    break
                if char == "O":
                    targets.append((cr, cc))
                if char == ".":
                    break
            if not go: continue
            grid[r][c] = "."
            grid[r+dr][c+dc] = "@"
            for br, bc in targets[1:]:
                grid[br+dr][bc+dc] = "O"
            r += dr
            c += dc
        
        return grid

    def find_start(self, grid):
        NR = len(grid)
        NC = len(grid[0])

        for r in range(NR):
            for c in range(NC):
                if grid[r][c] == "@":
                    return (r, c)
        
        return -1

    def read_input(self, file_path):
        try:
            with open(file_path, 'r') as file:
                part1, part2 = file.read().split("\n\n")

                grid = [list(line) for line in part1.splitlines()]
                moves = part2.replace("\n", "")

                # print(grid, '\n', moves)
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

        return grid, moves


if __name__ == "__main__":
    solution = Solution()
    solution.day15()