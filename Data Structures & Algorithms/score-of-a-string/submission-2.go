func scoreOfString(s string) int {
    r := 0
    for i := 0; i < len(s) - 1; i++ {
        r += int(math.Abs(float64(s[i]) - float64(s[i+1])))
    }
    return r
}
