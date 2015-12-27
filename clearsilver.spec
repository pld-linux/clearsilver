Summary:	ClearSilver HTML template system
Summary(pl.UTF-8):	ClearSilver - system szablonów HTML
Name:		clearsilver
Version:	0.10.5
Release:	14
License:	Apache License style
Group:		Development/Libraries
Source0:	http://www.clearsilver.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	b8c0c7fbe0ef5e06e0c935f134304d44
Patch0:		%{name}-pic.patch
Patch1:		format-security.patch
Patch2:		variadic-macros.patch
URL:		http://www.clearsilver.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClearSilver is a fast, powerful, and language-neutral HTML template
system. In both static content sites and dynamic HTML applications, it
provides a separation between presentation code and application logic
which makes working with your project easier.

%description -l pl.UTF-8
ClearSilver to szybki, potężny i niezależny od języka system szablonów
HTML. Zarówno w statycznych stronach HTML jak i dynamicznych
aplikacjach pomaga oddzielić kod prezentacyjny od logiki aplikacji, co
ułatwia pracę nad projektem.

%package devel
Summary:	ClearSilver development package
Summary(pl.UTF-8):	Pakiet programistyczny ClearSilver
Group:		Development/Libraries

%description devel
This package provides needed files to develop extension to
ClearSilver.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki potrzebne do tworzenia rozszerzeń dla
ClearSilver.

%package -n python-clearsilver
Summary:	Neotonic ClearSilver Python Module
Summary(pl.UTF-8):	Moduł Pythona Neotonic ClearSilver
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n python-clearsilver
This package provides a Python interface to the ClearSilver CGI kit
and templating system.

%description -n python-clearsilver -l pl.UTF-8
Ten pakiet dostarcza interfejs Pythona do zestawu CGI i systemu
szablonów ClearSilver.

%package -n perl-ClearSilver
Summary:	Neotonic ClearSilver Perl Module
Summary(pl.UTF-8):	Moduł Perla Neotonic ClearSilver
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n perl-ClearSilver
This package provides a Perl interface to the ClearSilver templating
system.

%description -n perl-ClearSilver -l pl.UTF-8
Ten pakiet dostarcza interfejs Perla do systemu szablonów ClearSilver.

%package -n ruby-clearsilver
Summary:	Neotonic ClearSilver Ruby Module
Summary(pl.UTF-8):	Moduł Ruby'ego Neotonic ClearSilver
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n ruby-clearsilver
This package provides a ruby interface to the ClearSilver templating
system.

%description -n ruby-clearsilver -l pl.UTF-8
Ten pakiet dostarcza interfejs języka Ruby do systemu szablonów
ClearSilver.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

find . -type f -print0 | xargs -0 perl -pi -e "s!/usr/local/bin!/usr/bin!g" 

%build
install /usr/share/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure \
	--disable-csharp \
	--disable-java \
	--disable-ruby \
	--enable-apache \
	--enable-perl \
	--with-python=%{__python}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLDIRS=vendor

%{__make} install -C python \
	PYTHON_SITE=%{py_sitedir} \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C perl \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLDIRS=vendor

rm -rf $RPM_BUILD_ROOT%{perl_archlib} \
	$RPM_BUILD_ROOT%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

# what an ass putting it to lib32 dir
%if "%{_lib}" != "lib"
rm $RPM_BUILD_ROOT%{_prefix}/lib/python%{py_ver}/site-packages/neo_cgi.so
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CS_LICENSE INSTALL LICENSE README scripts/cs_lint.py contrib/cs-mode.el
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libneo_*.a
%{_includedir}/ClearSilver
%{_mandir}/man3/[!C]*.3*

%files -n python-clearsilver
%defattr(644,root,root,755)
%doc README.python
%attr(755,root,root) %{py_sitedir}/neo_cgi.so

%files -n perl-ClearSilver
%defattr(644,root,root,755)
%{perl_vendorarch}/ClearSilver.pm
%dir %{perl_vendorarch}/auto/ClearSilver
%attr(755,root,root) %{perl_vendorarch}/auto/ClearSilver/ClearSilver.so
%{_mandir}/man3/ClearSilver.3pm*

%if 0
%files -n ruby-clearsilver
%defattr(644,root,root,755)
%{ruby_sitepath}/%{ruby_version}/neo.rb
%attr(755,root,root) %{ruby_sitepath}/%{ruby_version}/%{ruby_arch}/hdf.so

%files -n apache-mod_ecs
%defattr(644,root,root,755)
%attr(755,root,root) %{apache_libexec}/mod_ecs.so
%endif
