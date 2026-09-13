class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const m = new Set()
        for (const n of nums) {
            if (m.has(n)) {
                return true
            }
            m.add(n)
        }
        return false
    }
}
