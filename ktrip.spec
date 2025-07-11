%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
#define commit cc1ac2462e41873741c8b6f3fcafa29ae3ce6a30

Name:		ktrip
Version:	25.04.0
Release:	%{?git:0.%{git}.}1
Summary:	Public transport assistant for Plasma Mobile
%if 0%{?git}
Source0:	https://invent.kde.org/utilities/ktrip/-/archive/%{gitbranch}/ktrip-%{gitbranchd}.tar.bz2#/ktrip-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/ktrip-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6QQC2DesktopStyle)
BuildRequires:	cmake(KPublicTransport)
BuildRequires:	cmake(KF6KirigamiAddons)

%description
Public transport assistant for Plasma Mobile

%prep
%autosetup -p1 -n ktrip-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang ktrip --all-name

%files -f ktrip.lang
%{_bindir}/ktrip
%{_datadir}/applications/org.kde.ktrip.desktop
%{_datadir}/metainfo/org.kde.ktrip.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.ktrip.svg
