G## docker 学习笔记


## 1.dockefile
	目录:
		dockerfile/01/ 简单的nginx 服务
		dockerfile/02/ 演示onbuild 镜像触发器
		
		
## 2.docker build 过程
    1.每一条构建指定都会在上一次构建的容器上构建
    2.可以看到每一层的镜像id
    3.构建完成会删除中间层的容器
    4.但是不会删除中间层的镜像， 方便下一次构建时命中缓存
```
➜  docker git:(master) ✗ docker build -t u1:v1.0 . -f dockerFile/01/Dockerfile 
Sending build context to Docker daemon 344.6 kB
Step 1/7 : FROM debian:jessie-slim
 ---> 7d86024f45a4
Step 2/7 : MAINTAINER huoyinghui "huoyinghui@qpkpure.com"
 ---> Using cache
 ---> e5979465026f
Step 3/7 : RUN apt-get update
 ---> Running in a3faf47dcGdd8
Get:1 http://security.debian.org jessie/updates InRelease [63.1 kB]
Ign http://deb.debian.org jessie InRelease
Get:2 http://deb.debian.org jessie-updates InRelease [145 kB]
Get:3 http://security.debian.org jessie/updates/main amd64 Packages [448 kB]
Get:4 http://deb.debian.org jessie Release.gpg [2373 B]
Get:5 http://deb.debian.org jessie-updates/main amd64 Packages [17.6 kB]
Get:6 http://deb.debian.org jessie Release [148 kB]
Get:7 http://deb.debian.org jessie/main amd64 Packages [9049 kB]
Fetched 9874 kB in 10min 19s (15.9 kB/s)
Reading package lists...
 ---> d3cf54443ea3
Removing intermediate container a3faf47dcdd8
Step 4/7 : RUN apt-get install -y nginx
 ---> Running in b434a38c3e69
Reading package lists...
Building dependency tree...
The following extra packages will be installed:
  fontconfig-config fonts-dejavu-core geoip-database init-system-helpers
  libalgorithm-c3-perl libarchive-extract-perl libcgi-fast-perl libcgi-pm-perl
  libclass-c3-perl libclass-c3-xs-perl libcpan-meta-perl libdata-optlist-perl
  libdata-section-perl libexpat1 libfcgi-perl libfontconfig1 libfreetype6
  libgd3 libgdbm3 libgeoip1 libjbig0 libjpeg62-turbo liblog-message-perl
  liblog-message-simple-perl libmodule-build-perl libmodule-pluggable-perl
  libmodule-signature-perl libmro-compat-perl libpackage-constants-perl
  libparams-util-perl libpng12-0 libpod-latex-perl libpod-readme-perl
  libregexp-common-perl libsoftware-license-perl libssl1.0.0
  libsub-exporter-perl libsub-install-perl libterm-ui-perl
  libtext-soundex-perl libtext-template-perl libtiff5 libvpx1 libx11-6
  libx11-data libxau6 libxcb1 libxdmcp6 libxml2 libxpm4 libxslt1.1
  nginx-common nginx-full perl perl-modules rename sgml-base ucf xml-core
Suggested packages:
  libgd-tools geoip-bin fcgiwrap nginx-doc ssl-cert perl-doc
  libterm-readline-gnu-perl libterm-readline-perl-perl make libb-lint-perl
  libcpanplus-dist-build-perl libcpanplus-perl libfile-checktree-perl
  libobject-accessor-perl sgml-base-doc debhelper
Recommended packages:
  libarchive-tar-perl
The following NEW packages will be installed:
  fontconfig-config fonts-dejavu-core geoip-database init-system-helpers
  libalgorithm-c3-perl libarchive-extract-perl libcgi-fast-perl libcgi-pm-perl
  libclass-c3-perl libclass-c3-xs-perl libcpan-meta-perl libdata-optlist-perl
  libdata-section-perl libexpat1 libfcgi-perl libfontconfig1 libfreetype6
  libgd3 libgdbm3 libgeoip1 libjbig0 libjpeg62-turbo liblog-message-perl
  liblog-message-simple-perl libmodule-build-perl libmodule-pluggable-perl
  libmodule-signature-perl libmro-compat-perl libpackage-constants-perl
  libparams-util-perl libpng12-0 libpod-latex-perl libpod-readme-perl
  libregexp-common-perl libsoftware-license-perl libssl1.0.0
  libsub-exporter-perl libsub-install-perl libterm-ui-perl
  libtext-soundex-perl libtext-template-perl libtiff5 libvpx1 libx11-6
  libx11-data libxau6 libxcb1 libxdmcp6 libxml2 libxpm4 libxslt1.1 nginx
  nginx-common nginx-full perl perl-modules rename sgml-base ucf xml-core
0 upgraded, 60 newly installed, 0 to remove and 2 not upgraded.
Need to get 15.5 MB of archives.
After this operation, 63.0 MB of additional disk space will be used.
Get:1 http://security.debian.org/ jessie/updates/main libssl1.0.0 amd64 1.0.1t-1+deb8u6 [1047 kB]
Get:2 http://deb.debian.org/debian/ jessie/main libgdbm3 amd64 1.8.3-13.1 [30.0 kB]
Get:3 http://deb.debian.org/debian/ jessie/main libxml2 amd64 2.9.1+dfsg1-5+deb8u4 [802 kB]
Get:4 http://deb.debian.org/debian/ jessie/main perl-modules all 5.20.2-3+deb8u6 [2547 kB]
Get:5 http://security.debian.org/ jessie/updates/main libtiff5 amd64 4.0.3-12.3+deb8u2 [216 kB]
Get:6 http://security.debian.org/ jessie/updates/main libxpm4 amd64 1:3.5.12-0+deb8u1 [49.2 kB]
Get:7 http://security.debian.org/ jessie/updates/main libgd3 amd64 2.1.0-5+deb8u9 [148 kB]
Get:8 http://deb.debian.org/debian/ jessie/main perl amd64 5.20.2-3+deb8u6 [2637 kB]
Get:9 http://deb.debian.org/debian/ jessie/main libexpat1 amd64 2.1.0-6+deb8u3 [80.0 kB]
Get:10 http://deb.debian.org/debian/ jessie/main libpng12-0 amd64 1.2.50-2+deb8u3 [173 kB]
Get:11 http://deb.debian.org/debian/ jessie/main libfreetype6 amd64 2.5.2-3+deb8u1 [466 kB]
Get:12 http://deb.debian.org/debian/ jessie/main ucf all 3.0030 [69.7 kB]
Get:13 http://deb.debian.org/debian/ jessie/main fonts-dejavu-core all 2.34-1 [1047 kB]
Get:14 http://deb.debian.org/debian/ jessie/main fontconfig-config all 2.11.0-6.3+deb8u1 [274 kB]
Get:15 http://deb.debian.org/debian/ jessie/main libfontconfig1 amd64 2.11.0-6.3+deb8u1 [329 kB]
Get:16 http://deb.debian.org/debian/ jessie/main libjpeg62-turbo amd64 1:1.3.1-12 [116 kB]
Get:17 http://deb.debian.org/debian/ jessie/main libjbig0 amd64 2.1-3.1 [30.7 kB]
Get:18 http://deb.debian.org/debian/ jessie/main libvpx1 amd64 1.3.0-3 [599 kB]
Get:19 http://deb.debian.org/debian/ jessie/main libvpx1 amd64 1.3.0-3 [599 kB]
Get:20 http://deb.debian.org/debian/ jessie/main libxau6 amd64 1:1.0.8-1 [20.7 kB]
Get:21 http://deb.debian.org/debian/ jessie/main libxdmcp6 amd64 1:1.1.1-1+b1 [24.9 kB]
Get:22 http://deb.debian.org/debian/ jessie/main libxcb1 amd64 1.10-3+b1 [44.4 kB]
Get:23 http://deb.debian.org/debian/ jessie/main libx11-data all 2:1.6.2-3 [126 kB]
Get:24 http://deb.debian.org/debian/ jessie/main libx11-6 amd64 2:1.6.2-3 [729 kB]
Get:25 http://deb.debian.org/debian/ jessie/main libgeoip1 amd64 1.6.2-4 [90.8 kB]
Get:26 http://deb.debian.org/debian/ jessie/main libxslt1.1 amd64 1.1.28-2+deb8u2 [232 kB]
Get:27 http://deb.debian.org/debian/ jessie/main sgml-base all 1.26+nmu4 [14.6 kB]
Get:28 http://deb.debian.org/debian/ jessie/main init-system-helpers all 1.22 [14.0 kB]
Get:29 http://deb.debian.org/debian/ jessie/main geoip-database all 20150317-1 [1517 kB]
Get:30 http://deb.debian.org/debian/ jessie/main libalgorithm-c3-perl all 0.09-1 [11.9 kB]
Get:31 http://deb.debian.org/debian/ jessie/main libarchive-extract-perl all 0.72-1 [24.8 kB]
Get:32 http://deb.debian.org/debian/ jessie/main libcgi-pm-perl all 4.09-1 [213 kB]
Get:33 http://deb.debian.org/debian/ jessie/main libfcgi-perl amd64 0.77-1+deb8u1 [39.0 kB]
Get:34 http://deb.debian.org/debian/ jessie/main libcgi-fast-perl all 1:2.04-1 [10.9 kB]
Get:35 http://deb.debian.org/debian/ jessie/main libclass-c3-perl all 0.26-1 [22.9 kB]
Get:36 http://deb.debian.org/debian/ jessie/main libclass-c3-xs-perl amd64 0.13-2+b1 [15.2 kB]
Get:37 http://deb.debian.org/debian/ jessie/main libcpan-meta-perl all 2.142690-1 [125 kB]
Get:38 http://deb.debian.org/debian/ jessie/main libparams-util-perl amd64 1.07-2+b1 [23.5 kB]
Get:39 http://deb.debian.org/debian/ jessie/main libsub-install-perl all 0.928-1 [11.4 kB]
Get:40 http://deb.debian.org/debian/ jessie/main libdata-optlist-perl all 0.109-1 [10.6 kB]
Get:41 http://deb.debian.org/debian/ jessie/main libmro-compat-perl all 0.12-1 [13.2 kB]
Get:42 http://deb.debian.org/debian/ jessie/main libsub-exporter-perl all 0.986-1 [49.9 kB]
Get:43 http://deb.debian.org/debian/ jessie/main libdata-section-perl all 0.200006-1 [13.4 kB]
Get:44 http://deb.debian.org/debian/ jessie/main liblog-message-perl all 0.8-1 [26.0 kB]
Get:45 http://deb.debian.org/debian/ jessie/main liblog-message-simple-perl all 0.10-2 [8126 B]
Get:46 http://deb.debian.org/debian/ jessie/main libmodule-build-perl all 0.421000-2+deb8u1 [265 kB]
Get:47 http://deb.debian.org/debian/ jessie/main libmodule-pluggable-perl all 5.1-1 [25.0 kB]
Get:48 http://deb.debian.org/debian/ jessie/main libmodule-signature-perl all 0.73-1+deb8u2 [30.4 kB]
Get:49 http://deb.debian.org/debian/ jessie/main libpackage-constants-perl all 0.04-1 [5820 B]
Get:50 http://deb.debian.org/debian/ jessie/main libpod-latex-perl all 0.61-1 [34.7 kB]
Get:51 http://deb.debian.org/debian/ jessie/main libregexp-common-perl all 2013031301-1 [173 kB]
Get:52 http://deb.debian.org/debian/ jessie/main libpod-readme-perl all 0.11-1 [15.3 kB]
Get:53 http://deb.debian.org/debian/ jessie/main libtext-template-perl all 1.46-1 [53.1 kB]
Get:54 http://deb.debian.org/debian/ jessie/main libsoftware-license-perl all 0.103010-3 [119 kB]
Get:55 http://deb.debian.org/debian/ jessie/main libterm-ui-perl all 0.42-1 [19.1 kB]
Get:56 http://deb.debian.org/debian/ jessie/main libtext-soundex-perl amd64 3.4-1+b2 [13.7 kB]
Get:57 http://deb.debian.org/debian/ jessie/main nginx-common all 1.6.2-5+deb8u4 [88.1 kB]
Get:58 http://deb.debian.org/debian/ jessie/main nginx-full amd64 1.6.2-5+deb8u4 [430 kB]
Get:59 http://deb.debian.org/debian/ jessie/main nginx all 1.6.2-5+deb8u4 [72.6 kB]
Get:60 http://deb.debian.org/debian/ jessie/main rename all 0.20-3 [12.4 kB]
Get:61 http://deb.debian.org/debian/ jessie/main xml-core all 0.13+nmu2 [24.2 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 14.9 MB in 16min 32s (15.0 kB/s)
Selecting previously unselected package libgdbm3:amd64.
(Reading database ... 7559 files and directories currently installed.)
Preparing to unpack .../libgdbm3_1.8.3-13.1_amd64.deb ...
Unpacking libgdbm3:amd64 (1.8.3-13.1) ...
Selecting previously unselected package libssl1.0.0:amd64.
Preparing to unpack .../libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb ...
Unpacking libssl1.0.0:amd64 (1.0.1t-1+deb8u6) ...
Selecting previously unselected package libxml2:amd64.
Preparing to unpack .../libxml2_2.9.1+dfsg1-5+deb8u4_amd64.deb ...
Unpacking libxml2:amd64 (2.9.1+dfsg1-5+deb8u4) ...
Selecting previously unselected package perl-modules.
Preparing to unpack .../perl-modules_5.20.2-3+deb8u6_all.deb ...
Unpacking perl-modules (5.20.2-3+deb8u6) ...
Selecting previously unselected package perl.
Preparing to unpack .../perl_5.20.2-3+deb8u6_amd64.deb ...
Unpacking perl (5.20.2-3+deb8u6) ...
Selecting previously unselected package libexpat1:amd64.
Preparing to unpack .../libexpat1_2.1.0-6+deb8u3_amd64.deb ...
Unpacking libexpat1:amd64 (2.1.0-6+deb8u3) ...
Selecting previously unselected package libpng12-0:amd64.
Preparing to unpack .../libpng12-0_1.2.50-2+deb8u3_amd64.deb ...
Unpacking libpng12-0:amd64 (1.2.50-2+deb8u3) ...
Selecting previously unselected package libfreetype6:amd64.
Preparing to unpack .../libfreetype6_2.5.2-3+deb8u1_amd64.deb ...
Unpacking libfreetype6:amd64 (2.5.2-3+deb8u1) ...
Selecting previously unselected package ucf.
Preparing to unpack .../archives/ucf_3.0030_all.deb ...
Moving old data out of the way
Unpacking ucf (3.0030) ...
Selecting previously unselected package fonts-dejavu-core.
Preparing to unpack .../fonts-dejavu-core_2.34-1_all.deb ...
Unpacking fonts-dejavu-core (2.34-1) ...
Selecting previously unselected package fontconfig-config.
Preparing to unpack .../fontconfig-config_2.11.0-6.3+deb8u1_all.deb ...
Unpacking fontconfig-config (2.11.0-6.3+deb8u1) ...
Selecting previously unselected package libfontconfig1:amd64.
Preparing to unpack .../libfontconfig1_2.11.0-6.3+deb8u1_amd64.deb ...
Unpacking libfontconfig1:amd64 (2.11.0-6.3+deb8u1) ...
Selecting previously unselected package libjpeg62-turbo:amd64.
Preparing to unpack .../libjpeg62-turbo_1%3a1.3.1-12_amd64.deb ...
Unpacking libjpeg62-turbo:amd64 (1:1.3.1-12) ...
Selecting previously unselected package libjbig0:amd64.
Preparing to unpack .../libjbig0_2.1-3.1_amd64.deb ...
Unpacking libjbig0:amd64 (2.1-3.1) ...
Selecting previously unselected package libtiff5:amd64.
Preparing to unpack .../libtiff5_4.0.3-12.3+deb8u2_amd64.deb ...
Unpacking libtiff5:amd64 (4.0.3-12.3+deb8u2) ...
Selecting previously unselected package libvpx1:amd64.
Preparing to unpack .../libvpx1_1.3.0-3_amd64.deb ...
Unpacking libvpx1:amd64 (1.3.0-3) ...
Selecting previously unselected package libxau6:amd64.
Preparing to unpack .../libxau6_1%3a1.0.8-1_amd64.deb ...
Unpacking libxau6:amd64 (1:1.0.8-1) ...
Selecting previously unselected package libxdmcp6:amd64.
Preparing to unpack .../libxdmcp6_1%3a1.1.1-1+b1_amd64.deb ...
Unpacking libxdmcp6:amd64 (1:1.1.1-1+b1) ...
Selecting previously unselected package libxcb1:amd64.
Preparing to unpack .../libxcb1_1.10-3+b1_amd64.deb ...
Unpacking libxcb1:amd64 (1.10-3+b1) ...
Selecting previously unselected package libx11-data.
Preparing to unpack .../libx11-data_2%3a1.6.2-3_all.deb ...
Unpacking libx11-data (2:1.6.2-3) ...
Selecting previously unselected package libx11-6:amd64.
Preparing to unpack .../libx11-6_2%3a1.6.2-3_amd64.deb ...
Unpacking libx11-6:amd64 (2:1.6.2-3) ...
Selecting previously unselected package libxpm4:amd64.
Preparing to unpack .../libxpm4_1%3a3.5.12-0+deb8u1_amd64.deb ...
Unpacking libxpm4:amd64 (1:3.5.12-0+deb8u1) ...
Selecting previously unselected package libgd3:amd64.
Preparing to unpack .../libgd3_2.1.0-5+deb8u9_amd64.deb ...
Unpacking libgd3:amd64 (2.1.0-5+deb8u9) ...
Selecting previously unselected package libgeoip1:amd64.
Preparing to unpack .../libgeoip1_1.6.2-4_amd64.deb ...
Unpacking libgeoip1:amd64 (1.6.2-4) ...
Selecting previously unselected package libxslt1.1:amd64.
Preparing to unpack .../libxslt1.1_1.1.28-2+deb8u2_amd64.deb ...
Unpacking libxslt1.1:amd64 (1.1.28-2+deb8u2) ...
Selecting previously unselected package sgml-base.
Preparing to unpack .../sgml-base_1.26+nmu4_all.deb ...
Unpacking sgml-base (1.26+nmu4) ...
Selecting previously unselected package init-system-helpers.
Preparing to unpack .../init-system-helpers_1.22_all.deb ...
Unpacking init-system-helpers (1.22) ...
Selecting previously unselected package geoip-database.
Preparing to unpack .../geoip-database_20150317-1_all.deb ...
Unpacking geoip-database (20150317-1) ...
Selecting previously unselected package libalgorithm-c3-perl.
Preparing to unpack .../libalgorithm-c3-perl_0.09-1_all.deb ...
Unpacking libalgorithm-c3-perl (0.09-1) ...
Selecting previously unselected package libarchive-extract-perl.
Preparing to unpack .../libarchive-extract-perl_0.72-1_all.deb ...
Unpacking libarchive-extract-perl (0.72-1) ...
Selecting previously unselected package libcgi-pm-perl.
Preparing to unpack .../libcgi-pm-perl_4.09-1_all.deb ...
Unpacking libcgi-pm-perl (4.09-1) ...
Selecting previously unselected package libfcgi-perl.
Preparing to unpack .../libfcgi-perl_0.77-1+deb8u1_amd64.deb ...
Unpacking libfcgi-perl (0.77-1+deb8u1) ...
Selecting previously unselected package libcgi-fast-perl.
Preparing to unpack .../libcgi-fast-perl_1%3a2.04-1_all.deb ...
Unpacking libcgi-fast-perl (1:2.04-1) ...
Selecting previously unselected package libclass-c3-perl.
Preparing to unpack .../libclass-c3-perl_0.26-1_all.deb ...
Unpacking libclass-c3-perl (0.26-1) ...
Selecting previously unselected package libclass-c3-xs-perl.
Preparing to unpack .../libclass-c3-xs-perl_0.13-2+b1_amd64.deb ...
Unpacking libclass-c3-xs-perl (0.13-2+b1) ...
Selecting previously unselected package libcpan-meta-perl.
Preparing to unpack .../libcpan-meta-perl_2.142690-1_all.deb ...
Unpacking libcpan-meta-perl (2.142690-1) ...
Selecting previously unselected package libparams-util-perl.
Preparing to unpack .../libparams-util-perl_1.07-2+b1_amd64.deb ...
Unpacking libparams-util-perl (1.07-2+b1) ...
Selecting previously unselected package libsub-install-perl.
Preparing to unpack .../libsub-install-perl_0.928-1_all.deb ...
Unpacking libsub-install-perl (0.928-1) ...
Selecting previously unselected package libdata-optlist-perl.
Preparing to unpack .../libdata-optlist-perl_0.109-1_all.deb ...
Unpacking libdata-optlist-perl (0.109-1) ...
Selecting previously unselected package libmro-compat-perl.
Preparing to unpack .../libmro-compat-perl_0.12-1_all.deb ...
Unpacking libmro-compat-perl (0.12-1) ...
Selecting previously unselected package libsub-exporter-perl.
Preparing to unpack .../libsub-exporter-perl_0.986-1_all.deb ...
Unpacking libsub-exporter-perl (0.986-1) ...
Selecting previously unselected package libdata-section-perl.
Preparing to unpack .../libdata-section-perl_0.200006-1_all.deb ...
Unpacking libdata-section-perl (0.200006-1) ...
Selecting previously unselected package liblog-message-perl.
Preparing to unpack .../liblog-message-perl_0.8-1_all.deb ...
Unpacking liblog-message-perl (0.8-1) ...
Selecting previously unselected package liblog-message-simple-perl.
Preparing to unpack .../liblog-message-simple-perl_0.10-2_all.deb ...
Unpacking liblog-message-simple-perl (0.10-2) ...
Selecting previously unselected package libmodule-build-perl.
Preparing to unpack .../libmodule-build-perl_0.421000-2+deb8u1_all.deb ...
Adding 'diversion of /usr/bin/config_data to /usr/bin/config_data.diverted by libmodule-build-perl'
Adding 'diversion of /usr/share/man/man1/config_data.1.gz to /usr/share/man/man1/config_data.diverted.1.gz by libmodule-build-perl'
Unpacking libmodule-build-perl (0.421000-2+deb8u1) ...
Selecting previously unselected package libmodule-pluggable-perl.
Preparing to unpack .../libmodule-pluggable-perl_5.1-1_all.deb ...
Unpacking libmodule-pluggable-perl (5.1-1) ...
Selecting previously unselected package libmodule-signature-perl.
Preparing to unpack .../libmodule-signature-perl_0.73-1+deb8u2_all.deb ...
Unpacking libmodule-signature-perl (0.73-1+deb8u2) ...
Selecting previously unselected package libpackage-constants-perl.
Preparing to unpack .../libpackage-constants-perl_0.04-1_all.deb ...
Unpacking libpackage-constants-perl (0.04-1) ...
Selecting previously unselected package libpod-latex-perl.
Preparing to unpack .../libpod-latex-perl_0.61-1_all.deb ...
Adding 'diversion of /usr/bin/pod2latex to /usr/bin/pod2latex.bundled by libpod-latex-perl'
Adding 'diversion of /usr/share/man/man1/pod2latex.1.gz to /usr/share/man/man1/pod2latex.bundled.1.gz by libpod-latex-perl'
Unpacking libpod-latex-perl (0.61-1) ...
Selecting previously unselected package libregexp-common-perl.
Preparing to unpack .../libregexp-common-perl_2013031301-1_all.deb ...
Unpacking libregexp-common-perl (2013031301-1) ...
Selecting previously unselected package libpod-readme-perl.
Preparing to unpack .../libpod-readme-perl_0.11-1_all.deb ...
Unpacking libpod-readme-perl (0.11-1) ...
Selecting previously unselected package libtext-template-perl.
Preparing to unpack .../libtext-template-perl_1.46-1_all.deb ...
Unpacking libtext-template-perl (1.46-1) ...
Selecting previously unselected package libsoftware-license-perl.
Preparing to unpack .../libsoftware-license-perl_0.103010-3_all.deb ...
Unpacking libsoftware-license-perl (0.103010-3) ...
Selecting previously unselected package libterm-ui-perl.
Preparing to unpack .../libterm-ui-perl_0.42-1_all.deb ...
Unpacking libterm-ui-perl (0.42-1) ...
Selecting previously unselected package libtext-soundex-perl.
Preparing to unpack .../libtext-soundex-perl_3.4-1+b2_amd64.deb ...
Unpacking libtext-soundex-perl (3.4-1+b2) ...
Selecting previously unselected package nginx-common.
Preparing to unpack .../nginx-common_1.6.2-5+deb8u4_all.deb ...
Unpacking nginx-common (1.6.2-5+deb8u4) ...
Selecting previously unselected package nginx-full.
Preparing to unpack .../nginx-full_1.6.2-5+deb8u4_amd64.deb ...
Unpacking nginx-full (1.6.2-5+deb8u4) ...
Selecting previously unselected package nginx.
Preparing to unpack .../nginx_1.6.2-5+deb8u4_all.deb ...
Unpacking nginx (1.6.2-5+deb8u4) ...
Selecting previously unselected package rename.
Preparing to unpack .../archives/rename_0.20-3_all.deb ...
Unpacking rename (0.20-3) ...
Selecting previously unselected package xml-core.
Preparing to unpack .../xml-core_0.13+nmu2_all.deb ...
Unpacking xml-core (0.13+nmu2) ...
Processing triggers for systemd (215-17+deb8u6) ...
Setting up libgdbm3:amd64 (1.8.3-13.1) ...
Setting up libssl1.0.0:amd64 (1.0.1t-1+deb8u6) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
Setting up libxml2:amd64 (2.9.1+dfsg1-5+deb8u4) ...
Setting up perl-modules (5.20.2-3+deb8u6) ...
Setting up perl (5.20.2-3+deb8u6) ...
update-alternatives: using /usr/bin/prename to provide /usr/bin/rename (rename) in auto mode
update-alternatives: warning: skip creation of /usr/share/man/man1/rename.1.gz because associated file /usr/share/man/man1/prename.1.gz (of link group rename) doesn't exist
Setting up libexpat1:amd64 (2.1.0-6+deb8u3) ...
Setting up libpng12-0:amd64 (1.2.50-2+deb8u3) ...
Setting up libfreetype6:amd64 (2.5.2-3+deb8u1) ...
Setting up ucf (3.0030) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
Setting up fonts-dejavu-core (2.34-1) ...
Setting up fontconfig-config (2.11.0-6.3+deb8u1) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
Setting up libfontconfig1:amd64 (2.11.0-6.3+deb8u1) ...
Setting up libjpeg62-turbo:amd64 (1:1.3.1-12) ...
Setting up libjbig0:amd64 (2.1-3.1) ...
Setting up libtiff5:amd64 (4.0.3-12.3+deb8u2) ...
Setting up libvpx1:amd64 (1.3.0-3) ...
Setting up libxau6:amd64 (1:1.0.8-1) ...
Setting up libxdmcp6:amd64 (1:1.1.1-1+b1) ...
Setting up libxcb1:amd64 (1.10-3+b1) ...
Setting up libx11-data (2:1.6.2-3) ...
Setting up libx11-6:amd64 (2:1.6.2-3) ...
Setting up libxpm4:amd64 (1:3.5.12-0+deb8u1) ...
Setting up libgd3:amd64 (2.1.0-5+deb8u9) ...
Setting up libgeoip1:amd64 (1.6.2-4) ...
Setting up libxslt1.1:amd64 (1.1.28-2+deb8u2) ...
Setting up sgml-base (1.26+nmu4) ...
Setting up init-system-helpers (1.22) ...
Setting up geoip-database (20150317-1) ...
Setting up libalgorithm-c3-perl (0.09-1) ...
Setting up libarchive-extract-perl (0.72-1) ...
Setting up libcgi-pm-perl (4.09-1) ...
Setting up libfcgi-perl (0.77-1+deb8u1) ...
Setting up libcgi-fast-perl (1:2.04-1) ...
Setting up libclass-c3-perl (0.26-1) ...
Setting up libclass-c3-xs-perl (0.13-2+b1) ...
Setting up libcpan-meta-perl (2.142690-1) ...
Setting up libparams-util-perl (1.07-2+b1) ...
Setting up libsub-install-perl (0.928-1) ...
Setting up libdata-optlist-perl (0.109-1) ...
Setting up libmro-compat-perl (0.12-1) ...
Setting up libsub-exporter-perl (0.986-1) ...
Setting up libdata-section-perl (0.200006-1) ...
Setting up liblog-message-perl (0.8-1) ...
Setting up liblog-message-simple-perl (0.10-2) ...
Setting up libmodule-build-perl (0.421000-2+deb8u1) ...
Setting up libmodule-pluggable-perl (5.1-1) ...
Setting up libmodule-signature-perl (0.73-1+deb8u2) ...
Setting up libpackage-constants-perl (0.04-1) ...
Setting up libpod-latex-perl (0.61-1) ...
Setting up libregexp-common-perl (2013031301-1) ...
Setting up libpod-readme-perl (0.11-1) ...
Setting up libtext-template-perl (1.46-1) ...
Setting up libsoftware-license-perl (0.103010-3) ...
Setting up libterm-ui-perl (0.42-1) ...
Setting up libtext-soundex-perl (3.4-1+b2) ...
Setting up nginx-common (1.6.2-5+deb8u4) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
Setting up nginx-full (1.6.2-5+deb8u4) ...
invoke-rc.d: policy-rc.d denied execution of start.
Setting up nginx (1.6.2-5+deb8u4) ...
Setting up rename (0.20-3) ...
update-alternatives: using /usr/bin/file-rename to provide /usr/bin/rename (rename) in auto mode
update-alternatives: warning: skip creation of /usr/share/man/man1/rename.1.gz because associated file /usr/share/man/man1/file-rename.1p.gz (of link group rename) doesn't exist
Setting up xml-core (0.13+nmu2) ...
Processing triggers for libc-bin (2.19-18+deb8u7) ...
Processing triggers for systemd (215-17+deb8u6) ...
Processing triggers for sgml-base (1.26+nmu4) ...
 ---> 97e2cc27be3e
Removing intermediate container b434a38c3e69
Step 5/7 : ONBUILD copy index.html /usr/share/nginx/html
 ---> Running in f9d9947486a9
 ---> 976b62540c84
Removing intermediate container f9d9947486a9
Step 6/7 : EXPOSE 80
 ---> Running in 20b7489830a7
 ---> ffe38dd9af88
Removing intermediate container 20b7489830a7
Step 7/7 : ENTRYPOINT /usr/bin/nginx
 ---> Running in f6360528fb58
 ---> 7e3acbaa8141
Removing intermediate container f6360528fb58
Successfully built 7e3acbaa8141
➜  docker git:(master) ✗ 
```
## 3.容器调试
    知道了容器构建的过程，可以通过中间层的镜像id 进行分层调试
    ➜  docker git:(master) ✗ docker run -it 976b62540c84   #对应与  Step 5/7  nginx 已经成功安装                                  
    root@6ac42f801c8a:/# nginx 
    root@6ac42f801c8a:/# ps -ef | grep nginx
    root         6     1  0 13:39 ?        00:00:00 nginx: master process nginx
    www-data     7     6  0 13:39 ?        00:00:00 nginx: worker process
    www-data     8     6  0 13:39 ?        00:00:00 nginx: worker process
    www-data     9     6  0 13:39 ?        00:00:00 nginx: worker process
    www-data    10     6  0 13:39 ?        00:00:00 nginx: worker process
    root        12     1  0 13:39 ?        00:00:00 grep nginx
    root@6ac42f801c8a:/# 
    
## 4.构建缓存
    1.使用缓存
        只要镜像所在层没有发生改动，就会使用缓存
        
    2.禁用缓存
        a. --no-cache
        ➜  docker git:(master) ✗ docker build -t u1:v1.0 . -f dockerFile/01/Dockerfile --no-cache
        Sending build context to Docker daemon 346.1 kB
        Step 1/7 : FROM debian:jessie-slim
         ---> 7d86024f45a4
        Step 2/7 : MAINTAINER huoyinghui "huoyinghui@qpkpure.com"
         ---> Running in b8b1e2328aa1
         ---> e5de3748dd9f
        Removing intermediate container b8b1e2328aa1
        Step 3/7 : RUN apt-get update
         ---> Running in 58b65777eba1
        ^C
        ➜  docker git:(master) ✗ 
        b.ENV REFERESH_DATE 2017-04-01
        
## 5.构建过程查看
    docker history
```concept
➜  docker git:(master) ✗ docker history u1:v1.0
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
7e3acbaa8141        9 minutes ago       /bin/sh -c #(nop)  ENTRYPOINT ["/usr/bin/n...   0 B                 
ffe38dd9af88        9 minutes ago       /bin/sh -c #(nop)  EXPOSE 80/tcp                0 B                 
976b62540c84        9 minutes ago       /bin/sh -c #(nop)  ONBUILD COPY index.html...   0 B                 
97e2cc27be3e        9 minutes ago       /bin/sh -c apt-get install -y nginx             58.5 MB             
d3cf54443ea3        26 minutes ago      /bin/sh -c apt-get update                       9.87 MB             
e5979465026f        49 minutes ago      /bin/sh -c #(nop)  MAINTAINER huoyinghui "...   0 B                 
7d86024f45a4        7 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0 B                 
<missing>           7 weeks ago         /bin/sh -c #(nop) ADD file:0eebaa293cb06f6...   80 MB               
➜  docker git:(master) ✗ 
```

## docker 数据备份



## docker 跨主机访问
    1.使用open vswitch 实现跨主机容器连接
    2.weave 实现跨主机

##  fig 管理docker
    http://www.fig.sh/install.html
```concept
➜  log-collect git:(3-gzip) ✗ docker-compose --version
docker-compose version 1.11.2, build dfed245
➜  log-collect git:(3-gzip) ✗ docker-machine --version
docker-machine version 0.10.0, build 76ed2a6
➜  log-collect git:(3-gzip) ✗ sudo pip install -U fig
Password:
The directory '/Users/apple/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/apple/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting fig
  Downloading fig-1.0.1.tar.gz
Requirement already up-to-date: docopt<0.7,>=0.6.1 in /Library/Python/2.7/site-packages/docopt-0.6.2-py2.7.egg (from fig)
Collecting PyYAML<4,>=3.10 (from fig)
  Downloading PyYAML-3.12.tar.gz (253kB)
    100% |████████████████████████████████| 256kB 32kB/s 
Collecting requests<3,>=2.2.1 (from fig)
  Downloading requests-2.13.0-py2.py3-none-any.whl (584kB)
    100% |████████████████████████████████| 593kB 26kB/s 
Collecting texttable<0.9,>=0.8.1 (from fig)
  Downloading texttable-0.8.7.tar.gz
Collecting websocket-client<0.12,>=0.11.0 (from fig)
  Downloading websocket-client-0.11.0.tar.gz
Collecting docker-py<0.6,>=0.5.3 (from fig)
  Downloading docker-py-0.5.3.tar.gz
Collecting dockerpty<0.4,>=0.3.2 (from fig)
  Downloading dockerpty-0.3.4.tar.gz
Requirement already up-to-date: six<2,>=1.3.0 in /Library/Python/2.7/site-packages/six-1.10.0-py2.7.egg (from fig)
Installing collected packages: PyYAML, requests, texttable, websocket-client, docker-py, dockerpty, fig
  Running setup.py install for PyYAML ... done
  Running setup.py install for texttable ... done
  Running setup.py install for websocket-client ... done
  Running setup.py install for docker-py ... done
  Running setup.py install for dockerpty ... done
  Running setup.py install for fig ... done
Successfully installed PyYAML-3.12 docker-py-0.5.3 dockerpty-0.3.4 fig-1.0.1 requests-2.13.0 texttable-0.8.7 websocket-client-0.11.0
➜  log-collect git:(3-gzip) ✗ fig --version
fig 1.0.1
```


## 文件挂载
```
docker run --restart always -d --name abuse-robot -v /home/abuse-robot/conf:/app/conf   -v /home/abuse-robot/MailMange.py:/app/MailMange.py  registry.pureapk.com/apkpure/abuse-robot:latest
1.正确挂载
➜  imgfit git:(2-dockerfile) ✗ docker run -it -v `pwd`/config.json:/app/config.json lc:v0 bash
root@2d3f9c1fe2ea:/app# ls -kl
total 10092
-rw-r--r-- 1 root root      258 Jan 16 13:17 config.json
-rwxr-xr-x 1 root root 10322800 Mar 14 06:21 imgfit
drwxr-xr-x 2 root root     4096 Mar 14 07:03 upload
root@2d3f9c1fe2ea:/app# ./imgfit 
2.文件被错误挂载成目录
➜  imgfit git:(2-dockerfile) ✗ docker run -it -v config.json:/app/config.json lc:v0 bash 
drwxr-xr-x 2 root root     4096 Mar 14 07:04 config.json
-rwxr-xr-x 1 root root 10322800 Mar 14 06:21 imgfit
drwxr-xr-x 2 root root     4096 Mar 14 07:03 upload
root@85aaadb5bed7:/app# ^C
root@85aaadb5bed7:/app# 
```



## docker 中设定时区
    https://tommy.net.cn/2015/02/05/config-timezone-in-docker/
```
首先通过下面的命令进入对应的 container:
1# docker exec -ti container bash
然后在 container 里面执行如下的命令：
1# echo "Asia/Shanghai" > /etc/timezone
2# dpkg-reconfigure -f noninteractive tzdata
1RUN echo "Asia/Shanghai" > /etc/timezone
2RUN dpkg-reconfigure -f noninteractive tzdata
```
