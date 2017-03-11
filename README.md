# RPM demo


## create special user

为打包创建一个特殊的用户

```shell
useradd rpm
usermod -a -G root rpm
passwd rpm
#newegg@123
```

## build rpm
需要把该目录放在当前用户home目录，在`.rpmmacros`中配置了rpmbuild所需要的一些配置信息


使用rpm@scdfis01 进行编译
密码:newegg@123

```shell
cd ~

git clone http://trgit2/dfis/zabbix-agent-rpm.git rpmbuild

cd rpmbuild
rpmbuild -ba SPECS/camel.spec

```

## install

```shell
# rpm --force -ivh zabbix-agent-3.0.4-1.el7.centos.x86_64.rpm
sudo yum localinstall zabbix-agent-3.0.4-1.el7.centos.x86_64.rpm
```

## uninstall

```shell
rpm -e zabbix-agent-3.0.4-1.el7.centos.x86_64
```
## Service

disable selinux