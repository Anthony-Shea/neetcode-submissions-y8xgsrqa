func hasDuplicate(nums []int) bool {
    s := map[int]struct{}{}
    for _, num := range nums {
        s[num] = struct{}{}
    }
    return len(s) < len(nums)
}
