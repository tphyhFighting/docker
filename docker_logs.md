##docker logs

##since 某个时间点
docker logs -f --since "2017-04-04"
➜  docker git:(go) ✗ docker logs --help
Usage:	docker logs [OPTIONS] CONTAINER

Fetch the logs of a container

Options:
      --details        Show extra details provided to logs
  -f, --follow         Follow log output
      --help           Print usage
      --since string   Show logs since timestamp
      --tail string    Number of lines to show from the end of the logs (default "all")
  -t, --timestamps     Show timestamps
➜  docker git:(go) ✗