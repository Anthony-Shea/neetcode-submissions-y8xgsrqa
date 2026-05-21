func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    m1 := make(map[rune]int)
    for _, v := range s {
        m1[v]++
    }
    m2 := make(map[rune]int)
    for _, v := range t {
        m2[v]++
    }
    for _, v := range s {
        if m1[v] != m2[v] {
            return false
        }
    }
    return true
}
