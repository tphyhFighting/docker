func delDir(path string, this *S3Storage)  (err error){
	if !IsDir(path) {
		return errors.New("is not dir")
	}

	b := this.svc.Bucket(this.conf.Bucket)
	defer func() {
		logger.Debugf("fake rm dir:%v ..b:%v", path, b)
		//err = b.Del(path)
	}()
	keys, err := this.LsDir(path)
	if err != nil {
		return err
	}

	for _, key := range keys{
		if !IsDir(key) {
			logger.Errorf("fake rm :%v", key)
			//err = b.Del(key)
		}else{
			if key != path {
				logger.Debugf("dir:%v", key)
				err = delDir(key, this)
			}
		}
	}

	return err
}
