# TODO:
# - %files section need to be... made :)
# (FHS violations to kill - many dirs under /usr)
#  /bin/xorp_profiler
#  /bin/xorp_rtrmgr
#  /bin/xorpsh
#  /usr/bgp/tools/xorpsh_print_peers
#  /usr/bgp/tools/xorpsh_print_routes
#  /usr/bgp/xorp_bgp
#  /usr/bin/call_xrl
#  /usr/cli/tools/send_cli_processor_xrl
#  /usr/etc/templates/bgp.cmds
#  /usr/etc/templates/bgp.tp
#  /usr/etc/templates/fea.cmds
#  /usr/etc/templates/fea.tp
#  /usr/etc/templates/fib2mrib.tp
#  /usr/etc/templates/host.cmds
#  /usr/etc/templates/igmp.cmds
#  /usr/etc/templates/igmp.tp
#  /usr/etc/templates/interfaces.tp
#  /usr/etc/templates/mfea.cmds
#  /usr/etc/templates/mfea4.tp
#  /usr/etc/templates/mfea6.cmds
#  /usr/etc/templates/mfea6.tp
#  /usr/etc/templates/misc.cmds
#  /usr/etc/templates/mld.cmds
#  /usr/etc/templates/mld.tp
#  /usr/etc/templates/ospfv2.cmds
#  /usr/etc/templates/ospfv2.tp
#  /usr/etc/templates/pim.cmds
#  /usr/etc/templates/pim6.cmds
#  /usr/etc/templates/pimsm4.tp
#  /usr/etc/templates/pimsm6.tp
#  /usr/etc/templates/plumbing.tp
#  /usr/etc/templates/policy.tp
#  /usr/etc/templates/protocols.tp
#  /usr/etc/templates/rib.cmds
#  /usr/etc/templates/rib.tp
#  /usr/etc/templates/rip.cmds
#  /usr/etc/templates/rip.tp
#  /usr/etc/templates/ripng.tp
#  /usr/etc/templates/rtrmgr.tp
#  /usr/etc/templates/snmp.tp
#  /usr/etc/templates/static_routes.tp
#  /usr/etc/templates/xorpsh.cmds
#  /usr/fea/tools/show_interfaces
#  /usr/fea/xorp_fea
#  /usr/fea/xorp_fea_click_config_generator
#  /usr/fea/xorp_fea_dummy
#  /usr/fib2mrib/xorp_fib2mrib
#  /usr/libxipc/xorp_finder
#  /usr/mld6igmp/xorp_igmp
#  /usr/mld6igmp/xorp_mld
#  /usr/ospf/tools/print_lsas
#  /usr/ospf/tools/print_neighbours
#  /usr/ospf/xorp_ospfv2
#  /usr/ospf/xorp_ospfv3
#  /usr/pim/xorp_pimsm4
#  /usr/pim/xorp_pimsm6
#  /usr/policy/xorp_policy
#  /usr/rib/tools/show_routes
#  /usr/rib/xorp_rib
#  /usr/rip/tools/show_peer_stats
#  /usr/rip/tools/show_stats
#  /usr/rip/xorp_rip
#  /usr/rip/xorp_ripng
#  /usr/static_routes/xorp_static_routes
#  /usr/xrl/targets/bgp.xrls
#  /usr/xrl/targets/bgp4_mib.xrls
#  /usr/xrl/targets/cli.xrls
#  /usr/xrl/targets/coord.xrls
#  /usr/xrl/targets/demo_fea_ifmgr_client.xrls
#  /usr/xrl/targets/fea.xrls
#  /usr/xrl/targets/fea_ifmgr_mirror.xrls
#  /usr/xrl/targets/fib2mrib.xrls
#  /usr/xrl/targets/finder.xrls
#  /usr/xrl/targets/finder_client.xrls
#  /usr/xrl/targets/mfea.xrls
#  /usr/xrl/targets/mld6igmp.xrls
#  /usr/xrl/targets/ospf.xrls
#  /usr/xrl/targets/ospfv2.xrls
#  /usr/xrl/targets/ospfv3.xrls
#  /usr/xrl/targets/packet_acl.xrls
#  /usr/xrl/targets/pim.xrls
#  /usr/xrl/targets/policy.xrls
#  /usr/xrl/targets/profiler.xrls
#  /usr/xrl/targets/rib.xrls
#  /usr/xrl/targets/ribclient.xrls
#  /usr/xrl/targets/rip.xrls
#  /usr/xrl/targets/ripng.xrls
#  /usr/xrl/targets/rtrmgr.xrls
#  /usr/xrl/targets/show_routes.xrls
#  /usr/xrl/targets/socket_server.xrls
#  /usr/xrl/targets/static_routes.xrls
#  /usr/xrl/targets/test.xrls
#  /usr/xrl/targets/test_fea_ifmgr_mirror.xrls
#  /usr/xrl/targets/test_finder_events.xrls
#  /usr/xrl/targets/test_peer.xrls
#  /usr/xrl/targets/test_socket4.xrls
#  /usr/xrl/targets/test_socket6.xrls
#  /usr/xrl/targets/test_xrls.xrls
#  /usr/xrl/targets/xorp_if_mib.xrls
#  /usr/xrl/targets/xorpsh.xrls
# 
# - separate packages: xorpsh, maybe some more
# 
%define		_rc	RC
Summary:	eXtensible Open Router Platform
Summary(pl.UTF-8):   eXtensible Open Router Platform - rozszerzalna otwarta platforma dla routera
Name:		xorp
Version:	1.2
Release:	0.%{_rc}.0.3
License:	BSD-like
Group:		Networking/Admin
Source0:	http://www.xorp.org/releases/%{version}-%{_rc}/%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	ee5cc37d88304d2716245bf0279e6b04
URL:		http://www.xorp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
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
%setup -q -n %{name}-%{version}-%{_rc}

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f %{_sysconfdir}/shells ]; then
	echo "/bin/xorpsh" > %{_sysconfdir}/shells
else
	if ! grep -q '^/bin/xorpsh$' %{_sysconfdir}/shells; then
		echo "/bin/xorpsh" >> %{_sysconfdir}/shells
	fi
fi

%preun
umask 022
if [ "$1" = "0" ]; then
	grep -v /bin/xorpsh /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%files
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog README CHROOT SECURITY mkchroot.sh
#%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rssh.conf
%attr(755,root,root) /bin/xorp_profiler
%attr(755,root,root) /bin/xorp_rtrmgr
%attr(755,root,root) /bin/xorpsh
#%attr(4755,root,root) %{_libdir}/rssh_chroot_helper
#%{_mandir}/man?/*
