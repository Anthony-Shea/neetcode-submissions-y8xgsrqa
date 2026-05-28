func getConcatenation(nums []int) []int {
    for _, v := range nums {
        nums = append(nums, v)
    }
    return nums
}
