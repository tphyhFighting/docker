## fabric 远程操作

#0x01 imgfit  部署
    1.fab -H fs12t01 imgfit_up_bin  #更新bin 
    2.fab -H fs12t01 imgfit_up      #重启服务
```python
    cmd = [__bin, ' -logtostderr']

    systemd.setup_simple(systemd_name,
                         app_run_cmd=' '.join(cmd),
                         work_path=__install_path,
                         run_user=__user,
                         run_group=__group,
                         description=__description,
                         addition_service_setting={'LimitNOFILE': 40960},
                         )
    systemd.restart(systemd_name) 
    systemd.status(systemd_name)
```
#0x02 log 获取
    1.fab -H fs12t01 hyh_log_imgfit
```python
@task
def hyh_log_imgfit():
    run("journalctl -u imgfit -f ")
```
    2.fab -H fs12t01 hyh_log_docker_abuse_robot
```shell
➜  serv-ops git:(local) ✗ fab -H fs12t01 hyh_log_docker_abuse_robot
['hyh_log_docker_abuse_robot']
Found host by [name], fs12t01: root@167.114.175.4:4550
[root@167.114.175.4:4550] Executing task 'hyh_log_docker_abuse_robot'
[root@167.114.175.4:4550] run: docker ps -a
[root@167.114.175.4:4550] out: CONTAINER ID        IMAGE                                      COMMAND                  CREATED             STATUS              PORTS               NAMES
[root@167.114.175.4:4550] out: bc93de8cde45        registry.pureapk.com/apkpure/abuse-robot   "/bin/sh -c 'pytho..."   3 days ago          Up About an hour                        abuse-robot
[root@167.114.175.4:4550] out: 
```
#0x03 docker 命令运行
#0x04 abuse-robot 部署
#0x05


