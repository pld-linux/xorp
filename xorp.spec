%define		_rc	RC
Summary:	eXtensible Open Router Platform
Name:		xorp
Version:	1.2
Release:	0.%{_rc}.0.2
License:	BSD-like
Group:		Networking/Admin
Source0:	http://www.xorp.org/releases/1.2-RC/%{name}-%{version}-%{_rc}.tar.gz
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
#if [ ! -f %{_sysconfdir}/shells ]; then
# echo "%{_bindir}/%{name}" > %{_sysconfdir}/shells
# echo "%{_bindir}/scpsh" >> %{_sysconfdir}/shells
# echo "%{_bindir}/sftpsh" >> %{_sysconfdir}/shells
#else
# if ! grep -q '^%{_bindir}/%{name}$' %{_sysconfdir}/shells; then
# echo "%{_bindir}/%{name}" >> %{_sysconfdir}/shells
#	fi
# if ! grep -q '^%{_bindir}/scpsh$' %{_sysconfdir}/shells; then
# echo "%{_bindir}/scpsh" >> %{_sysconfdir}/shells
#	fi
# if ! grep -q '^%{_bindir}/sftpsh$' %{_sysconfdir}/shells; then
# echo "%{_bindir}/sftpsh" >> %{_sysconfdir}/shells
#	fi
#fi

%preun
umask 022
#if [ "$1" = "0" ]; then
#	grep -v %{_bindir}/%{name} /etc/shells | grep -v %{_bindir}/scpsh | grep -v %{_bindir}/sftpsh > /etc/shells.new
#	mv -f /etc/shells.new /etc/shells
#fi

%files
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog README CHROOT SECURITY mkchroot.sh
#%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rssh.conf
#%attr(755,root,root) %{_bindir}/%{name}
#%attr(755,root,root) %{_bindir}/scpsh
#%attr(755,root,root) %{_bindir}/sftpsh
#%attr(4755,root,root) %{_libdir}/rssh_chroot_helper
#%{_mandir}/man?/*
