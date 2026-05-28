class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length != t.length) {
            return false
        }
        const cnt = {};
        for (const c of s) {
            cnt[c] = (cnt[c] || 0) + 1;
        }
        for (const c of t) {
            cnt[c]--
        }
        for (const c in cnt) {
            if (cnt[c] !== 0) return false;
        }
        return true
    }
}
