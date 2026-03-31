class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] != words[j] and words[i] in words[j]:
                    result.append(words[i])
                    result = set(result)
                    result = list(result)
        return result