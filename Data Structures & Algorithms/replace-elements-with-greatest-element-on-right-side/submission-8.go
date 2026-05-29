func replaceElements(arr []int) []int {
    oldM := -1
    for i := len(arr)-1; i >= 0; i-- {
        newM := max(oldM, arr[i])
        arr[i] = oldM
        oldM = newM
    }
    return arr
}
