func replaceElements(arr []int) []int {
    m := -1
    for i := len(arr) - 1; i > -1; i-- {
        newM := max(m, arr[i])
        arr[i] = m
        m = newM
    }
    return arr
}
