Summary:	GNOME Chords - free GTK+/GNOME Guitar Chord program
Summary(pl.UTF-8):	GNOME Chords - wolnodostępny program do akordów gitarowych dla GTK+/GNOME
Name:		gnome-chords
Version:	0.0.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-chords/0.0/%{name}-%{version}.tar.xz
# Source0-md5:	fe4fa0abc37cae87f634578cc216550b
URL:		https://gitlab.gnome.org/ole/gnome-chords
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-bad-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Chords is a free GTK+/GNOME Guitar Chord program.

%description -l pl.UTF-8
GNOME Chords to wolnodostępny program do akordów gitarowych dla
GTK+/GNOME.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-chords
%{_datadir}/gnome-chords
