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
        for (let i = 0; i < s.length; i++ ) {
            if (m.has(s[i])) {
                m.set(s[i], m.get(s[i])! + 1);
            } else {
                m.set(s[i], 1)
            }
        }
        for (let i = 0; i < t.length; i++) {
            if (m.has(t[i])) {
                m.set(t[i], m.get(t[i])! - 1);
            } else {
                return false
            }
            if (m.get(t[i]) < 0) {
                return false
            }
        }
        return true
    }
}
