func getConcatenation(nums []int) []int {
    ans := make([]int, 2* len(nums))
    for i, n := range(nums){
        ans[i]= n
        ans[i+len(nums)] = n
    }
    return ans
}
