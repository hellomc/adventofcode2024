"""
Resources:
Disk Fragmenter [Day 9 - Advent of Code 2024 - Python]. 0xdf. https://www.youtube.com/watch?v=5k8O1EloI5M
"""

class Solution:
    def day9(self):
        filename = "example.txt"
        densedisk = self.read_input(filename)
        print(densedisk)
        infodisk = self.unpackDisk(densedisk)
        print(infodisk)

        compactdisk = self.compactDisk(infodisk[:])
        print(compactdisk)
        outChecksum = self.calcChecksum(compactdisk)
        print("checksum: ", outChecksum)

        compactdisk2 = self.compactDisk2(densedisk)
        print(compactdisk2)
        outChecksum2 = self.calcChecksum2(compactdisk2)
        print("checksum2: ", outChecksum2)

    def calcChecksum2(self, files):
        checksum = 0
        for filenum, (loc, size) in files.items():
            for i in range(loc, loc + size):
                checksum += (i * filenum)
        
        return checksum

    def compactDisk2(self, disk):
        disk = list(map(int, disk))
        isfile = True
        files = {}
        spaces = []
        ptr = 0
        print(disk)

        for i, size in enumerate(disk):
            if isfile:
                files[i//2] = (ptr, size)
            else:
                spaces.append((ptr, size))
            isfile = not isfile
            ptr += size
        
        for filenum in dict(reversed(list(files.items()))):
            loc, file_size = files[filenum]
            space_id = 0
            while space_id < len(spaces):
                space_loc, space_size = spaces[space_id]
                if space_loc > loc:
                    break
                if space_size == file_size:
                    files[filenum] = (space_loc, file_size)
                    spaces.pop(space_id)
                    break
                if space_size > file_size:
                    files[filenum] = (space_loc, file_size)
                    spaces[space_id] = (space_loc + file_size, space_size - file_size)
                    break
                space_id += 1
        
        return files

    
    def calcChecksum(self, disk):
        checksum = sum(i*val for i, val in enumerate(disk))
        
        return checksum

    def compactDisk(self, disk):
        disk_length = len(disk)
        mydisk = disk

        free_space = [i for i, val in enumerate(mydisk) if val == -1]
        i = 0
        while True:
            while mydisk[-1] == -1: mydisk.pop()
            target = free_space[i]
            if target >= len(mydisk):
                break
            mydisk[target] = mydisk.pop()
            i += 1
        
        return mydisk
        

    def unpackDisk(self, disk):
        disk = list(map(int, disk))
        id_count = 0
        disk_length = len(disk)
        disk_map = []

        for i in range(disk_length):
            if i % 2 == 0:
                count = disk[i]
                for i in range(count):
                    disk_map.append(id_count)
                id_count += 1
            elif i % 2 == 1:
                count = disk[i]
                for i in range(count):
                    disk_map.append(-1)

        return disk_map
    
    def read_input(self, file_path):
        try:
            with open(file_path, "r") as file:
                data = "".join(line.strip() for line in file)
            return data
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

if __name__ == "__main__":
    solution = Solution()
    solution.day9()