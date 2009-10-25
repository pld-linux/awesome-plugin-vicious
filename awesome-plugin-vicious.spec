%define	shortname	vicious
Summary:	Vicious is a modular widget library for the "awesome" window manager
Summary(hu.UTF-8):	Vicious egy moduláris widget könyvtár az "awesome" ablakkezelőhöz
Name:		awesome-plugin-%{shortname}
Version:	1.0.18
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://git.sysphere.org/vicious/snapshot/vicious-%{version}.tar.gz
# Source0-md5:	ab3f5af58c59a73700fbcc670c00ebdd
URL:		http://awesome.naquadah.org/wiki/Vicious
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vicious is a modular widget library for the "awesome" window manager,
derived from the "Wicked" widget library. Vicious widget types are a
framework for creating your own widgets.

%description -l hu.UTF-8
Vicious egy modulár widget könyvtár az "awesome" ablakkezelőhöz, a
Wicked widget könyvtár alapjain. Vicious egy keretrendszert is
biztosít saját widgetek létrehozásához.


%prep
%setup -q -n %{shortname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{shortname}
install *.lua $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{shortname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{_datadir}/awesome/lib/%{shortname}
