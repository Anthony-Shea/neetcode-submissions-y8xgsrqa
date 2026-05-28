func getConcatenation(nums []int) []int {
    n := len(nums)
    res := make([]int, 0, 2*n)
    for i := 0; i < 2*n; i++ {
        res = append(res, nums[i%n])
    }
    return res
}
