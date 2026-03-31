class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for i, word in enumerate(strs):
            if "".join(sorted(word)) in m:
                m["".join(sorted(word))].append(i)
            else:
                m["".join(sorted(word))] = [i]
        res = []
        for w in m:
            r = []
            for num in m[w]:
                r.append(strs[num])
            res.append(r)
        return res