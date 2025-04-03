"""RESOURCES
Advent of Code 2024 | Day 14 "Restroom Redoubt". HyperNeutrino. https://www.youtube.com/watch?v=ySUUTxVv31U"""

import matplotlib.pyplot as plt

class Solution:
    def day14(self):
        filename = "input.txt"
        pos, vel = self.read_input(filename)
        # print(pos, "\n", vel)

        WIDTH = 101   #101 11  num columns
        HEIGHT = 103  #103  7  num rows

        movement = self.getRobots(pos, vel, rows=HEIGHT, columns=WIDTH)
        # print(movement)
        
        grid = [[0] * WIDTH for _ in range(HEIGHT)]
        for px, py in movement:
            grid[py][px] += 1
        for row in grid:
            print(*row, sep="")

        score = self.getQuads(movement, height=HEIGHT, width=WIDTH)
        print("Safety Score:", score)

        self.part2(pos, vel, height=HEIGHT, width=WIDTH)
        # print(iteration)


    def part2(self, positions, velocities, height=7, width=11):
        t = []
        ss = []

        for second in range(10000):
            result = []
            
            for px, py in positions:
                for vx, vy in velocities:
                    result.append(((px + vx * second) % width, (py + vy * second) % height))
            
            t.append(second)
            ss.append(self.getQuads(result, height=height, width=width))
            
        plt.plot(t, ss)
        plt.show()

    
    def getQuads(self, lastpositions, height=7, width=11):
        HMedian = (height - 1) // 2
        WMedian = (width - 1) // 2
        quad = [0] * 4

        for px, py in lastpositions:
            if px == WMedian or py == HMedian: continue
            if px < WMedian:
                if py < HMedian:
                    quad[0] += 1
                else:
                    quad[1] += 1
            else:
                if py < HMedian:
                    quad[2] += 1
                else:
                    quad[3] += 1
        
        return quad[0] * quad[1] * quad[2] * quad[3]

    def getRobots(self, positions, velocities, time=100, rows=7, columns=11):
        NR = rows
        NC = columns
        lastpos = []
        
        for i in range(len(positions)):
            for _ in range(time):
                cx, cy = positions[i]
                # print(cx, cy)
                dx, dy = velocities[i][0], velocities[i][1]
                # print(dx, dy)
                nx = (cx + dx) % NC
                ny = (cy + dy) % NR
                positions[i] = [nx, ny]
            # print(nx, ny)
            lastpos.append((nx, ny))
        
        return lastpos
    
    def read_input(self, file_path):
        pos_list = []
        vel_list = []

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    data = line.strip()
                    parts = data.split()
                    if len(parts) == 2:
                        p = parts[0].lstrip("p=")
                        v = parts[1].lstrip("v=")
                        p_val = list(map(int, p.split(",")))
                        v_val = list(map(int, v.split(",")))
                        pos_list.append(p_val)
                        vel_list.append(v_val)

        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

        return pos_list, vel_list
    
if __name__ == "__main__":
    solution = Solution()
    solution.day14()