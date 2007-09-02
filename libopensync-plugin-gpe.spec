Summary:	GPE Plugin for OpenSync
Summary(pl.UTF-8):	Wtyczka GPE do OpenSync
Name:		libopensync-plugin-gpe
Version:	0.22
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	791c8976b725c4c52e5dd38ddb38c769
URL:		http://www.opensync.org/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a plugin for OpenSync to sync with handhelds using GPE
<http://gpe.handhelds.org>.

%description -l pl.UTF-8
Ten pakiet zawiera wtyczkę do OpenSync służącą do synchronizacji
z PDA używającymi GPE <http://gpe.handhelds.org>.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/plugins/*.la
# no -devel yet
rm -f $RPM_BUILD_ROOT%{_includedir}/opensync-1.0/opensync/gpe_sync.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/opensync/plugins/gpe_sync.so
%{_datadir}/opensync/defaults/gpe-sync
