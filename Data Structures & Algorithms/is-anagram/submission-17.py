class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list1 = []
        list2 = []
        for char in s:
            list1.append(char)
        for char in t:
            list2.append(char)
        if sorted(list1) != sorted(list2):
            return False
        return True