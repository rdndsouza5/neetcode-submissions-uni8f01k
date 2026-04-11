func hasDuplicate(nums []int) bool {
    a := make(map[int]struct{})
    for _,i := range nums{
        if _,ok:= a[i];ok{
            return ok
        }
        a[i]=struct{}{}
    }
    return false
}
