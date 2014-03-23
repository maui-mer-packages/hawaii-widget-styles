# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       hawaii-widget-styles

# >> macros
# << macros

Summary:    QtQuick Controls styles
Version:    0.2.0.20140323.881d688
Release:    1
Group:      Applications/System
License:    LGPL 2.1
URL:        https://github.com/mauios/hawaii-widget-styles.git
Source0:    hawaii-widget-styles-%{version}.tar.xz
Source100:  hawaii-widget-styles.yaml
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  cmake

%description
Styles for QtQuick Controls applications.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
cd upstream
# << build pre

%cmake .  \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=/usr

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
cd upstream
# << install pre
%make_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/Controls/Styles/Aluminium/*
# >> files
# << files
