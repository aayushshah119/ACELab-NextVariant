""" 
Requirements for proof of concept:
1. Track when is first call, and retrieve total_variants from helper
2. Generate iterator to randomly iterate through variant numbers 
3. Be able to accomodate when variant number is specified (select variant i example)
"""
import random 

class MiddleWare:
    def __init__(self):
        self.selected = set()
        self.totalNum = helperAbstract()
        self.iter = (a for a in random.sample(range(self.totalNum), self.totalNum)) 
        return
    
    def getVNum(self, variantNum = -1):
        
        if variantNum != -1:
            variantNumAdjust = variantNum % self.totalNum
            self.selected.add(variantNumAdjust)
            return variantNumAdjust
        
        ret = self.nextVNum()

        while ret in self.selected:
            ret = self.nextVNum()
        
        return ret

    def nextVNum(self):
        try:
            ret = next(self.iter)
        except StopIteration:
            print("Finished all iterations, will be repeating now.")
            self.selected.clear()
            self.iter = (a for a in random.sample(range(self.totalNum), self.totalNum))
            ret = next(self.iter)
        return ret


def helperAbstract():
    return random.randint(5,10)

prototype = MiddleWare()

for i in range(20):
    print(prototype.getVNum())

for i in range(20):
    print(prototype.getVNum(i + 1))