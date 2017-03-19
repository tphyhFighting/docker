## ruby docker 
##1. install
    1.brew install ruby
    2.docker
```concept
➜  5.2.2 docker pull ruby:2.4-slim
2.4-slim: Pulling from library/ruby
➜  5.2.2 docker run -it ruby:2.4-slim bash
root@2d6f77542124:/# ls
bin  boot  dev	etc  home  lib	lib64  media  mnt  opt	proc  root  run  sbin  srv  sys  tmp  usr  var
root@2d6f77542124:/# ruby --version
ruby 2.4.0p0 (2016-12-24 revision 57164) [x86_64-linux]
root@2d6f77542124:/# gem
RubyGems is a sophisticated package manager for Ruby.  This is a
basic help message containing pointers to more information.

  Usage:
    gem -h/--help
    gem -v/--version
    gem command [arguments...] [options...]

  Examples:
    gem install rake
    gem list --local
    gem build package.gemspec
    gem help install

  Further help:
    gem help commands            list all 'gem' commands
    gem help examples            show some examples of usage
    gem help gem_dependencies    gem dependencies file guide
    gem help platforms           gem platforms guide
    gem help <COMMAND>           show help on COMMAND
                                   (e.g. 'gem help install')
    gem server                   present a web page at
                                 http://localhost:8808/
                                 with info about installed gems
  Further information:
    http://guides.rubygems.org
root@2d6f77542124:/#
root@2d6f77542124:/# env
HOSTNAME=2d6f77542124
GEM_HOME=/usr/local/bundle
TERM=xterm
BUNDLE_SILENCE_ROOT_WARNING=1
BUNDLE_APP_CONFIG=/usr/local/bundle
PATH=/usr/local/bundle/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUBY_DOWNLOAD_SHA256=3a87fef45cba48b9322236be60c455c13fd4220184ce7287600361319bb63690
PWD=/
RUBY_MAJOR=2.4
RUBYGEMS_VERSION=2.6.10
BUNDLE_BIN=/usr/local/bundle/bin
SHLVL=1
HOME=/root
no_proxy=127.0.0.1, localhost
BUNDLE_PATH=/usr/local/bundle
RUBY_VERSION=2.4.0
BUNDLER_VERSION=1.14.6
_=/usr/bin/env
root@2d6f77542124:/# 
```
## 
## 
