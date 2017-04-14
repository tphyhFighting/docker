## pyenv
```bash
[root@VM_103_136_centos python]# which python
/root/.pyenv/shims/python
[root@VM_103_136_centos python]# pyenv shell 3.5.1
[root@VM_103_136_centos python]# pyenv rehash
[root@VM_103_136_centos python]# python
Python 3.5.1 (default, Apr 14 2017, 17:01:18) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-17)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
[root@VM_103_136_centos python]# pyenv shell system
[root@VM_103_136_centos python]# pyenv rehash
[root@VM_103_136_centos python]# which python
/root/.pyenv/shims/python
[root@VM_103_136_centos python]# python
Python 2.6.6 (r266:84292, Aug 18 2016, 15:13:37) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-17)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
KeyboardInterrupt
>>> 
[root@VM_103_136_centos python]# python --version
Python 2.6.6
[root@VM_103_136_centos python]# which python
/root/.pyenv/shims/python
```
