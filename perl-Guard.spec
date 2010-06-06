#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Guard
Summary:	Guard - safe cleanup blocks
Summary(pl.UTF-8):	Guard - bezpieczne czyszczenie bloków
Name:		perl-Guard
Version:	1.021
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pdir}-%{version}.tar.gz
# Source0-md5:	6c15e885c089115f8263a5873ed74f1e
URL:		http://search.cpan.org/dist/Guard/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements so-called "guards". A guard is something
(usually an object) that "guards" a resource, ensuring that it is
cleaned up when expected.

Specifically, this module supports two different types of guards:
guard objects, which execute a given code block when destroyed, and
scoped guards, which are tied to the scope exit.

%description -l pl.UTF-8
Moduł ten implementuje tzw "strażników". Strażnik jest czymś (zwykle
obiektem), co strzeże zasobu, zapewniając jego usunięcie wtedy kiedy
jest ono pożądane.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Guard.pm
%dir %{perl_vendorarch}/auto/Guard/
%{perl_vendorarch}/auto/Guard/Guard.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Guard/Guard.so
%{_mandir}/man3/*
