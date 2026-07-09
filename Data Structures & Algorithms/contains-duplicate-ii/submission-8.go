func containsNearbyDuplicate(nums []int, k int) bool {
    L := 0
    window := make(map[int]bool)
    for R := 0; R < len(nums); R++ {
        if R-L > k {
            delete(window,nums[L])
            L++
        }
        if window[nums[R]] {
            return true
        }
        window[nums[R]] = true
    }
    return false
}
