func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
	for i , num := range nums {
		diff := target - num
		if _, ok := m[diff]; ok {
			return []int{m[diff], i}
		}
		m[num] = i
	}
	return []int{}
}
