%define name	netwox
%define version	5.39.0
%define release	1

Summary:	A network toolbox
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Networking/Other
URL:		http://www.laurentconstantin.com/fr/netw/netwox/
Source0:	http://downloads.sourceforge.net/project/ntwox/netwox%20only/5.39/%{name}-%{version}-src.tgz
Source1:	http://downloads.sourceforge.net/project/ntwox/netwox%20only/5.39/%{name}-%{version}-doc_html.tgz
BuildRequires:	libpcap-devel >= 0.7.2
BuildRequires:	net-devel >= 1.1.3
BuildRequires:	netwib-devel = %{version}

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

cd src
%makeinstall_std

%files
%doc INSTALLUNIX.TXT INSTALLWINDOWS.TXT README.TXT
%doc doc/*.txt %{name}-%{version}-doc_html/*
%{_bindir}/netwox*
%{_mandir}/man1/netwox*.1*


%changelog
* Mon Jul 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 5.39.0-1
+ Revision: 808566
- version update 5.39

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 5.35.0-5mdv2010.0
+ Revision: 382737
- rebuilt against libnet 1.1.3

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 5.35.0-4mdv2009.1
+ Revision: 298322
- rebuilt against libpcap-1.0.0

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 5.35.0-3mdv2009.0
+ Revision: 241095
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jul 03 2007 Funda Wang <fwang@mandriva.org> 5.35.0-1mdv2008.0
+ Revision: 47458
- New version
- rebuild for new era
- Import netwox

