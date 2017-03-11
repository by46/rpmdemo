Name: camel
Version: 0.0.1
Release: 1%{?alphatag:.%{alphatag}}%{?dist}
Summary: Python program package demo
Group: Applications/Internet
License: MIT 2.0
URL: http://www.zabbix.com
Source0: camel-%{version}%{?alphatag:%{alphatag}}.tar.gz
Source1: gunicorn.service
Buildroot: %{_tmppath}/camel-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: MySQL-python
Requires: python-devel
Requires: python-gunicorn == 18.0
Requires: python-virtualenv
Requires: python-flask
%if 0%{?rhel} >= 7
Requires(post):		systemd
Requires(preun):	    systemd
Requires(preun):	     systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	    /sbin/chkconfig
Requires(preun):    /sbin/service
Requires(postun):	/sbin/service
%endif

%description
Zabbix is the ultimate enterprise-level software designed for
real-time monitoring of millions of metrics collected from tens of
thousands of servers, virtual machines and network devices.

%prep
%setup0 -q -n camel-%{version}%{?alphatag:%{alphatag}}

%install

rm -rf $RPM_BUILD_ROOT

# install necessary folder

install -p -d -m 0755 $RPM_BUILD_ROOT%{_localstatedir}/run/gunicorn

mkdir -p $RPM_BUILD_ROOT/opt/camel

cp -rvf config $RPM_BUILD_ROOT/opt/camel
cp -rvf app $RPM_BUILD_ROOT/opt/camel
install -m 0644 -p run.py $RPM_BUILD_ROOT/opt/camel
install -m 0644 -p gunicorn.py $RPM_BUILD_ROOT/opt/camel
install -m 0644 -p wsgi.py $RPM_BUILD_ROOT/opt/camel


# install startup scripts
%if 0%{?rhel} >= 7
install -Dm 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/gunicorn.service
%else
install -Dm 0755 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-agent
%endif

%post
%if 0%{?rhel} >= 7
%systemd_post gunicorn.service
%else
/sbin/chkconfig --add zabbix-agent || :
%endif
service gunicorn stop
service gunicorn start

%files
%defattr(0755,root,root,0755)
/opt/camel
%{_unitdir}/gunicorn.service
%dir %{_localstatedir}/run/gunicorn