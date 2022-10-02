# https://cybergeeksquad.co/2021/06/fill-the-truck-maximum-units-on-a-truck.html
# Solved on leetcode

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1])

        res = 0
        while boxTypes and truckSize > 0:
            count, unit_size = boxTypes.pop()
            if truckSize - count > 0:
                res += count * unit_size
                truckSize -= count
            else:
                res += truckSize * unit_size
                truckSize = 0

        return res
