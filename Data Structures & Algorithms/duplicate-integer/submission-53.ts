class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const s = new Set<number>()
        for (let n of nums) {
            if (s.has(n)) {
                return true
            }
            else {
                s.add(n)
            }
        }
        return false
    }
}
