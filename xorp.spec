# TODO:
# - separate packages: xorpsh, maybe some more
# 
# Conditional build:
%bcond_without	tests	# build without performing tests
#
Summary:	eXtensible Open Router Platform
Summary(pl.UTF-8):	eXtensible Open Router Platform - rozszerzalna otwarta platforma dla routera
Name:		xorp
Version:	1.8.3
Release:	1
License:	BSD-like
Group:		Networking/Admin
Source0:	https://github.com/downloads/greearb/xorp.ct/%{name}-%{version}-src.tar.gz
# Source0-md5:	5879bcf398a7040e893bfb0b33329511
Source1:	%{name}.init
Patch0:		%{name}-default_paths.patch
URL:		http://www.xorp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	ncurses-devel
BuildRequires:	net-snmp-devel
%{?with_test:BuildRequires:	python}
Requires(post,preun):	/sbin/chkconfig
Requires:	traceroute
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XORP currently provides a set of routing protocol implementations, an
extensible programming API, and configuration tools. The supported
protocols are BGP, RIP, PIM-SM, and IGMP/MLD. IPv4 and IPv6 are both
supported. The list of protocols and features will hopefully grow as
more people start contributing to the project.

At the present time, XORP does not implement its own forwarding
system. It is reliant on the forwarding of the underlying host
operating system. We would like to support forwarding in custom
hardware and software architectures in future. An example being the
Click modular router.

%description -l pl.UTF-8
XORP udostępnia zbiór implementacji protokołów routingu, rozszerzalne
API programistyczne oraz narzędzia konfiguracyjne. Obsługiwane
protokoły to BGP, RIP, PIM-SM i IGMP/MLD. Obsługiwane są zarówno IPv4
jak i IPv6. Lista protokołów i możliwości prawdopodobnie będzie się
powiększać w miarę przybywania osób rozwijających projekt.

Aktualnie XORP nie implementuje własnego systemu forwardowania. Polega
na forwardingu z systemu operacyjnego. Autorzy chcą w przyszłości
obsługiwać forwarding we własnych architekturach sprzętowych i
programowych. Przykładem może być modularny router Click.

%prep
%setup -q -n %{name}
%patch0 -p1

# in addition to patch0
%{__sed} -i "s#/lib/xorp#/%{_lib}/xorp#g" rtrmgr/util.cc

%build
%{__scons} DESTDIR=$RPM_BUILD_ROOT \
	prefix=/usr \
	libexecdir=%{_libdir} \
	libdir=%{_libdir} \
	sbindir=%{_sbindir} \
	sysconfdir=%{_sysconfdir} \
	localstatedir=%{_localstatedir} \

%if %{with tests}
%{__scons} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{xorp,rc.d/init.d,logrotate.d,sysconfig}
install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install -p package_files/xorp.conf $RPM_BUILD_ROOT/etc/xorp/ 
install -p package_files/xorp.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/xorp
install -p package_files/xorp.logrotate $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

%{__scons} install DESTDIR=$RPM_BUILD_ROOT \
	prefix=/usr \
	libexecdir=%{_libdir} \
	libdir=%{_libdir} \
	sbindir=%{_sbindir} \
	sysconfdir=%{_sysconfdir} \
	localstatedir=%{_localstatedir} \

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f %{_sysconfdir}/shells ]; then
	echo "/usr/sbin/xorpsh" > %{_sysconfdir}/shells
else
	if ! grep -q '^/usr/sbin/xorpsh$' %{_sysconfdir}/shells; then
		echo "/usr/sbin/xorpsh" >> %{_sysconfdir}/shells
	fi
fi
/sbin/chkconfig --add %{name}
if [ -f /var/lock/subsys/%{name} ]; then
	echo "Run \"/sbin/service %{name} restart\" to restart XORP." >&2
else
	echo "Run \"/sbin/service %{name} start\" to start XORP." >&2
fi

%preun
umask 022
if [ "$1" = "0" ]; then
	grep -v /usr/sbin/xorpsh /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
	%service %{name} stop
	/sbin/chkconfig --del %{name}
fi

%files
%defattr(644,root,root,755)
%doc ERRATA RELEASE_NOTES
%attr(755,root,root) /etc/rc.d/init.d/%{name}
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/%{name}
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%dir %{_sysconfdir}/%{name}
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/%{name}.conf
%{_sysconfdir}/%{name}/templates
%attr(755,root,root) %{_sbindir}/bgp_xrl_shell_funcs.sh
%attr(755,root,root) %{_sbindir}/call_xrl
%attr(755,root,root) %{_sbindir}/fea_xrl_shell_funcs.sh
%attr(755,root,root) %{_sbindir}/rib_xrl_shell_funcs.sh
%attr(755,root,root) %{_sbindir}/xorp_profiler
%attr(755,root,root) %{_sbindir}/xorp_rtrmgr
%attr(755,root,root) %{_sbindir}/xorpsh
%attr(755,root,root) %{_libdir}/%{name}
#%{_datadir}/xorp
