class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        my_dict = {}
        for s in strs:
            myKey = "".join(sorted(s))
            if myKey in my_dict:
                my_dict[myKey].append(s)
            else:
                my_dict[myKey] = [s]
        out = [v for k,v in my_dict.items()]
        return out

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print Solution().groupAnagrams(strs)
