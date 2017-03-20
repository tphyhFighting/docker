##imgfit 

## gif 处理
```concept
func DecodeAll(r io.Reader) (*GIF, error) {
	var d decoder
	if err := d.decode(r, false); err != nil {
		return nil, err
	}
	gif := &GIF{
		Image:     d.image,
		LoopCount: d.loopCount,
		Delay:     d.delay,
		Disposal:  d.disposal,
		Config: image.Config{
			ColorModel: d.globalColorTable,
			Width:      d.width,
			Height:     d.height,
		},
		BackgroundIndex: d.backgroundIndex,
	}
	return gif, nil
}
```

1.缩放后w/h保持原有的大小
gif.Config.Width = 