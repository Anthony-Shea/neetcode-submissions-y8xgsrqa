import "slices"

func isAnagram(s string, t string) bool {
    if len(s) != len(t) { return false}
    ss := []rune(s)
    tt := []rune(t)
    slices.Sort(ss)
    slices.Sort(tt)
    return string(ss) == string(tt)
}
