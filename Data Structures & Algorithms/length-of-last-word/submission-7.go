func lengthOfLastWord(s string) int {
	i, r := len(s) - 1, 0
    for s[i] == ' ' {
        i--
    }
    for i >= 0 && s[i] != ' ' {
        i--
        r++
    }
    return r
}
