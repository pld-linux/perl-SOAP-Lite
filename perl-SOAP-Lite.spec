#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SOAP
%define	pnam	Lite
Summary:	SOAP::Lite - Client and server side SOAP implementation
Summary(pl):	SOAP::Lite - implementacja SOAP po stronie klienta i serwera
Name:		perl-SOAP-Lite
Version:	0.60a
%define		real_version	%(echo %{version} | sed 's/[a-zA-Z]//')
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aed9f8e9c4cf180d15c6e15aedc484d7
URL:		http://www.soaplite.com/
%if %{with tests}
# this list is probably incomplete
BuildRequires:	apache-mod_perl
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Crypt-SSLeay
BuildRequires:	perl-FCGI
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-libnet
BuildRequires:	perl-libwww
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-MIME-Lite
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-Net-Jabber
BuildRequires:	perl-URI
%endif
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SOAP::Lite is a collection of Perl modules which provides a simple and
lightweight interface to the Simple Object Access Protocol (SOAP) both
on client and server side.

%description -l pl
SOAP::Lite to zestaw modu³ów Perla udostêpniaj±cych prosty i lekki
interfejs do protoko³u SOAP (Simple Object Access Protocol) zarówno
po stronie klienta, jak i serwera.

%package JABBER
Summary:	Net::Jabber support for SOAP::Lite
Summary(pl):	Obs³uga Net::Jabber dla SOAP::Lite
Group:		Development/Languages/Perl

%description JABBER
JABBER transport support for SOAP::Lite (SOAP::Transport::JABBER).

%description JABBER -l pl
Obs³uga transportu JABBER dla SOAP::Lite (SOAP::Transport::JABBER).

%package MQ
Summary:	MQ transport support for SOAP::Lite (SOAP::Transport::MQ)
Summary(pl):	Obs³uga transportu MQ dla SOAP::Lite (SOAP::Transport::MQ)
Group:		Development/Languages/Perl

%description MQ
MQ transport support for SOAP::Lite (SOAP::Transport::MQ).

%description MQ -l pl
Obs³uga transportu MQ dla SOAP::Lite (SOAP::Transport::MQ).

%package examples
Summary:	SOAP::Lite - examples
Summary(pl):	Przyk³ady u¿ycia SOAP::Lite
Group:		Development/Languages/Perl

%description examples
Examples for SOAP::Lite.

%description examples -l pl
Przyk³ady u¿ycia SOAP::Lite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{real_version}
%{__chmod} u+rw . -R

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"SOAP::Lite")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -ar examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Apache/*.pm
%dir %{perl_vendorlib}/Apache/XMLRPC
%{perl_vendorlib}/Apache/XMLRPC/*.pm
%{perl_vendorlib}/IO/*.pm
%{perl_vendorlib}/SOAP/*.pm
%{perl_vendorlib}/SOAP/Transport/[FHILPT]*.pm
%{perl_vendorlib}/SOAP/Transport/MAILTO.pm
%dir %{perl_vendorlib}/UDDI
%{perl_vendorlib}/UDDI/*.pm
%{perl_vendorlib}/XML/Parser/*.pm
%dir %{perl_vendorlib}/XMLRPC
%{perl_vendorlib}/XMLRPC/*.pm
%dir %{perl_vendorlib}/XMLRPC/Transport
%{perl_vendorlib}/XMLRPC/Transport/*.pm
%{_mandir}/man3/Apache*
%{_mandir}/man3/UDDI*
%{_mandir}/man3/XML*
%{_mandir}/man3/SOAP::Lite*
%{_mandir}/man3/SOAP::Test*
%{_mandir}/man3/SOAP::Transport::[FHILPT]*
%{_mandir}/man3/SOAP::Transport::MAILTO*

%files MQ
%defattr(644,root,root,755)
%{perl_vendorlib}/SOAP/Transport/MQ.pm
%{_mandir}/man3/*::MQ.*

%files JABBER
%defattr(644,root,root,755)
%{perl_vendorlib}/SOAP/Transport/JABBER.pm
%{_mandir}/man3/*JABBER*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
