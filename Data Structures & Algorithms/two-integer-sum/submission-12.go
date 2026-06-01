func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
	for i , num := range nums {
		diff := target - num
		if j, ok := m[diff]; ok {
			return []int{j, i}
		}
		m[num] = i
	}
	return []int{}
}
