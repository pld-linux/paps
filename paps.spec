Summary:	Plain Text to PostScript converter
Summary(pl.UTF-8):	Konwerter czystego tekstu do PostScriptu
Name:		paps
Version:	0.6.8
Release:	1
License:	LGPL
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/paps/%{name}-%{version}.tar.gz
# Source0-md5:	e9508132bf27609bf2fded2bfd9cb3f1
Patch0:		%{name}-as-needed.patch
URL:		http://paps.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
paps is a PostScript converter from plain text file using Pango.

%description -l pl.UTF-8
paps jest konwerterem czystego tekstu do PostScriptu za pomocą Pango.

%package devel
Summary:	paps static library and header file
Summary(pl.UTF-8):	Biblioteka statyczna i plik nagłówkowy paps
Group:		Development/Libraries
# doesn't require base

%description devel
paps static library and header file.

%description devel -l pl.UTF-8
Biblioteka statyczna i plik nagłówkowy paps.

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/paps
%{_mandir}/man1/paps.1*

%files devel
%defattr(644,root,root,755)
%doc doxygen-doc/html
%{_includedir}/libpaps.h
%{_libdir}/libpaps.a
