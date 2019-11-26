Summary:	Online dictionary
Summary(pl.UTF-8):	Słownik online
Name:		gnome-dictionary
Version:	3.26.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-dictionary/3.26/%{name}-%{version}.tar.xz
# Source0-md5:	08be36dd1c6d8d4e23a744737519d546
URL:		https://wiki.gnome.org/Apps/Dictionary
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.42.0
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc >= 1.15
BuildRequires:	meson >= 0.42.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.42.0
Requires:	libgdict = %{epoch}:%{version}-%{release}
Provides:	gnome-utils-dict
Provides:	gnome-utils-dictionary = %{epoch}:%{version}-%{release}
Obsoletes:	gnome-dict
Obsoletes:	gnome-utils-dict
Obsoletes:	gnome-utils-dictionary < 1:3.3.2-1
# system library dropped since 3.26; if something needs it, re-add as libgdict.spec built from gnome-dictionary 3.24.1
Obsoletes:	libgdict < 1:3.26
Obsoletes:	libgdict-apidocs < 1:3.26
Obsoletes:	libgdict-devel < 1:3.26
Obsoletes:	libgdict-static < 1:3.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows to look up an online dictionary for definitions and correct
spellings of words.

%description -l pl.UTF-8
Pozwala na wyszukiwanie definicji i poprawnej pisowni słów w słowniku
sieciowym.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-dictionary
%{_datadir}/appdata/org.gnome.Dictionary.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Dictionary.service
%dir %{_datadir}/gdict-1.0
%dir %{_datadir}/gdict-1.0/sources
%{_datadir}/gdict-1.0/sources/default.desktop
%{_datadir}/gdict-1.0/sources/spanish.desktop
%{_datadir}/gdict-1.0/sources/thai.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
%{_desktopdir}/org.gnome.Dictionary.desktop
%{_mandir}/man1/gnome-dictionary.1*
