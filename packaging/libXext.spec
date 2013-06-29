Name:           libXext
Version:        1.3.1
Release:        1
License:        MIT
Summary:        Common X Extensions library
Url:            http://www.x.org
Group:          Graphics/X Window System

Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXext.manifest

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%description
X.Org X11 libXext runtime library

%package devel
Summary:        Common X Extensions library - Development Files
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xorg-macros)

%description devel
X.Org X11 libXext development package

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure --disable-static
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libXext.so.6
%{_libdir}/libXext.so.6.4.0

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/MITMisc.h
%{_includedir}/X11/extensions/XEVI.h
%{_includedir}/X11/extensions/XLbx.h
%{_includedir}/X11/extensions/XShm.h
%{_includedir}/X11/extensions/Xag.h
%{_includedir}/X11/extensions/Xcup.h
%{_includedir}/X11/extensions/Xdbe.h
%{_includedir}/X11/extensions/Xext.h
%{_includedir}/X11/extensions/Xge.h
%{_includedir}/X11/extensions/dpms.h
%{_includedir}/X11/extensions/extutil.h
%{_includedir}/X11/extensions/multibuf.h
%{_includedir}/X11/extensions/security.h
%{_includedir}/X11/extensions/shape.h
%{_includedir}/X11/extensions/sync.h
%{_includedir}/X11/extensions/xtestext1.h
%{_libdir}/libXext.so
%{_libdir}/pkgconfig/xext.pc
