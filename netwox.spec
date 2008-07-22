%define name	netwox
%define version	5.35.0
%define release	%mkrel 3

Summary:	A network toolbox
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Networking/Other
URL:		http://www.laurentconstantin.com/fr/netw/netwox/
Source0:	http://www.laurentconstantin.com/common/netw/netwox/download/v5/%{name}-%{version}-src.tgz
Source1:	http://www.laurentconstantin.com/common/netw/netwox/download/v5/%{name}-%{version}-doc_html.tgz
BuildRequires:	libpcap-devel >= 0.7.2
BuildRequires:	net2-devel
BuildRequires:	netwib-devel = %{version}
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Netwox is a network tools for network administrator and hackers.

It contains about 100 functions

%prep

%setup -q -n %{name}-%{version}-src -a1 

perl -pi -e 's!^NETWIBDEF_INSTPREFIX=.*!NETWIBDEF_INSTPREFIX=/usr!' src/config.dat
perl -pi -e 's!^NETWOXDEF_INSTPREFIX=.*!NETWOXDEF_INSTPREFIX=/usr!' src/config.dat
# Hacking for lib64
perl -pi -e 's!^NETWIBDEF_INSTLIB=.*!NETWIBDEF_INSTLIB=%{_libdir}!' src/config.dat
perl -pi -e 's!^NETWIBDEF_SYSARCH=.*!NETWIBDEF_SYSARCH=%{_arch}!' src/config.dat
perl -pi -e 's!^NETWOXDEF_INSTMAN=.*!NETWOXDEF_INSTMAN=%{_mandir}!' src/config.dat

%build
cd src
./genemake
make GCCOPT="%{optflags} -D_BSD_SOURCE -D__BSD_SOURCE -D__FAVOR_BSD -DHAVE_NET_ETHERNET_H"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

cd src
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALLUNIX.TXT INSTALLWINDOWS.TXT README.TXT
%doc doc/*.txt %{name}-%{version}-doc_html/*
%{_bindir}/netwox*
%{_mandir}/man1/netwox*.1*
