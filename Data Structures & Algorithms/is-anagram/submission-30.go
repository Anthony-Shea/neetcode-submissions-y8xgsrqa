func isAnagram(s string, t string) bool {
    m := make(map[rune]int)
    if len(s) != len(t) {
        return false
    } 
    for _, v := range s {
        m[v]++
    }
    for _, v := range t {
        m[v]--
        if m[v] < 0 {
            return false
        }
    }
    return true
}
