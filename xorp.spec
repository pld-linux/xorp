# TODO:
# - fix putting config templates in datadir (should be /etc/xorp/templates) 
# - separate packages: xorpsh, maybe some more
# - if someone know how to run bgp tests without root priviledges 
#   (probably other too)
# 
# Conditional build:
%bcond_with	tests	# build without performing tests
#
Summary:	eXtensible Open Router Platform
Summary(pl.UTF-8):	eXtensible Open Router Platform - rozszerzalna otwarta platforma dla routera
Name:		xorp
Version:	1.4
Release:	0.1
License:	BSD-like
Group:		Networking/Admin
Source0:	http://www.xorp.org/releases/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2eeacffc96d9551fdbf6786fcd033e76
Patch0:		%{name}-curses.patch
Patch1:		%{name}-tests.patch
Patch2:		%{name}-configure.patch
URL:		http://www.xorp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	ncurses-devel
BuildRequires:	net-snmp-devel
%{?with_test:BuildRequires:	python}
BuildRequires:	python
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
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT datadir=%{_datadir}/xorp bindir=%{_bindir} sbindir=%{_sbindir} sysconfdir=/etc/xorp docdir=%{_docdir}/xorp-1.4

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f %{_sysconfdir}/shells ]; then
	echo "/usr/bin/xorpsh" > %{_sysconfdir}/shells
else
	if ! grep -q '^/usr/bin/xorpsh$' %{_sysconfdir}/shells; then
		echo "/usr/bin/xorpsh" >> %{_sysconfdir}/shells
	fi
fi

%preun
umask 022
if [ "$1" = "0" ]; then
	grep -v /usr/bin/xorpsh /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%files
%defattr(644,root,root,755)
%doc ERRATA README RELEASE_NOTES
#%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rssh.conf
%attr(755,root,root) %{_bindir}/print_lsas
%attr(755,root,root) %{_bindir}/print_neighbours
%attr(755,root,root) %{_bindir}/send_cli_processor_xrl
%attr(755,root,root) %{_bindir}/show_interfaces
%attr(755,root,root) %{_bindir}/show_peer_stats
%attr(755,root,root) %{_bindir}/show_routes
%attr(755,root,root) %{_bindir}/show_stats
%attr(755,root,root) %{_bindir}/xorp_profiler
%attr(755,root,root) %{_bindir}/xorp_rtrmgr
%attr(755,root,root) %{_bindir}/xorp_bgp
%attr(755,root,root) %{_bindir}/xorp_fea
%attr(755,root,root) %{_bindir}/xorp_fea_click_config_generator
%attr(755,root,root) %{_bindir}/xorp_fea_dummy
%attr(755,root,root) %{_bindir}/xorp_fib2mrib
%attr(755,root,root) %{_bindir}/xorp_finder
%attr(755,root,root) %{_bindir}/xorp_igmp
%attr(755,root,root) %{_bindir}/xorp_mld
%attr(755,root,root) %{_bindir}/xorp_ospfv2
%attr(755,root,root) %{_bindir}/xorp_ospfv3
%attr(755,root,root) %{_bindir}/xorp_pimsm4
%attr(755,root,root) %{_bindir}/xorp_pimsm6
%attr(755,root,root) %{_bindir}/xorp_policy
%attr(755,root,root) %{_bindir}/xorp_rib
%attr(755,root,root) %{_bindir}/xorp_rip
%attr(755,root,root) %{_bindir}/xorp_ripng
%attr(755,root,root) %{_bindir}/xorp_static_routes
%attr(755,root,root) %{_bindir}/xorpsh
%attr(755,root,root) %{_bindir}/xorpsh_print_peers
%attr(755,root,root) %{_bindir}/xorpsh_print_routes
%attr(755,root,root) %{_sbindir}/call_xrl
%{_datadir}/xorp
