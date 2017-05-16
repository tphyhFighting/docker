#### cli 测试

#### post
```bash
curl -H "Content-Type: application/json" http://localhost:1500/crawler -d '{"type": "search","par": {"key":"liebao"}}' | python -mjson.tool

curl -H "Content-Type: application/json" http://localhost:1500/crawler -d '{"type": "apk","par": {"key":"liebao"}}' | python -mjson.tool
```
