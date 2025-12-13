%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg knmap
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	2.1
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	An NMAP frontend for TDE
Group:		Applications/Internet
URL:		http://sourceforge.net/projects/knmap/

License:	GPLv2+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/internet/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_INSTALL_PREFIX="%{tde_prefix}"
BuildOption:    -DSHARE_INSTALL_PREFIX="%{tde_datadir}"
BuildOption:    -DLIB_INSTALL_DIR="%{tde_libdir}"
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON -DBUILD_TRANSLATIONS=ON

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

# NMAP support
Requires:		nmap


%description
Knmap is a TDE-based interface to the 'nmap' facility.

The main Knmap window provides for the entry of nmap options and the
display of nmap-generated output.

This program is a complete re-write of one by the same name written by
Alexandre Sagala. The last version of that program was 0.9 which was
released on 2003-03-09 and targeted the KDE 2.2 and QT 2.3 environments.

Not to mention that it did not cater for the full set of 'nmap' options.
Or, perhaps, 'nmap' progressed whilst that version of Knmap languished.

http://www.kde-apps.org/content/show.php?content=31108


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"


%install -a
%find_lang %{tde_pkg}

# Move desktop icon to XDG directory
if [ -d "%{buildroot}%{tde_datadir}/applnk" ]; then
  %__mkdir_p %{buildroot}%{tde_tdeappdir}
  %__mv "%{buildroot}%{tde_datadir}/applnk/"*"/%{tde_pkg}.desktop" "%{buildroot}%{tde_tdeappdir}/%{tde_pkg}.desktop"
  %__rm -r "%{buildroot}%{tde_datadir}/applnk"
fi


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md ChangeLog
%{tde_bindir}/knmap
%{tde_tdeappdir}/knmap.desktop
%{tde_datadir}/apps/knmap/
%{tde_tdedocdir}/HTML/en/knmap/
%{tde_datadir}/icons/hicolor/*/apps/knmap.png
%{tde_datadir}/icons/hicolor/*/apps/knmapman.png
%{tde_datadir}/icons/hicolor/*/apps/localman.png
%{tde_datadir}/icons/hicolor/*/apps/manpage.png
%{tde_datadir}/icons/hicolor/*/apps/manstylesheet.png
%{tde_datadir}/icons/hicolor/*/apps/profilecopy.png
%{tde_datadir}/icons/hicolor/*/apps/profiledelete.png
%{tde_datadir}/icons/hicolor/*/apps/profileload.png
%{tde_datadir}/icons/hicolor/*/apps/profilerename.png
%{tde_datadir}/icons/hicolor/*/apps/profilesave.png
%{tde_datadir}/icons/hicolor/*/apps/profilesaveas.png
%{tde_datadir}/icons/hicolor/*/apps/scanclose.png
%{tde_datadir}/icons/hicolor/*/apps/scanduplicate.png
%{tde_datadir}/icons/hicolor/*/apps/scannew.png
%{tde_datadir}/icons/hicolor/*/apps/scanrename.png
%{tde_datadir}/icons/hicolor/*/apps/zoomcustom.png
%{tde_datadir}/icons/hicolor/*/apps/zoomin.png
%{tde_datadir}/icons/hicolor/*/apps/zoomout.png
%{tde_mandir}/man1/*.1*

