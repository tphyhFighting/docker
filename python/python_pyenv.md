## pyenv简介——Debian/Ubuntu中管理多版本Python
http://blog.codylab.com/python-pyenv-management/
http://www.jianshu.com/p/002c425041fb

#一、安装pyenv  && 修改环境变量
    git clone https://github.com/yyuu/pyenv.git ~/.pyenv
    将PYENV_ROOT和pyenv init加入bash的~/.bashrc（或zsh的~/.zshrc）
    echo 'export PATH=~/.pyenv/bin:$PATH' >> ~/.bashrc
    echo 'export PYENV_ROOT=~/.pyenv' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc

#二. 安装python3.5 ipython
    1.安装python版本
        pyenv install 3.5.0
        
    2.创建python3.5 的虚拟环境, 添加到.bashrc中
    virtualenv -p ~/.pyenv/versions/3.5.0/bin/python3.5 python3.5_test
    
    
    3.把python3.5的可执行路径添加到环境变量中
    virtualenv -p python3.5 celery
    mkvirtualenv -p python3.5 https
    workon https
    
    4.在虚拟环境安装ipython
    
```python
(celery) ➜  celery pip install ipython
Collecting ipython
  Using cached ipython-5.2.2-py3-none-any.whl
Requirement already satisfied: pygments in ./lib/python3.5/site-packages (from ipython)
Requirement already satisfied: setuptools>=18.5 in ./lib/python3.5/site-packages (from ipython)
Requirement already satisfied: pickleshare in ./lib/python3.5/site-packages (from ipython)
Requirement already satisfied: pexpect; sys_platform != "win32" in ./lib/python3.5/site-packages (from ipython)
Requirement already satisfied: appnope; sys_platform == "darwin" in ./lib/python3.5/site-packages (from ipython)
Requirement already satisfied: traitlets>=4.2 in ./lib/python3.5/site-packages (from ipython)
Requirement already satisfied: decorator in ./lib/python3.5/site-packages (from ipython)
Requirement already satisfied: simplegeneric>0.8 in ./lib/python3.5/site-packages (from ipython)
Requirement already satisfied: prompt-toolkit<2.0.0,>=1.0.4 in ./lib/python3.5/site-packages (from ipython)
Requirement already satisfied: six>=1.6.0 in ./lib/python3.5/site-packages (from setuptools>=18.5->ipython)
Requirement already satisfied: appdirs>=1.4.0 in ./lib/python3.5/site-packages (from setuptools>=18.5->ipython)
Requirement already satisfied: packaging>=16.8 in ./lib/python3.5/site-packages (from setuptools>=18.5->ipython)
Requirement already satisfied: ptyprocess>=0.5 in ./lib/python3.5/site-packages (from pexpect; sys_platform != "win32"->ipython)
Requirement already satisfied: ipython-genutils in ./lib/python3.5/site-packages (from traitlets>=4.2->ipython)
Requirement already satisfied: wcwidth in ./lib/python3.5/site-packages (from prompt-toolkit<2.0.0,>=1.0.4->ipython)
Requirement already satisfied: pyparsing in ./lib/python3.5/site-packages (from packaging>=16.8->setuptools>=18.5->ipython)
Installing collected packages: ipython
Successfully installed ipython-5.2.2
(celery) ➜  celery which ipython
/Users/apple/celery/bin/ipython
(celery) ➜  celery ipython 
Python 3.5.0 (default, Feb 13 2017, 12:06:45) 
Type "copyright", "credits" or "license" for more information.

IPython 5.2.2 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: 
```