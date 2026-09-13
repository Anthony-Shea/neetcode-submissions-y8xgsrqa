class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const m = new Map()
        for (const n of nums) {
            if (n in m) {
                return true
            }
            m[n] = true
        }
        return false
    }
}
