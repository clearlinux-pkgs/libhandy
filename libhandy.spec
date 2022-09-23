#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libhandy
Version  : 1.8.0
Release  : 27
URL      : https://download.gnome.org/sources/libhandy/1.8/libhandy-1.8.0.tar.xz
Source0  : https://download.gnome.org/sources/libhandy/1.8/libhandy-1.8.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: libhandy-bin = %{version}-%{release}
Requires: libhandy-data = %{version}-%{release}
Requires: libhandy-lib = %{version}-%{release}
Requires: libhandy-license = %{version}-%{release}
Requires: libhandy-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : glib-dev
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pygobject

%description
# Handy
[![Pipeline status](https://gitlab.gnome.org/GNOME/libhandy/badges/main/build.svg)](https://gitlab.gnome.org/GNOME/libhandy/commits/main)
[![Code coverage](https://gitlab.gnome.org/GNOME/libhandy/badges/main/coverage.svg)](https://gitlab.gnome.org/GNOME/libhandy/commits/main)

%package bin
Summary: bin components for the libhandy package.
Group: Binaries
Requires: libhandy-data = %{version}-%{release}
Requires: libhandy-license = %{version}-%{release}

%description bin
bin components for the libhandy package.


%package data
Summary: data components for the libhandy package.
Group: Data

%description data
data components for the libhandy package.


%package dev
Summary: dev components for the libhandy package.
Group: Development
Requires: libhandy-lib = %{version}-%{release}
Requires: libhandy-bin = %{version}-%{release}
Requires: libhandy-data = %{version}-%{release}
Provides: libhandy-devel = %{version}-%{release}
Requires: libhandy = %{version}-%{release}

%description dev
dev components for the libhandy package.


%package lib
Summary: lib components for the libhandy package.
Group: Libraries
Requires: libhandy-data = %{version}-%{release}
Requires: libhandy-license = %{version}-%{release}

%description lib
lib components for the libhandy package.


%package license
Summary: license components for the libhandy package.
Group: Default

%description license
license components for the libhandy package.


%package locales
Summary: locales components for the libhandy package.
Group: Default

%description locales
locales components for the libhandy package.


%prep
%setup -q -n libhandy-1.8.0
cd %{_builddir}/libhandy-1.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663251254
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libhandy
cp %{_builddir}/libhandy-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libhandy/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libhandy

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/handy-1-demo

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Handy-1.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libhandy-1.deps
/usr/share/vala/vapi/libhandy-1.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libhandy-1/handy.h
/usr/include/libhandy-1/hdy-action-row.h
/usr/include/libhandy-1/hdy-animation.h
/usr/include/libhandy-1/hdy-application-window.h
/usr/include/libhandy-1/hdy-avatar.h
/usr/include/libhandy-1/hdy-carousel-indicator-dots.h
/usr/include/libhandy-1/hdy-carousel-indicator-lines.h
/usr/include/libhandy-1/hdy-carousel.h
/usr/include/libhandy-1/hdy-clamp.h
/usr/include/libhandy-1/hdy-combo-row.h
/usr/include/libhandy-1/hdy-deck.h
/usr/include/libhandy-1/hdy-enum-value-object.h
/usr/include/libhandy-1/hdy-enums.h
/usr/include/libhandy-1/hdy-expander-row.h
/usr/include/libhandy-1/hdy-flap.h
/usr/include/libhandy-1/hdy-header-bar.h
/usr/include/libhandy-1/hdy-header-group.h
/usr/include/libhandy-1/hdy-keypad.h
/usr/include/libhandy-1/hdy-leaflet.h
/usr/include/libhandy-1/hdy-main.h
/usr/include/libhandy-1/hdy-navigation-direction.h
/usr/include/libhandy-1/hdy-preferences-group.h
/usr/include/libhandy-1/hdy-preferences-page.h
/usr/include/libhandy-1/hdy-preferences-row.h
/usr/include/libhandy-1/hdy-preferences-window.h
/usr/include/libhandy-1/hdy-search-bar.h
/usr/include/libhandy-1/hdy-squeezer.h
/usr/include/libhandy-1/hdy-status-page.h
/usr/include/libhandy-1/hdy-style-manager.h
/usr/include/libhandy-1/hdy-swipe-group.h
/usr/include/libhandy-1/hdy-swipe-tracker.h
/usr/include/libhandy-1/hdy-swipeable.h
/usr/include/libhandy-1/hdy-tab-bar.h
/usr/include/libhandy-1/hdy-tab-view.h
/usr/include/libhandy-1/hdy-title-bar.h
/usr/include/libhandy-1/hdy-types.h
/usr/include/libhandy-1/hdy-value-object.h
/usr/include/libhandy-1/hdy-version.h
/usr/include/libhandy-1/hdy-view-switcher-bar.h
/usr/include/libhandy-1/hdy-view-switcher-title.h
/usr/include/libhandy-1/hdy-view-switcher.h
/usr/include/libhandy-1/hdy-window-handle.h
/usr/include/libhandy-1/hdy-window.h
/usr/lib64/libhandy-1.so
/usr/lib64/pkgconfig/libhandy-1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhandy-1.so.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libhandy/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files locales -f libhandy.lang
%defattr(-,root,root,-)

