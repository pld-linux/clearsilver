Summary:	ClearSilver HTML template system
Name:		clearsilver
Version:	0.9.13
Release:	0.1
License:	Apache License style
Group:		Development/Libraries
URL:		http://www.clearsilver.net/
Source0:	http://www.clearsilver.net/downloads/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	zlib-devel
BuildRequires:	python-devel
BuildRequires:	automake
BuildRequires:	autoconf

%description
ClearSilver is a fast, powerful, and language-neutral HTML template
system. In both static content sites and dynamic HTML applications, it
provides a separation between presentation code and application logic
which makes working with your project easier.

%package devel
Summary:	ClearSilver development package
Group:		Development/Libraries

%description devel
This package provides needed files to develop extension to
ClearSilver.

%package -n python-clearsilver
Summary:	Neotonic ClearSilver Python Module
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n python-clearsilver
This package provides a python interface to the clearsilver CGI kit
and templating system.

%package -n perl-ClearSilver
Summary:	Neotonic ClearSilver Perl Module
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n perl-ClearSilver
The clearsilver-perl package provides a perl interface to the
clearsilver templating system.

%package -n ruby-clearsilver
Summary:	Neotonic ClearSilver Ruby Module
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n ruby-clearsilver
The clearsilver-ruby package provides a ruby interface to the
clearsilver templating system.

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
	DESTDIR="$RPM_BUILD_ROOT" \
	INSTALLDIRS="vendor"

%{__make} install -C python \
	DESTDIR="$RPM_BUILD_ROOT"

%{__make} install -C perl \
	DESTDIR="$RPM_BUILD_ROOT" \
	INSTALLDIRS="vendor"

%{__rm} -rf $RPM_BUILD_ROOT%{perl_archlib} \
		$RPM_BUILD_ROOT%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CS_LICENSE INSTALL LICENSE README scripts/cs_lint.py contrib/cs-mode.el
%doc %{_mandir}/man3/*.3.*
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/ClearSilver/
%{_libdir}/libneo_*.a

%files -n python-clearsilver
%defattr(644,root,root,755)
%doc README.python
%{_libdir}/python*/site-packages/neo_cgi.so

%files -n perl-ClearSilver
%defattr(644,root,root,755)
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/ClearSilver.pm
%{perl_vendorarch}/auto/ClearSilver/

#%files -n ruby
#%defattr(-, root, root, 0755)
#{ruby_sitepath}/(ruby_version}/neo.rb
#{ruby_sitepath}/(ruby_version}/$(ruby_arch}/hdf.so

#%files -n mod_ecs
#{apache_libexec}/mod_ecs.so
