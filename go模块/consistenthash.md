## consistenthash

## 源码
	结果分析
	1.Map
		1.hash 函数对象
		2.repicas 
		3.keys 排序后的键，从小到大
		4.hashMap map[int]string  //add 中实现值的存储

	2.New()
		1.分配Map.
			绑定fn->hash. 调用者绑定hash函数
			初始化
			replicas: 3,


	1.Add(keys ...string)
		1.keys: "2" "4" "6"
		for _, key := range keys {//'2', '4', '6'
			for i := 0; i < m.replicas; i++ {//0, 1, 2
				hash := int(m.hash([]byte(strconv.Itoa(i) + key))) //'2' '12' '22'; '4' '14' '24'; '6' '16' '26'
				m.keys = append(m.keys, hash).                     //[2  12  22    4  14  24   6  16  26] ==> sort [2 4 6 12 14 16 22 24 26]
				m.hashMap[hash] = key 							   //'2' '2' '2'  '4' '4' '4' '6' '6' '6'
			}
		}

	2.Get()
		//1.由add -> m.hashMap[hash] = key, 数据是通过key->hash(key) 放在了m.hashMap中

		1.hash := int(m.hash([]byte(key))) //个人认为，完全可以从此处直接获取v, v = m.hashMap[hash];
		//hash := int(m.hash([]byte(strconv.Itoa(0)+key))) //个人认为，完全可以从此处直接获取v, v = m.hashMap[hash]; 但是对于Get('11') 则不成立
		//hash := int(m.hash([]byte(strconv.Itoa(1)+key))) //hash 虽然不同，但值相同
		//hash := int(m.hash([]byte(strconv.Itoa(2)+key))) //

		2.idx: 找到第一个不满足m.keys[i] >= hash 的值
			idx := sort.Search(len(m.keys), func(i int) bool {
				fmt.Printf("i:%v m.keys:%v", i, m.keys[i])
				return m.keys[i] >= hash
			})
			1.   mkeys     [2 4 6 12 14 16 22 24 26]
				 hashMap.  [2 4 6 ...      ...     ] //是否可以再次使用字典，减小缓存?

			2.Get('11') --> 2
				1.'11' -> hash('11') = > 11
				2.idx = sort.Search(9, func(i int) ) => 
								i.     m.keys   fn
							1.	4      14 > 11  true   j=h;  //4
							2.  2      6  < 11  false  i=h+1 //3, i<j
							3.  3      12 > 11  true.  j=3.  //i<j 不成立，退出 
					idx = 3

			hash('11') -> 找到就是大于等于11最近的值

		3.return m.hashMap[m.keys[idx]] //m.hashMap[12] = 2 

```
type Hash func(data []byte) uint32

type Map struct {
	hash     Hash
	replicas int
	keys     []int // Sorted
	hashMap  map[int]string
}

func New(replicas int, fn Hash) *Map {
	m := &Map{
		replicas: replicas,
		hash:     fn,
		hashMap:  make(map[int]string),
	}
	if m.hash == nil {
		m.hash = crc32.ChecksumIEEE
	}
	return m
}

// Returns true if there are no items available.
func (m *Map) IsEmpty() bool {
	return len(m.keys) == 0
}

// Adds some keys to the hash.
func (m *Map) Add(keys ...string) {
	for _, key := range keys {
		for i := 0; i < m.replicas; i++ {
			hash := int(m.hash([]byte(strconv.Itoa(i) + key)))
			m.keys = append(m.keys, hash)
			m.hashMap[hash] = key
		}
	}
	sort.Ints(m.keys)
}

// Gets the closest item in the hash to the provided key.
func (m *Map) Get(key string) string {
	if m.IsEmpty() {
		return ""
	}

	hash := int(m.hash([]byte(key)))
	fmt.Printf("hash:%v..m.hashMap:%v\n", hash, m.hashMap[hash])

	// Binary search for appropriate replica.
	idx := sort.Search(len(m.keys), func(i int) bool {
		fmt.Printf("i:%v m.keys:%v", i, m.keys[i])
		return m.keys[i] >= hash
	})
	fmt.Printf("idx:%v\n", idx)

	// Means we have cycled back to the first replica.
	if idx == len(m.keys) {
		idx = 0
	}

	return m.hashMap[m.keys[idx]]
}
```