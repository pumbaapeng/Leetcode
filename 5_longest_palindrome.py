class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        for i,c in enumerate(s) :
            # odd
            l_nxt = 1
            while True :
                if i - l_nxt < 0 or i + l_nxt >= len(s) or s[i - l_nxt] != s[i + l_nxt] :
                    break
                l_nxt += 1
            cur_len = 2 * (l_nxt - 1) + 1
            max_len = max(max_len, cur_len)
            # even
            l_nxt = 1
            while True :
                if i - l_nxt + 1 < 0 or i + l_nxt >= len(s) or s[i - l_nxt + 1] != s[i + l_nxt] :
                    break
                l_nxt += 1
            max_len = max(max_len, 2 * (l_nxt - 1))
        return(max_len)
    
if __name__ == "__main__":
    s = 'adccbccdd'
    print Solution().longestPalindrome(s)
    assert Solution().longestPalindrome(s) == 7
    s = 'ccc'
    assert Solution().longestPalindrome(s) == 3
    s = 'bb'
    assert Solution().longestPalindrome(s) == 2
    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    assert Solution().longestPalindrome(s) == 983
