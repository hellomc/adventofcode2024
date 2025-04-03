"""
Resources:
Advent of Code 2024 | Day 2 Jackie's Python Solution. CS Jackie. https://www.youtube.com/watch?v=sghAbg0WKt8
"""

import numpy as np

class Solution:

    def day2(self):
        filename = "input.txt"
        reports = self.readinput(filename)
        outReports = self.countSafe(reports)
        print("Number of Safe Reports: ", outReports)

        outDampened = self.countDampened(reports)
        print("Number of Dampened Safe Reports: ", outDampened)
    
    def acceptSingleBad(self, report):
        not_dampened = self.isSafe(report)
        if not_dampened == 0:
            for level in range(len(report)):
                if self.isSafe(np.delete(report, [level])):
                    return 1
            return 0
        return not_dampened

    def countDampened(self, reports):
        return np.sum(self.acceptSingleBad(report) for report in reports)
    
    def isSafe(self, report):
        if len(report) == 1:
            return 1
        
        diffs = np.diff(report) #gets differences between each level
        is_inc = np.all(diffs>=1) and np.all(diffs<=3)
        is_dec = np.all(diffs<=-1) and np.all(diffs>=-3)

        if is_inc or is_dec:
            return 1
        else:
            return 0
    
    def countSafe(self, reports):
        return np.sum(self.isSafe(report) for report in reports)

    def readinput(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            arrays = list()
            for line in lines:
                current = np.fromstring(line, dtype=int, sep=' ')
                arrays.append(current)        

        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError as e:
            print(f"Error processing the file: {e}")
        
        return np.array(arrays, dtype=object)


if __name__ == "__main__":
    solution = Solution()
    solution.day2()