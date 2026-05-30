func isAnagram(s string, t string) bool {
    if len(s) != len(t) { return false}
    ss := []rune(s)
    tt := []rune(t)
    sort.Slice(ss, func (i, j int) bool { return ss[i] < ss[j]})
    sort.Slice(tt, func (i, j int) bool { return tt[i] < tt[j]})
    return string(ss) == string(tt)
}
