##### go build

##### -ldflags 
```bash
➜  smart-backup git:(master) go build -ldflags --help
# smart-backup
usage: link [options] main.o
  -B note
    	add an ELF NT_GNU_BUILD_ID note when using ELF
  -D address
    	set data segment address (default -1)
  -E entry
    	set entry symbol name
  -H type
    	set header type
  -I linker
    	use linker as ELF dynamic linker
  -L directory
    	add specified directory to library path
  -R quantum
    	set address rounding quantum (default -1)
  -T address
    	set text segment addresGs (default -1)
  -V	print version and exit
  -X definition
    	add string value definition of the form importpath.name=value
  -a	disassemble output
  -buildid id
    	record id as Go toolchain build id
  -buildmode mode
    	set build mode
  -c	dump call graph
  -cpuprofile file
    	write cpu profile to file
  -d	disable dynamic executable
  -debugtramp int
    	debug trampolines
  -dumpdep
    	dump symbol dependency graph
  -extar string
    	archive program for buildmode=c-archive
  -extld linker
    	use linker when linking in external mode
  -extldflags flags
    	pass flags to external linker
  -f	ignore version mismatch
  -g	disable go package data checks
  -h	halt on error
  -installsuffix suffix
    	set package directory suffix
  -k symbol
    	set field tracking symbol
  -libgcc string
    	compiler support lib for internal linking; use "none" to disable
  -linkmode mode
    	set link mode
  -linkshared
    	link against installed Go shared libraries
  -memprofile file
    	write memory profile to file
  -memprofilerate rate
    	set runtime.MemProfileRate to rate
  -msan
    	enable MSan interface
  -n	dump symbol table
  -o file
    	write output to file
  -pluginpath string
    	full path name for plugin
  -r path
    	set the ELF dynamic linker search path to dir1:dir2:...
  -race
    	enable race detector
  -s	disable symbol table
  -tmpdir directory
    	use directory for temporary files
  -u	reject unsafe packages
  -v	print link trace
  -w	disable DWARF generation
➜  smart-backup git:(master)
```

##### 使用-X 设置编译时变量
```bash
➜  smart-backup git:(master) go build -ldflags "-X smart-backup/cmd.AppVersion=`git describe --tags` -X smart-backup/cmd.BuildTime=`date '+%Y-%m-%d_%H:%M:%S'`"
➜  smart-backup git:(master) ./smart-backup version
App Version:  1.0-1-g783defd
Go Version:  go1.8
Build Time:  2017-04-27_11:48:25
➜  smart-backup git:(master)
```
```
bash
查看调试信息
set -ex
```
