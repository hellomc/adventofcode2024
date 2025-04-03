"""
Resources:
Day 5: Print Queue | Advent of Code 2024. William Y. Feng. https://www.youtube.com/watch?v=LA4RiCDPUlI
"""

from collections import defaultdict

class Solution:
    def day5(self):
        filename = "input.txt"
        pages, updates = self.read_input(filename)
        # print(pages, "\n", updates)
        outSum = self.getMidSum(pages, updates)
        print("Mid Sum: ", outSum)
        outNewSum = self.getNewMidSum(pages, updates)
        print("New Mid Sum: ", outNewSum)

    def getNewMidSum(self, pages, updates):
        sum = 0
        for update in updates:
            if self.isValid(pages, update)[0]: continue

            newupdate = self.makeValid(pages, update)
            sum += newupdate[len(newupdate) // 2]
        return sum

    def makeValid(self, pages, update):
        my_pages = []
        for x, y in pages:
            if not (x in update and y in update): continue
            my_pages.append((x,y))

        indegree = defaultdict(int)
        for x, y in my_pages:
            indegree[y] += 1
        
        valid = []
        while len(valid) < len(update):
            for page in update:
                if page in valid:
                    continue
                if indegree[page] <= 0:
                    valid.append(page)
                    for x, y in my_pages:
                        if x == page:
                            indegree[y] -= 1
        
        return valid
    
    def getMidSum(self, pages, updates):
        sum = 0
        for update in updates:
            valid, mid = self.isValid(pages, update)
            if valid:
                sum += mid
        return sum

    def isValid(self, pages, update):
        index = {}
        for i, num in enumerate(update):
            index[num] = i
        
        for x, y in pages:
            if x in index and y in index and not index[x] < index[y]:
                return False, 0
        
        return True, update[len(update) // 2]
    
    def read_input(self, file_path):
        """
        Reads in and splits page rules from updates. Converts string to int values.
        """
        pages = []
        updates = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    strip_line = line.strip()
                    if "|" in strip_line:
                        x, y = strip_line.split("|")
                        pages.append((int(x), int(y)))
                    if "," in strip_line:
                        updates.append(list(map(int, strip_line.split(","))))
            return pages, updates
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")

if __name__ == "__main__":
    solution = Solution()
    solution.day5()