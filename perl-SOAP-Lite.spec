#
# Conditional build:
# _with_tests - perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	SOAP
%define	pnam	Lite
Summary:	SOAP::Lite - Client and server side SOAP implementation
#Summary(pl):	
Name:		perl-SOAP-Lite
Version:	0.55
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.zip
URL:		http://www.soaplite.com/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_with_tests:1}%{!?_with_tests:0}
# this list is probably incomplete
BuildRequires:	perl-libwww
BuildRequires:	apache-mod_perl
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Crypt-SSLeay
BuildRequires:	perl-FCGI
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-libnet
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-MIME-Lite
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-Net-Jabber
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SOAP::Lite is a collection of Perl modules which provides a simple and
lightweight interface to the Simple Object Access Protocol (SOAP) both
on client and server side.

# %description -l pl
# TODO

%package examples
Summary:	SOAP::Lite - examples
Group:		Development/Languages/Perl

%description examples
Examples for SOAP::Lite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__chmod} u+rw . -R

%build
perl -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"SOAP::Lite")'
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -ar examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Apache/*.pm
%{perl_sitelib}/Apache/XMLRPC/*.pm
%{perl_sitelib}/IO/*.pm
%{perl_sitelib}/SOAP/*.pm
%{perl_sitelib}/SOAP/Transport/*.pm
%{perl_sitelib}/UDDI/*.pm
%{perl_sitelib}/XML/Parser/*.pm
%{perl_sitelib}/XMLRPC/*.pm
%{perl_sitelib}/XMLRPC/Transport/*.pm
%{_mandir}/man3/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
