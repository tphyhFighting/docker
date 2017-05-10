#### etcdv3cli 使用https访问

#### 1.代码
```bash
func initETCdClient(machines []string, CA, cert, key string, timeout time.Duration) (*etcd.Client, error) {
	var tlsConfig *tls.Config
	if cert != "" && key != "" && CA != "" {
		cert, err := tls.LoadX509KeyPair(cert, key)
		if err != nil {
			log.Fatal("failed to load client key pair:", err)
		}
		caCert, err := ioutil.ReadFile(CA)
		if err != nil {
			log.Fatal("failed to load CA:", err)
		}
		caCertPool := x509.NewCertPool()
		caCertPool.AppendCertsFromPEM(caCert)
		tlsConfig = &tls.Config{
			Certificates: []tls.Certificate{cert},
			RootCAs:      caCertPool,
		}
		tlsConfig.BuildNameToCertificate()
	}

	cfg := etcd.Config{
		Endpoints:   machines,
		TLS:         tlsConfig,
		DialTimeout: timeout,
	}

	c, err := etcd.New(cfg)
	if err != nil {
		return nil, err
	}
	return c, err
}
```
KeepAlive
```bash
func setKVKeepAlive(endpoint []string, key, value string, ttl int64)  (err error){
	cli, err := clientv3.New(clientv3.Config{
		Endpoints: endpoint,
	})
	if err != nil {
		return err
	}
	defer cli.Close()

	// minimum lease TTL is 30-second
	resp, err := cli.Grant(context.TODO(), ttl)
	if err != nil {
		return err
	}

	logger.Debugf("resp:%v", resp)
	_, err = cli.Put(context.TODO(), key, value, clientv3.WithLease(resp.ID))
	if err != nil {
		return err
	}

	// the key 'foo' will be kept forever
	ch := cli.KeepAlive(context.TODO(), resp.ID)
	//if kaerr != nil {
	//	log.Fatal(kaerr)
	//}
	cnt := 1
	for {
		ka := <-ch
		fmt.Println(time.Now(),"ttl:", ka.TTL)
		cnt = cnt + 1
		if cnt > 5{
			break
		}
	}


	return err
}
```
getkey by prefix
