func addBinary(a string, b string) string {
	res := []byte{}
    carry := 0
    i, j := len(a) - 1, len(b) - 1
    for i >= 0 || j >= 0 || carry > 0 {
        digitA := 0
        digitB := 0
        if i >= 0 {
            digitA = int(a[i] - '0')
        }
        if j >= 0 {
            digitB = int(b[j] - '0')
        }
        total := digitA + digitB + carry
        res = append(res, byte(total%2)+'0')
        carry = total / 2
        i--
        j--
    }
    for l, r := 0, len(res) - 1; l < r; l, r = l + 1, r-1 {
        res[l], res[r] = res[r], res[l]
    }
    return string(res)
}
