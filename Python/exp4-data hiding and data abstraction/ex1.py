class Solution:
    def __init__(self):
        self.privatecounter = 0
    
    def sum(self):
        self.privatecounter += 1
        print(self.privatecounter)

count = Solution()
count.sum()
count.sum()
count.sum()
