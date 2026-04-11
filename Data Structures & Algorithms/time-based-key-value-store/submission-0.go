type TimeMap struct {
    Map  map[string][]Value 
}
type Value struct{
    time int
    value string
}

func Constructor() TimeMap {
  return TimeMap{
    Map: make(map[string][]Value),
  }
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
    if _, exists:= this.Map[key];!exists{
        this.Map[key] = make([]Value, 0 ,0)
    }
    this.Map[key]= append(this.Map[key], Value{
        time: timestamp,
        value: value,
    })
}

func (this *TimeMap) Get(key string, timestamp int) string {
    tmp, exists := this.Map[key]
    if !exists{
        return ""
    }
    l, r := 0, len(tmp)-1
    res := ""
    for (l<=r){
        m := (l+r)/2
        if timestamp == tmp[m].time{
            return tmp[m].value
        } 
        if timestamp< tmp[m].time{
            r= m-1
        }else{
            res = tmp[m].value

            l =m+1
        }
    }
    return res
}
