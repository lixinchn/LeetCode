class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        map_number = {}
        n = str(n)
        while True:
            map_number[n] = True
            new_n = self.get_number(n)
            if int(new_n) == 1:
                return True
            if new_n in map_number:
                return False
            n = new_n

    def get_number(self, n):
        total = 0
        for i in range(len(n)):
            int_i = int(n[i])
            total += int_i * int_i
        return str(total)
        
if __name__ == "__main__":
    solution = Solution()
    print solution.isHappy(19)
    print solution.isHappy(18)
    print solution.isHappy(17)
    print solution.isHappy(16)