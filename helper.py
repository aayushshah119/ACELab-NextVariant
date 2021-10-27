
from functools import reduce

class Helper:
    def __init__(self, ranges):
        new_ranges = []
        for item in ranges:
            new_ranges.append(item[1] - item[0])
        self.ranges = new_ranges

    def generate_values(self, variant):
        result = []
        for i in range(len(self.ranges) - 1):
            ranges_product = reduce((lambda x, y: x * y), self.ranges[i+1:])
            if variant - ranges_product < 0:
                result.append(0)
            else:
                for j in range(1, self.ranges[i] + 1):
                    if variant %(ranges_product*self.ranges[i]) < j*ranges_product:
                        result.append(j - 1)
                        break

        result.append(variant % self.ranges[-1])
        return result


"""
check = Helper([5,4,3])
for i in range(60):
    print(i, check.generate_values(i))
"""
"""
    #A's value
    if variant - b_range*c_range < 0:
        result.append(0)
    else:
        for i in range(1, a_range + 1):
            if variant < i*b_range*c_range:
                result.append(i-1)
                break
    
    #B's value
    if variant - c_range < 0:
        result.append(0)
    else:
        for i in range(1, b_range+1):
            if variant % (c_range*b_range) < i * c_range:
                result.append(i-1)
                break

    #C's value
    result.append(variant % c_range)
    return result
"""