### 视频时长处理
```go
func ParseDuration(d string)  (total int, err error){
	total = 0
	ret := durationregx.FindStringSubmatch(d)
	for _, tt := range ret[1:] {
		if tt == ""{
			continue
		}
		tmp, err := ToSeconds(tt)
		if err != nil {
			return total, err
		}
		total += tmp
	}

	return total, nil
}

//d must endwith s/m/h/d
func ToSeconds(d string)  (t int, err error){
	if d == "" || len(d) < 2{
		err = fmt.Errorf("input err d:%v", d)
		return 0, err
	}
	length := len(d) - 1
	logger.Debugf("parse:%v", d[:length])
	tmp, err := strconv.Atoi(d[:length])
	if err != nil {
		err = fmt.Errorf("err:%v d:%v pare:%v", err, d, d[:length])
		return tmp, err
	}
	lastChar := d[length]
	logger.Debugf("last:%v", lastChar)
	//if strings.HasSuffix(d,"S") {
	//	t = tmp*1
	//}else if strings.HasSuffix(d, "M") {
	//	t = tmp*60
	//}else if strings.HasSuffix(d, "H") {
	//	t = tmp*60*60
	//}else if strings.HasSuffix(d, "D") {
	//	t = tmp*24*60*60
	//}
	switch string(lastChar) {
	case "S":
		t = tmp*1
	case "M":
		t = tmp*60
	case "H":
		t = tmp*60*60
	case "D":
		t = tmp*24*60*60
	}
	return t, err
}
```

#### test case
```go
//P#DT#H#M#S.
//PT#H#M#S
//PT15M33S
//PT#M#S
func TestParseDuration(t *testing.T)  {
	type parseResult struct {
		dd	int
		hh 	int
		mm 	int
		ss  int
	}

	tds := []struct {
		D string
		result parseResult
	}{
		{
			D:"P1DT12H31M44S",
			result:parseResult{
				dd:1,
				hh:12,
				mm:31,
				ss:44,
			},
		},
		{
			//PhMmHTFj7tc
			D:"PT2H42M22S",
			result:parseResult{
				dd:0,
				hh:2,
				mm:42,
				ss:42,
			},
		},
		{
			D:"PT31M44S",
			result:parseResult{
				dd:0,
				hh:0,
				mm:31,
				ss:44,
			},
		},
		{
			D:"PT44S",
			result:parseResult{
				dd:0,
				hh:0,
				mm:0,
				ss:44,
			},
		},
	}

	re := regexp.MustCompile("P(|\\d+D)T(|\\d+H)(|\\d+M)(\\d+S)$")
	for index, td := range tds {
		ret := re.FindStringSubmatch(td.D)
		t.Logf("index:%v ret:%v ret[1:]:%v", index,  ret, ret[1:])
		total := 0
		for _, tt := range ret[1:] {
			//t.Logf("tt:%v", tt)
			if tt == ""{
				continue
			}
			tmp, err := ToSeconds(tt)
			if err != nil {
				t.Fatal(err)
			}
			t.Logf("tt:%v tmpS:%v", tt, tmp)
			total += tmp
		}
		t.Logf("total:%v", total)
	}
}

func TestToSeconds(t *testing.T)  {
	ret, err := ToSeconds("44M")
	if err != nil {
		t.Fatal(err)
	}
	t.Logf("ret:%v", ret)
}
```
