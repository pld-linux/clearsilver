Summary:	ClearSilver HTML template system
Summary(pl):	ClearSilver - system szablonów HTML
Name:		clearsilver
Version:	0.9.13
Release:	0.1
License:	Apache License style
Group:		Development/Libraries
Source0:	http://www.clearsilver.net/downloads/%{name}-%{version}.tar.gz
URL:		http://www.clearsilver.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClearSilver is a fast, powerful, and language-neutral HTML template
system. In both static content sites and dynamic HTML applications, it
provides a separation between presentation code and application logic
which makes working with your project easier.

%description -l pl
ClearSilver to szybki, potê¿ny i niezale¿ny od jêzyka system szablonów
HTML. Zarówno w statycznych stronach HTML jak i dynamicznych
aplikacjach pomaga oddzieliæ kod prezentacyjny od logiki aplikacji,
co u³atwia pracê nad projektem.

%package devel
Summary:	ClearSilver development package
Summary(pl):	Pakiet programistyczny ClearSilver
Group:		Development/Libraries

%description devel
This package provides needed files to develop extension to
ClearSilver.

%description devel -l pl
Ten pakiet dostarcza pliki potrzebne do tworzenia rozszerzeñ dla
ClearSilver.

%package -n python-clearsilver
Summary:	Neotonic ClearSilver Python Module
Summary(pl):	Modu³ Pythona Neotonic ClearSilver
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n python-clearsilver
This package provides a Python interface to the ClearSilver CGI kit
and templating system.

%description -n python-clearsilver -l pl
Ten pakiet dostarcza interfejs Pythona do zestawu CGI i systemu
szablonów ClearSilver.

%package -n perl-ClearSilver
Summary:	Neotonic ClearSilver Perl Module
Summary(pl):	Modu³ Perla Neotonic ClearSilver
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n perl-ClearSilver
This package provides a Perl interface to the ClearSilver templating
system.

%description -n perl-ClearSilver -l pl
Ten pakiet dostarcza interfejs Perla do systemu szablonów ClearSilver.

%package -n ruby-clearsilver
Summary:	Neotonic ClearSilver Ruby Module
Summary(pl):	Modu³ Ruby'ego Neotonic ClearSilver
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n ruby-clearsilver
This package provides a ruby interface to the ClearSilver templating
system.

%description -n ruby-clearsilver -l pl
Ten pakiet dostarcza interfejs jêzyka Ruby do systemu szablonów
ClearSilver.

%prep
%setup -q

%build
install /usr/share/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure \
	--enable-apache \
	--enable-python=%{_bindir}/python \
	--enable-perl \
	--disable-csharp \
	--disable-ruby \
	--disable-java

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLDIRS=vendor

%{__make} install -C python \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C perl \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLDIRS=vendor

rm -rf $RPM_BUILD_ROOT%{perl_archlib} \
	$RPM_BUILD_ROOT%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CS_LICENSE INSTALL LICENSE README scripts/cs_lint.py contrib/cs-mode.el
%attr(755,root,root) %{_bindir}/*
# XXX
%{_mandir}/man3/*.3.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/ClearSilver
%{_libdir}/libneo_*.a

%files -n python-clearsilver
%defattr(644,root,root,755)
%doc README.python
%{_libdir}/python*/site-packages/neo_cgi.so

%files -n perl-ClearSilver
%defattr(644,root,root,755)
%{perl_vendorarch}/ClearSilver.pm
%{perl_vendorarch}/auto/ClearSilver
%{_mandir}/man3/*.3pm*

#%files -n ruby
#%defattr(644,root,root,755)
#{ruby_sitepath}/(ruby_version}/neo.rb
#%attr(755,root,root) {ruby_sitepath}/(ruby_version}/$(ruby_arch}/hdf.so

#%files -n mod_ecs
#%defattr(644,root,root,755)
#%attr(755,root,root) {apache_libexec}/mod_ecs.so
