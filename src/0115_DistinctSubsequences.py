'''


    r  a  b  b  b  i  t
    
r   1  1  1  1  1  1  1
a   0  1  1  1  1  1  1
b   0  0  1  2  3  3  3
b   0  0  0  1  3  3  3
i   0  0  0  0  0  3  3
t   0  0  0  0  0  0  3


'''

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_s, len_t = len(s), len(t)
        ret_arr = []
        for i in range(len_t):
            arr = []
            for j in range(len_s):
                if i > j:
                    arr.append(0)
                else:
                    if s[j] == t[i]:
                        if i == 0:
                            arr.append(1 if j == 0 else 1 + arr[-1])
                        else:
                            arr.append(ret_arr[i - 1][j - 1] + arr[j - 1])
                    else:
                        arr.append(arr[j - 1] if j - 1 >= 0 else 0)
            ret_arr.append(arr)
        return ret_arr[-1][-1] if ret_arr and ret_arr[0] else 0

        
if __name__ == "__main__":
    solution = Solution()
    print solution.numDistinct('rabbbit', 'rabbit')