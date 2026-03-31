class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mST, mTS = {}, {}
        for c1, c2 in zip(s,t):
            if ((c1 in mST and mST[c1] != c2) or
                (c2 in mTS and mTS[c2] != c1)):
                return False
            mST[c1] = c2
            mTS[c2] = c1
        return True