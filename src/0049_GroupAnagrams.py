class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret_arr = []
        hash_obj = {}
        for str_each in strs:
            str_sorted = ''.join(sorted(str_each))
            if str_sorted in hash_obj:
                index = hash_obj[str_sorted]
                str_arr_temp = ret_arr[index]

                inserted = False
                for i in range(len(str_arr_temp)):
                    str_temp = str_arr_temp[i]
                    if str_each < str_temp:
                        str_arr_temp.insert(i, str_each)
                        inserted = True
                        break

                if not inserted:
                    str_arr_temp.append(str_each)
            else:
                ret_arr.append([str_each])
                hash_obj[str_sorted] = len(ret_arr) - 1

        return ret_arr

if __name__ == "__main__":
    solution = Solution()
    print solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])