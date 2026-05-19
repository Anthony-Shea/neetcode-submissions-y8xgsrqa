class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums: number[]): number[] {
        let ans = [];
        let n = nums.length
        for (let i = 0; i < n; i++) {
            ans[i] = ans[i+n] = nums[i]
        }
        return ans
    }
}
