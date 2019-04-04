class Solution:
    def reverseWords(self, s: str) -> str:
        my_list = s.split(" ")
        tmp = []
        for item in my_list:
            if item != "":
                tmp.append(item)
        return " ".join(tmp[::-1])
