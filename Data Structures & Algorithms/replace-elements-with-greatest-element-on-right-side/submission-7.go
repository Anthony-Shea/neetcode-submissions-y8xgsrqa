func replaceElements(arr []int) []int {
    oldM := -1
    n := len(arr) - 1
    for i := n; i > -1; i-- {
        newM := max(oldM, arr[i])
        arr[i] = oldM
        oldM = newM
    }
    return arr
}
