Summary:	A network toolbox
Name:		netwox
Version:	5.39.0
Release:	2
License:	LGPL
Group:		Networking/Other
URL:		https://www.laurentconstantin.com/fr/netw/netwox/
Source0:	http://downloads.sourceforge.net/project/ntwox/netwox%20only/5.39/%{name}-%{version}-src.tgz
Source1:	http://downloads.sourceforge.net/project/ntwox/netwox%20only/5.39/%{name}-%{version}-doc_html.tgz
BuildRequires:	libpcap-devel >= 0.7.2
BuildRequires:	libnet-devel >= 1.1.3
BuildRequires:	netwib-devel = %{version}

%description
Netwox is a network tools for network administrator and hackers.

It contains about 100 functions

%prep

%setup -q -n %{name}-%{version}-src -a1 

find . -type f -exec chmod a+r {} \; 

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

cd src
%makeinstall_std

%files
%doc INSTALLUNIX.TXT INSTALLWINDOWS.TXT README.TXT
%doc doc/*.txt %{name}-%{version}-doc_html/*
%{_bindir}/netwox*
%{_mandir}/man1/netwox*.1*
