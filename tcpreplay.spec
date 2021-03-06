Summary:	Replay captured network traffic
Name:		tcpreplay
Version:	4.3.4
Release:	1
License:	GPL v3
Group:		Applications/Networking
Source0:	https://github.com/appneta/tcpreplay/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	d11673863c88a1f4607a9a8761c8e6e8
Patch0:		x32.patch
URL:		http://tcpreplay.appneta.com/
BuildRequires:	libdnet-devel
BuildRequires:	libpcap-devel >= 0.8.0
BuildRequires:	tcpdump
Requires:	/usr/bin/tcpdump

%description
Tcpreplay is a tool to replay captured network traffic. Currently,
tcpreplay supports pcap (tcpdump) and snoop capture formats. Also
included, is tcpprep a tool to pre-process capture files to allow
increased performance under certain conditions as well as capinfo
which provides basic information about capture files.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I libopts/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{CHANGELOG,CREDIT,HACKING,INSTALL,LICENSE,TODO}
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*

%changelog
