class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        res = 0
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(c)):
                    xor = a[i] ^ b[j] ^ c[k]
                    if xor.bit_count() % 2 == 0:
                        res += 1
        return res