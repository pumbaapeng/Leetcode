# corner case: last occurance of the new character is before the current right
# key: contain is the index of characters 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
	left = 0
	contain = {}
	max_run = 0
	for right, c in enumerate(s):
		if c in contain :
			new_left = contain[c] + 1
			while left < new_left :
				del contain[s[left]]
				left += 1
                contain[c] = right
		cur_run = right - left + 1
                print cur_run
        	max_run = max(max_run, cur_run)
        return max_run
		
if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring('abcabcbb') == 3
    assert Solution().lengthOfLongestSubstring('bbbbb') == 1
    assert Solution().lengthOfLongestSubstring('pwwkew') == 3
