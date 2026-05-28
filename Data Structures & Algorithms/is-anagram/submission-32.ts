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
        const m = new Map<string, number>();
        for (const c of s) {
            if (m.has(c)) {
                m.set(c, m.get(c)! + 1);
            } else {
                m.set(c, 1)
            }
        }
        for (const c of t) {
            if (m.has(c)) {
                m.set(c, m.get(c)! - 1);
            } else {
                return false
            }
            if (m.get(c) < 0) {
                return false
            }
        }
        return true
    }
}
