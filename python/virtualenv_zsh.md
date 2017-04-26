### mac 下virtualenvwrapper 异常
### 问题
```bash
Last login: Wed Apr 26 16:02:24 on ttys006
/usr/local/opt/python/bin/python2.7: No module named virtualenvwrapper
virtualenvwrapper.sh: There was a problem running the initialization hooks.

If Python could not import the module virtualenvwrapper.hook_loader,
check that virtualenvwrapper has been installed for
VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python and that PATH is
set properly.
```
### 分析
```bash
1.查看/usr/local/bin/virtualenvwrapper.sh +217
217 # Run the hooks
 218 function virtualenvwrapper_run_hook {
 219     typeset hook_script
 220     typeset result
 221
 222     hook_script="$(virtualenvwrapper_tempfile ${1}-hook)" || return 1
 223
 224     # Use a subshell to run the python interpreter with hook_loader so
 225     # we can change the working directory. This avoids having the
 226     # Python 3 interpreter decide that its "prefix" is the virtualenv
 227     # if we happen to be inside the virtualenv when we start.
 228     ( \
 229         virtualenvwrapper_cd "$WORKON_HOME" &&
 230         "$VIRTUALENVWRAPPER_PYTHON" -m 'virtualenvwrapper.hook_loader' \
 231             $HOOK_VERBOSE_OPTION --script "$hook_script" "$@" \
 232     )
 233     result=$?
 234
 235     if [ $result -eq 0 ]
 236     then
 237         if [ ! -f "$hook_script" ]
 238         then
 239             echo "ERROR: virtualenvwrapper_run_hook could not find temporary file $hook_script" 1>&2
 240             command \rm -f "$hook_script"
 241             return 2
 242         fi
 243         # cat "$hook_script"
 244         source "$hook_script"
 245     elif [ "${1}" = "initialize" ]
 246     then
 247         cat - 1>&2 <<EOF
 248 virtualenvwrapper.sh: There was a problem running the initialization hooks.
 249
 250 If Python could not import the module virtualenvwrapper.hook_loader,
 251 check that virtualenvwrapper has been installed for
 252 VIRTUALENVWRAPPER_PYTHON=$VIRTUALENVWRAPPER_PYTHON and that PATH is
 253 set properly.

 结论:
 230: 脚本在倒入virtualenvwrapper模块时出现异常, 打印了错误信息。
    解决方法：  手动处理掉吧。。。。

 本质原因:
 python 找不到virtualenvwrapper模包
 线索:
    1.VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python : virutalxx  使用了/usr/local/bin/python
    
    ➜  ~ ll /usr/local/bin/python
    lrwxr-xr-x  1 apple  admin  34  3 28 19:31 /usr/local/bin/python -> ../Cellar/python/2.7.13/bin/python
    ➜  ~ ll /usr/local/Cellar/python/2.7.13/bin/python
    lrwxr-xr-x  1 apple  admin  54 12 18 04:05 /usr/local/Cellar/python/2.7.13/bin/python -> ../Frameworks/Python.framework/Versions/2.7/bin/python
    ➜  ~
```
#### 查看python 环境 
```bash
➜  ~ which python
/usr/local/bin/python
➜  ~ python
Python 2.7.13 (default, Dec 18 2016, 07:03:39)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> virtualenvwrapper.hook_loade
KeyboardInterrupt
>>> import virtualenvwrapper.hook_loade
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named virtualenvwrapper.hook_loade
>>> import virtualenvwrapper
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named virtualenvwrapper
>>>
```
#### 安装python virtualenvwrapper包
```bash
➜  ~ sudo pip install virtualenvwrapper
Password:
The directory '/Users/apple/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/apple/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting virtualenvwrapper
  Downloading virtualenvwrapper-4.7.2.tar.gz (90kB)
    100% |████████████████████████████████| 92kB 115kB/s
Requirement already satisfied: virtualenv in /usr/local/lib/python2.7/site-packages (from virtualenvwrapper)
Collecting virtualenv-clone (from virtualenvwrapper)
  Downloading virtualenv-clone-0.2.6.tar.gz
Collecting stevedore (from virtualenvwrapper)
  Downloading stevedore-1.21.0-py2.py3-none-any.whl
Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python2.7/site-packages (from stevedore->virtualenvwrapper)
Collecting pbr>=2.0.0 (from stevedore->virtualenvwrapper)
  Downloading pbr-3.0.0-py2.py3-none-any.whl (98kB)
    100% |████████████████████████████████| 102kB 8.8MB/s
Installing collected packages: virtualenv-clone, pbr, stevedore, virtualenvwrapper
  Running setup.py install for virtualenv-clone ... done
  Running setup.py install for virtualenvwrapper ... done
Successfully installed pbr-3.0.0 stevedore-1.21.0 virtualenv-clone-0.2.6 virtualenvwrapper-4.7.2
➜  ~ source .zshrc
➜  ~ 
```
#### finish
