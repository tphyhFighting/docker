##elk

#1.0 资料
	https://kibana.logstash.es/content/logstash/get-start/install.html
	https://www.elastic.co/guide/en/logstash/current/configuration.html
	https://github.com/hyhlinux/ELKstack-guide-cn/blob/master/README.md
	安装教程
	https://segmentfault.com/a/1190000006188536

#1. elasticsearch
    端口:127.0.0.1:9200
    1.brew install elasticsearch
    2.elasticsearch --version
    3.brew services start elasticsearch
    4.brew services stop elasticsearch
    5.使用docker 安装
    https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
```concept
➜  ~ docker pull docker.elastic.co/elasticsearch/elasticsearch:5.2.2
5.2.2: Pulling from elasticsearch/elasticsearch
3690ec4760f9: Pull complete 
f52154c3d3fc: Pull complete 
4075cc5db14a: Pull complete 
5d31442d4bee: Pull complete 
f79275a9b20e: Pull complete 
7936cfd6c41c: Pull complete 
3ecc13d7ef73: Pull complete 
92ec059627ea: Pull complete 
738e956f3f5b: Pull complete 
099051b6b436: Pull complete 
Digest: sha256:2906a194f969d1704bc9f00580141dc72b8f79567933a1b59faf568401e057cc
Status: Downloaded newer image for docker.elastic.co/elasticsearch/elasticsearch:5.2.2
➜  ~ 

```
    
#2. logstash
    端口:http://localhost:9600/
    1.brew install logstash
    2.logstash --version
```concept
➜  tools logstash -e 'input{stdin{}}output{stdout{codec=>rubydebug}}'
Sending Logstash's logs to /usr/local/Cellar/logstash/5.2.2/libexec/logs which is now configured via log4j2.properties
[2017-03-15T22:00:39,042][INFO ][logstash.setting.writabledirectory] Creating directory {:setting=>"path.queue", :path=>"/usr/local/Cellar/logstash/5.2.2/libexec/data/queue"}
[2017-03-15T22:00:39,060][INFO ][logstash.agent           ] No persistent UUID file found. Generating new UUID {:uuid=>"d0c5e0ca-1ba7-49a5-ac2a-bb7fabcc56c6", :path=>"/usr/local/Cellar/logstash/5.2.2/libexec/data/uuid"}
[2017-03-15T22:00:39,313][INFO ][logstash.pipeline        ] Starting pipeline {"id"=>"main", "pipeline.workers"=>4, "pipeline.batch.size"=>125, "pipeline.batch.delay"=>5, "pipeline.max_inflight"=>500}
[2017-03-15T22:00:44,338][INFO ][logstash.pipeline        ] Pipeline main started
The stdin plugin is now waiting for input:
[2017-03-15T22:00:44,408][INFO ][logstash.agent           ] Successfully started Logstash API endpoint {:port=>9600}

{
    "@timestamp" => 2017-03-15T14:01:42.712Z,
      "@version" => "1",
          "host" => "hyhMac.local",
       "message" => ""
}
helloworld
{
    "@timestamp" => 2017-03-15T14:01:49.070Z,
      "@version" => "1",
          "host" => "hyhMac.local",
       "message" => "helloworld"
}
```
#3. 安装kibana
    1.tar -xvf kibana-5.2.2-darwin-x86_64.tar.gz
    2../kibana #会自动连接9200
```concept
➜  bin pwd
/Users/apple/opt/kibana-5.2.2-darwin-x86_64/bin
➜  bin ./kibana
➜  bin ./kibana
  log   [14:11:01.882] [info][status][plugin:kibana@5.2.2] Status changed from uninitialized to green - Ready
  log   [14:11:01.972] [info][status][plugin:elasticsearch@5.2.2] Status changed from uninitialized to yellow - Waiting for Elasticsearch
  log   [14:11:01.994] [error][admin][elasticsearch] Request error, retrying
HEAD http://localhost:9200/ => connect ECONNREFUSED 127.0.0.1:9200
  log   [14:11:02.029] [warning][admin][elasticsearch] Unable to revive connection: http://localhost:9200/
  log   [14:11:02.030] [warning][admin][elasticsearch] No living connections
  log   [14:11:02.033] [info][status][plugin:console@5.2.2] Status changed from uninitialized to green - Ready
  log   [14:11:02.038] [error][status][plugin:elasticsearch@5.2.2] Status changed from yellow to red - Unable to connect to Elasticsearch at http://localhost:9200.
  log   [14:11:02.273] [info][status][plugin:timelion@5.2.2] Status changed from uninitialized to green - Ready
  log   [14:11:02.279] [info][listening] Server running at http://localhost:5601
  log   [14:11:02.281] [error][status][ui settings] Status changed from uninitialized to red - Elasticsearch plugin is red
  log   [14:11:04.544] [warning][admin][elasticsearch] Unable to revive connection: http://localhost:9200/
  log   [14:11:04.546] [warning][admin][elasticsearch] No living connections

```

# 安装位置
    1./usr/local/Cellar/logstash/5.2.2
    2./Users/apple/opt/kibana-5.2.2-darwin-x86_64/bin
    3./usr/local/Cellar/elasticsearch
    
# 配置文件路径
    1./usr/local/Cellar/logstash/5.2.2/libexec
```concept
➜  libexec ll
total 64
-rw-r--r--   1 apple  admin   2249  2 25 01:41 CONTRIBUTORS
-rw-r--r--   1 apple  admin   3864  2 25 01:46 Gemfile
-rw-r--r--   1 apple  admin  21251  2 25 01:41 Gemfile.jruby-1.9.lock
drwxr-xr-x  10 apple  admin    340  3 15 21:56 bin
drwxr-xr-x   6 apple  admin    204  3 15 21:56 config
drwxr-xr-x   4 apple  admin    136  3 15 22:00 data
drwxr-xr-x   5 apple  admin    170  3 15 21:56 lib
drwxr-xr-x   5 apple  admin    170  3 16 09:35 logs
drwxr-xr-x   6 apple  admin    204  3 15 21:56 logstash-core
drwxr-xr-x   5 apple  admin    170  3 15 21:56 logstash-core-event-java
drwxr-xr-x   4 apple  admin    136  3 15 21:56 logstash-core-plugin-api
drwxr-xr-x   5 apple  admin    170  3 15 21:56 logstash-core-queue-jruby
drwxr-xr-x   4 apple  admin    136  3 15 21:56 vendor
➜  libexec ll config 
total 40
-rw-r--r--   1 apple  admin  1738  2 25 01:41 jvm.options
-rw-r--r--   1 apple  admin  3958  2 25 01:41 log4j2.properties
-rw-r--r--   1 apple  admin  4436  2 25 01:41 logstash.yml
-rw-r--r--   1 apple  admin  1701  2 25 01:41 startup.options
➜  libexec ll data 
total 8
drwxr-xr-x   2 apple  admin   68  3 15 22:00 queue
-rw-r--r--   1 apple  admin   36  3 15 22:00 uuid
➜  libexec ll logs
total 16
-rw-r--r--   1 apple  admin  795  3 15 22:01 logstash-plain-2017-03-15.log
-rw-r--r--   1 apple  admin  594  3 16 09:36 logstash-plain.log
-rw-r--r--   1 apple  admin    0  3 15 22:00 logstash-slowlog-plain.log
➜  libexec
```
    2./usr/local/Cellar/elasticsearch
    elasticsearch.yml 配置文件
        a. path.data: /usr/local/var/elasticsearch/
        b. path.logs: /usr/local/var/log/elasticsearch/ 
        
```concept
➜  libexec pwd
/usr/local/Cellar/elasticsearch/5.2.2/libexec
➜  libexec ls -l
total 8
drwxr-xr-x   7 apple  admin   238  3 15 22:20 bin
lrwxr-xr-x   1 apple  admin    28  3 15 22:20 config -> /usr/local/etc/elasticsearch
drwxr-xr-x  35 apple  admin  1190  2 25 01:29 lib
drwxr-xr-x  12 apple  admin   408  2 25 01:29 modules
drwxr-xr-x   2 apple  admin    68  3 15 22:20 plugins
➜  libexec ls -l config 
lrwxr-xr-x  1 apple  admin  28  3 15 22:20 config -> /usr/local/etc/elasticsearch
➜  libexec ls -l config/
elasticsearch.yml  jvm.options        log4j2.properties  scripts/ 
```
log 查看:
```concept
1.参考README.textile 创建数据并查询
➜  bin curl -XPUT 'http://localhost:9200/twitter/tweet/1?pretty' -d '
quote> {
    "user": "kimchy",
    "post_date": "2009-11-15T13:12:00",
    "message": "Trying out Elasticsearch, so far so good?"
}'
{
  "_index" : "twitter",
  "_type" : "tweet",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "created" : true
}
➜  bin curl -XPUT 'http://localhost:9200/twitter/tweet/2?pretty' -d '
quote> {
    "user": "kimchy",
    "post_date": "2009-11-15T14:12:12",
    "message": "Another tweet, will it be indexed?"
} 
quote> ' 
{
  "_index" : "twitter",
  "_type" : "tweet",
  "_id" : "2",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "created" : true
}
➜  bin curl -XGET 'http://localhost:9200/twitter/user/kimchy?pretty=true'
{
  "_index" : "twitter",
  "_type" : "user",
  "_id" : "kimchy",
  "_version" : 1,
  "found" : true,
  "_source" : {
    "name" : "Shay Banon"
  }
}
➜  bin curl -XGET 'http://localhost:9200/twitter/tweet/1?pretty=true'
{
  "_index" : "twitter",
  "_type" : "tweet",
  "_id" : "1",
  "_version" : 1,
  "found" : true,
  "_source" : {
    "user" : "kimchy",
    "post_date" : "2009-11-15T13:12:00",
    "message" : "Trying out Elasticsearch, so far so good?"
  }
}
➜  bin

2.查看log
➜  elasticsearch pwd
/usr/local/var/log/elasticsearch
➜  elasticsearch ll
total 24
drwxr-xr-x  6 apple  admin   204  3 16 09:28 .
drwxr-xr-x  4 apple  admin   136  3 16 09:27 ..
-rw-r--r--  1 apple  admin  3687  3 16 09:57 elasticsearch_apple.log
-rw-r--r--  1 apple  admin  4785  3 16 09:58 elasticsearch_apple_deprecation.log
-rw-r--r--  1 apple  admin     0  3 16 09:28 elasticsearch_apple_index_indexing_slowlog.log
-rw-r--r--  1 apple  admin     0  3 16 09:28 elasticsearch_apple_index_search_slowlog.log
➜  elasticsearch cat elasticsearch_apple.log 
[2017-03-16T09:28:14,111][INFO ][o.e.n.Node               ] [] initializing ...
[2017-03-16T09:28:14,214][INFO ][o.e.e.NodeEnvironment    ] [dil84tY] using [1] data paths, mounts [[/ (/dev/disk0s2)]], net usable_space [153.6gb], net total_space [232gb], spins? [unknown], types [hfs]
[2017-03-16T09:28:14,215][INFO ][o.e.e.NodeEnvironment    ] [dil84tY] heap size [1.9gb], compressed ordinary object pointers [true]
[2017-03-16T09:28:14,216][INFO ][o.e.n.Node               ] node name [dil84tY] derived from node ID [dil84tYgTpKwpJ8rIN9WOg]; set [node.name] to override
[2017-03-16T09:28:14,219][INFO ][o.e.n.Node               ] version[5.2.2], pid[61352], build[f9d9b74/2017-02-24T17:26:45.835Z], OS[Mac OS X/10.12.3/x86_64], JVM[Oracle Corporation/Java HotSpot(TM) 64-Bit Server VM/1.8.0_121/25.121-b13]
[2017-03-16T09:28:15,330][INFO ][o.e.p.PluginsService     ] [dil84tY] loaded module [aggs-matrix-stats]
[2017-03-16T09:28:15,330][INFO ][o.e.p.PluginsService     ] [dil84tY] loaded module [ingest-common]
[2017-03-16T09:28:15,330][INFO ][o.e.p.PluginsService     ] [dil84tY] loaded module [lang-expression]
[2017-03-16T09:28:15,330][INFO ][o.e.p.PluginsService     ] [dil84tY] loaded module [lang-groovy]
[2017-03-16T09:28:15,330][INFO ][o.e.p.PluginsService     ] [dil84tY] loaded module [lang-mustache]
[2017-03-16T09:28:15,331][INFO ][o.e.p.PluginsService     ] [dil84tY] loaded module [lang-painless]
[2017-03-16T09:28:15,331][INFO ][o.e.p.PluginsService     ] [dil84tY] loaded module [percolator]
[2017-03-16T09:28:15,331][INFO ][o.e.p.PluginsService     ] [dil84tY] loaded module [reindex]
[2017-03-16T09:28:15,331][INFO ][o.e.p.PluginsService     ] [dil84tY] loaded module [transport-netty3]
[2017-03-16T09:28:15,331][INFO ][o.e.p.PluginsService     ] [dil84tY] loaded module [transport-netty4]
[2017-03-16T09:28:15,331][INFO ][o.e.p.PluginsService     ] [dil84tY] no plugins loaded
[2017-03-16T09:28:18,263][INFO ][o.e.n.Node               ] initialized
[2017-03-16T09:28:18,263][INFO ][o.e.n.Node               ] [dil84tY] starting ...
[2017-03-16T09:28:23,540][INFO ][o.e.t.TransportService   ] [dil84tY] publish_address {127.0.0.1:9300}, bound_addresses {[fe80::1]:9300}, {[::1]:9300}, {127.0.0.1:9300}
[2017-03-16T09:28:26,799][INFO ][o.e.c.s.ClusterService   ] [dil84tY] new_master {dil84tY}{dil84tYgTpKwpJ8rIN9WOg}{rGrad0ZMSTygV2LlKSOWtA}{127.0.0.1}{127.0.0.1:9300}, reason: zen-disco-elected-as-master ([0] nodes joined)
[2017-03-16T09:28:26,819][INFO ][o.e.h.HttpServer         ] [dil84tY] publish_address {127.0.0.1:9200}, bound_addresses {[fe80::1]:9200}, {[::1]:9200}, {127.0.0.1:9200}
[2017-03-16T09:28:26,819][INFO ][o.e.n.Node               ] [dil84tY] started
[2017-03-16T09:28:26,825][INFO ][o.e.g.GatewayService     ] [dil84tY] recovered [0] indices into cluster_state
[2017-03-16T09:28:34,136][INFO ][o.e.c.m.MetaDataCreateIndexService] [dil84tY] [.kibana] creating index, cause [api], templates [], shards [1]/[1], mappings [server, config]
[2017-03-16T09:34:24,582][INFO ][o.e.c.m.MetaDataMappingService] [dil84tY] [.kibana/Numw0U5GSNiVZy37m6NkDg] create_mapping [index-pattern]
[2017-03-16T09:34:42,582][INFO ][o.e.c.m.MetaDataMappingService] [dil84tY] [.kibana/Numw0U5GSNiVZy37m6NkDg] create_mapping [timelion-sheet]
[2017-03-16T09:56:05,716][INFO ][o.e.c.m.MetaDataCreateIndexService] [dil84tY] [twitter] creating index, cause [auto(index api)], templates [], shards [5]/[1], mappings []
[2017-03-16T09:56:05,802][INFO ][o.e.c.m.MetaDataMappingService] [dil84tY] [twitter/wKZ4BpxzRj2kyekQYJVEmA] create_mapping [user]
[2017-03-16T09:57:01,188][INFO ][o.e.c.m.MetaDataMappingService] [dil84tY] [twitter/wKZ4BpxzRj2kyekQYJVEmA] create_mapping [tweet]
➜  elasticsearch cat elasticsearch_apple_deprecation.log 
[2017-03-16T09:28:15,537][WARN ][o.e.d.s.g.GroovyScriptEngineService] [groovy] scripts are deprecated, use [painless] scripts instead
[2017-03-16T09:28:34,102][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [buildNum]
[2017-03-16T09:34:24,572][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [title]
[2017-03-16T09:34:24,575][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [timeFieldName]
[2017-03-16T09:34:24,576][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [intervalName]
[2017-03-16T09:34:24,576][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [fields]
[2017-03-16T09:34:24,577][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [sourceFilters]
[2017-03-16T09:34:24,577][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [fieldFormatMap]
[2017-03-16T09:34:24,579][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [title]
[2017-03-16T09:34:24,579][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [timeFieldName]
[2017-03-16T09:34:24,579][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [intervalName]
[2017-03-16T09:34:24,579][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [fields]
[2017-03-16T09:34:24,580][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [sourceFilters]
[2017-03-16T09:34:24,580][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [fieldFormatMap]
[2017-03-16T09:34:42,571][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [title]
[2017-03-16T09:34:42,575][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [description]
[2017-03-16T09:34:42,576][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [timelion_sheet]
[2017-03-16T09:34:42,576][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [timelion_interval]
[2017-03-16T09:34:42,576][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [timelion_other_interval]
[2017-03-16T09:34:42,576][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [searchSourceJSON]
[2017-03-16T09:34:42,578][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [title]
[2017-03-16T09:34:42,578][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [description]
[2017-03-16T09:34:42,579][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [timelion_sheet]
[2017-03-16T09:34:42,579][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [timelion_interval]
[2017-03-16T09:34:42,579][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [timelion_other_interval]
[2017-03-16T09:34:42,579][WARN ][o.e.d.i.m.StringFieldMapper$TypeParser] The [string] field is deprecated, please use [text] or [keyword] instead on [searchSourceJSON]
[2017-03-16T09:34:42,859][WARN ][o.e.d.i.q.QueryParseContext] query malformed, empty clause found at [1:143]
[2017-03-16T09:35:11,791][WARN ][o.e.d.i.q.QueryParseContext] query malformed, empty clause found at [1:143]
[2017-03-16T09:36:18,150][WARN ][o.e.d.i.q.QueryParseContext] query malformed, empty clause found at [1:143]
[2017-03-16T09:40:12,472][WARN ][o.e.d.i.q.QueryParseContext] query malformed, empty clause found at [1:143]
[2017-03-16T09:58:26,163][WARN ][o.e.d.i.q.QueryParseContext] query malformed, empty clause found at [1:143]
➜  elasticsearch 
```