Summary:	Plain Text to PostScript converter
Summary(pl):	Konwerter czystego tekstu do PostScriptu
Name:		paps
Version:	0.6.7
Release:	1
License:	LGPL
Group:		Applications/Publishing
URL:		http://paps.sourceforge.net/
Source0:	http://dl.sourceforge.net/paps/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define filterout_ld -Wl,--as-needed

%description
paps is a PostScript converter from plain text file using Pango.

%description -l pl
paps jest konwerterem czystego tekstu do PostScriptu za pomoc± Pango.

%prep
%setup -q

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
%doc AUTHORS COPYING.LIB README TODO doxygen-doc/html
%attr(755,root,root) %{_bindir}/paps
%{_mandir}/man1/paps.1*
%{_includedir}/libpaps.h
%{_libdir}/libpaps.a
