# Conditional build:
%bcond_with	tests	# perform "make test"
%bcond_with	MQ	# build MQ subpackage (require commercial software to use)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	SOAP
%define		pnam	Lite
%define		real_version	%(echo %{version} | sed 's/[a-zA-Z]//')
Summary:	SOAP::Lite - Client and server side SOAP implementation
Summary(pl.UTF-8):	SOAP::Lite - implementacja SOAP po stronie klienta i serwera
Name:		perl-SOAP-Lite
Version:	0.710.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MK/MKUTTER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	45d6679daac03fe4eb604a5b5f416fd5
Patch0:		%{name}-warnings.patch
Patch1:		%{name}-pod.patch
URL:		http://www.soaplite.com/
%if %{with tests}
# this list is probably incomplete
BuildRequires:	apache-mod_perl
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Crypt-SSLeay
BuildRequires:	perl-FCGI
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-MIME-Lite
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-Net-Jabber
BuildRequires:	perl-URI
BuildRequires:	perl-libnet
BuildRequires:	perl-libwww
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional
%define		_noautoreq	'perl(SOAP::Transport::HTTP)'

%description
SOAP::Lite is a collection of Perl modules which provides a simple and
lightweight interface to the Simple Object Access Protocol (SOAP) both
on client and server side.

%description -l pl.UTF-8
SOAP::Lite to zestaw modułów Perla udostępniających prosty i lekki
interfejs do protokołu SOAP (Simple Object Access Protocol) zarówno po
stronie klienta, jak i serwera.

%package HTTP
Summary:	HTTP transport support for SOAP::Lite
Summary(pl.UTF-8):	Obsługa transportu HTTP dla SOAP::Lite
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl-libwww

%description HTTP
HTTP transport support for SOAP::Lite (SOAP::Transport::HTTP).

%description HTTP -l pl.UTF-8
Obsługa transportu HTTP dla SOAP::Lite (SOAP::Transport::HTTP).

%package JABBER
Summary:	Net::Jabber support for SOAP::Lite
Summary(pl.UTF-8):	Obsługa Net::Jabber dla SOAP::Lite
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description JABBER
JABBER transport support for SOAP::Lite (SOAP::Transport::JABBER).

%description JABBER -l pl.UTF-8
Obsługa transportu JABBER dla SOAP::Lite (SOAP::Transport::JABBER).

%package MQ
Summary:	MQ transport support for SOAP::Lite (SOAP::Transport::MQ)
Summary(pl.UTF-8):	Obsługa transportu MQ dla SOAP::Lite (SOAP::Transport::MQ)
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description MQ
MQ transport support for SOAP::Lite (SOAP::Transport::MQ).

%description MQ -l pl.UTF-8
Obsługa transportu MQ dla SOAP::Lite (SOAP::Transport::MQ).

%package examples
Summary:	SOAP::Lite - examples
Summary(pl.UTF-8):	Przykłady użycia SOAP::Lite
Group:		Development/Languages/Perl

%description examples
Examples for SOAP::Lite.

%description examples -l pl.UTF-8
Przykłady użycia SOAP::Lite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{real_version}
%patch0 -p1
%patch1 -p1

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
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# don't package .pod
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/SOAP/*.pod

# don't package OldDocs
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/OldDocs::*
rm -rf $RPM_BUILD_ROOT%{perl_vendorlib}/OldDocs

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
%dir %{perl_vendorlib}/SOAP/Lite
%{perl_vendorlib}/SOAP/Lite/*.pm
%dir %{perl_vendorlib}/SOAP/Lite/Deserializer
%{perl_vendorlib}/SOAP/Lite/Deserializer/*.pm
%dir %{perl_vendorlib}/SOAP/Transport
%{perl_vendorlib}/SOAP/Transport/*.pm
%exclude %{perl_vendorlib}/SOAP/Transport/JABBER.pm
%exclude %{perl_vendorlib}/SOAP/Transport/MQ.pm
%exclude %{perl_vendorlib}/SOAP/Transport/HTTP.pm
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
%{_mandir}/man3/SOAP*
%if %{with MQ}
%exclude %{_mandir}/man3/*::MQ.*
%endif

%files HTTP
%defattr(644,root,root,755)
%{perl_vendorlib}/SOAP/Transport/HTTP.pm

%if %{with MQ}
%files MQ
%defattr(644,root,root,755)
%{perl_vendorlib}/SOAP/Transport/MQ.pm
%{_mandir}/man3/*::MQ.*
%endif

%files JABBER
%defattr(644,root,root,755)
%{perl_vendorlib}/SOAP/Transport/JABBER.pm

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
