##编译镜像题调试
➜  smart-backup git:(1-) ✗ docker run -it  --rm -v "`pwd`":/go/src/smart-backup  -w /go/src/smart-backup golang:1.7-alpine  sh
/go/src/smart-backup # ls
Dockerfile.app  LICENSE         README.md       cmd             contrib         glide.yaml      logger          storage         utils
Dockerfile.env  Makefile        build           conf            glide.lock      job             main.go         tmp             vendor
/go/src/smart-backup # go build
^C
/go/src/smart-backup # go env
GOARCH="amd64"
GOBIN=""
GOEXE=""
GOHOSTARCH="amd64"
GOHOSTOS="linux"
GOOS="linux"
GOPATH="/go"
GORACE=""
GOROOT="/usr/local/go"
GOTOOLDIR="/usr/local/go/pkg/tool/linux_amd64"
CC="gcc"
GOGCCFLAGS="-fPIC -m64 -pthread -fmessage-length=0"
CXX="g++"
CGO_ENABLED="1"
/go/src/smart-backup # go build
/go/src/smart-backup # ls
Dockerfile.app  LICENSE         README.md       cmd             contrib         glide.yaml      logger          smart-backup    tmp             vendor
Dockerfile.env  Makefile        build           conf            glide.lock      job             main.go         storage         utils
/go/src/smart-backup # ./smart-backup
A longer description that spans multiple lines and likely contains
examples and usage of using your application. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.

Usage:
  smart-backup [command]

Available Commands:
  cron        Run cron backup job
  help        Help about any command
  run         Run backup job
  simulate    Simulate run cron backup job
  version     Show version

Flags:
      --config string   config file (default is $HOME/.smart-backup.yaml)
  -t, --toggle          Help message for toggle

Use "smart-backup [command] --help" for more information about a command.
/go/src/smart-backup #