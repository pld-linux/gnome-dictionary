Summary:	Online dictionary
Summary(pl.UTF-8):	Słownik online
Name:		gnome-dictionary
Version:	3.9.0
Release:	1
Epoch:		1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-dictionary/3.9/%{name}-%{version}.tar.xz
# Source0-md5:	4a82e6d7f3d2bfd65056bae87ca9d5f6
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	yelp-tools
BuildRequires:	gtk+3-devel >= 3.0.3
BuildRequires:	gtk-doc >= 1.15
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	glib2 >= 1:2.28.0
Requires:	gtk+3 >= 3.0.3
Requires:	libgdict = %{epoch}:%{version}-%{release}
Provides:	gnome-utils-dict
Provides:	gnome-utils-dictionary = %{epoch}:%{version}-%{release}
Obsoletes:	gnome-dict
Obsoletes:	gnome-utils-dict
Obsoletes:	gnome-utils-dictionary < 1:3.3.2-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows to look up an online dictionary for definitions and correct
spellings of words.

%description -l pl.UTF-8
Pozwala na wyszukiwanie definicji i poprawnej pisowni słów w słowniku
sieciowym.

%package -n libgdict
Summary:	libgdict library
Summary(pl.UTF-8):	Biblioteka libgdict
License:	LGPL v2
Group:		X11/Libraries

%description -n libgdict
libgdict library.

%description -n libgdict -l pl.UTF-8
Biblioteka libgdict.

%package -n libgdict-devel
Summary:	Header files for libgdict library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgdict
License:	LGPL v2
Group:		X11/Development/Libraries
Requires:	gtk+3-devel >= 3.0.3
Requires:	libgdict = %{epoch}:%{version}-%{release}

%description -n libgdict-devel
This is the package containing the header files for libgdict library.

%description -n libgdict-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libgdict.

%package -n libgdict-static
Summary:	Static libgdict library
Summary(pl.UTF-8):	Statyczna biblioteka libgdict
License:	LGPL v2
Group:		X11/Development/Libraries
Requires:	libgdict-devel = %{epoch}:%{version}-%{release}

%description -n libgdict-static
Static libgdict library.

%description -n libgdict-static -l pl.UTF-8
Statyczna biblioteka libgdict.

%package -n libgdict-apidocs
Summary:	libgdict API documentation
Summary(pl.UTF-8):	Dokumentacja API libgdict
Group:		Documentation
Requires:	gtk-doc-common

%description -n libgdict-apidocs
libgdict API documentation.

%description -n libgdict-apidocs -l pl.UTF-8
Dokumentacja API libgdict.

%prep
%setup -q

%build
mkdir m4
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgdict-1.0.la

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%post -n libgdict -p /sbin/ldconfig
%postun -n libgdict -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-dictionary
%{_desktopdir}/gnome-dictionary.desktop
%{_datadir}/gnome-dictionary
%{_datadir}/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
%{_mandir}/man1/gnome-dictionary.1*

%files -n libgdict
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdict-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdict-1.0.so.6
%{_datadir}/gdict-1.0

%files -n libgdict-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdict-1.0.so
%{_includedir}/gdict-1.0
%{_pkgconfigdir}/gdict-1.0.pc

%files -n libgdict-static
%defattr(644,root,root,755)
%{_libdir}/libgdict-1.0.a

%files -n libgdict-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdict
