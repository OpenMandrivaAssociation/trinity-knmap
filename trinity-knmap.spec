%bcond clang 1

# TDE variables
%define tde_pkg knmap
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	An NMAP frontend for TDE
Group:		Applications/Internet
URL:		http://sourceforge.net/projects/knmap/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/internet/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils
BuildRequires:	gettext


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
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}

# Move desktop icon to XDG directory
if [ -d "%{buildroot}%{tde_prefix}/share/applnk" ]; then
  %__mkdir_p %{buildroot}%{tde_prefix}/share/applications/tde
  %__mv "%{buildroot}%{tde_prefix}/share/applnk/"*"/%{tde_pkg}.desktop" "%{buildroot}%{tde_prefix}/share/applications/tde/%{tde_pkg}.desktop"
  %__rm -r "%{buildroot}%{tde_prefix}/share/applnk"
fi


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md ChangeLog
%{tde_prefix}/bin/knmap
%{tde_prefix}/share/applications/tde/knmap.desktop
%{tde_prefix}/share/apps/knmap/
%{tde_prefix}/share/doc/tde/HTML/en/knmap/
%{tde_prefix}/share/icons/hicolor/*/apps/knmap.png
%{tde_prefix}/share/icons/hicolor/*/apps/knmapman.png
%{tde_prefix}/share/icons/hicolor/*/apps/localman.png
%{tde_prefix}/share/icons/hicolor/*/apps/manpage.png
%{tde_prefix}/share/icons/hicolor/*/apps/manstylesheet.png
%{tde_prefix}/share/icons/hicolor/*/apps/profilecopy.png
%{tde_prefix}/share/icons/hicolor/*/apps/profiledelete.png
%{tde_prefix}/share/icons/hicolor/*/apps/profileload.png
%{tde_prefix}/share/icons/hicolor/*/apps/profilerename.png
%{tde_prefix}/share/icons/hicolor/*/apps/profilesave.png
%{tde_prefix}/share/icons/hicolor/*/apps/profilesaveas.png
%{tde_prefix}/share/icons/hicolor/*/apps/scanclose.png
%{tde_prefix}/share/icons/hicolor/*/apps/scanduplicate.png
%{tde_prefix}/share/icons/hicolor/*/apps/scannew.png
%{tde_prefix}/share/icons/hicolor/*/apps/scanrename.png
%{tde_prefix}/share/icons/hicolor/*/apps/zoomcustom.png
%{tde_prefix}/share/icons/hicolor/*/apps/zoomin.png
%{tde_prefix}/share/icons/hicolor/*/apps/zoomout.png
%{tde_prefix}/share/man/man1/*.1*

