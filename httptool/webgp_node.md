#### webgp_node 端测试指南
```bash
curl -H "Content-Type: application/json" http://localhost:1500/crawler -d '{"type": "apk","par": {"package_name": "com.gameloft.android.ANMP.GloftOLHM"}}' | python -mjson.tool

curl -H "Content-Type: application/json" http://localhost:1500/crawler -d '{"type": "search","par": {}}' | python -mjson.tool
```
