func isAnagram(s string, t string) bool {
    if len(s) != len(t) { return false }
    cnts := make([]int, 26)
    for _, c := range s {
        cnts[c-'a']++
    }
    for _, c := range t {
        cnts[c-'a']--
    }
    for _, c := range cnts {
        if c != 0 {
            return false
        }
    }
    return true
}
