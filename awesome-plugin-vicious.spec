%define	shortname	vicious
Summary:	Vicious is a modular widget library for the "awesome" window manager
Summary(hu.UTF-8):	Vicious egy moduláris widget könyvtár az "awesome" ablakkezelőhöz
Name:		awesome-plugin-%{shortname}
Version:	2.0.0
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://git.sysphere.org/vicious/snapshot/vicious-%{version}.tar.gz
# Source0-md5:	eb7a67f13581b913220c2c50c004a12d
Patch0:		%{name}-graph.patch
URL:		http://awesome.naquadah.org/wiki/Vicious
Requires:	awesome >= 3.4
Obsoletes:	awesome-plugin-wicked
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vicious is a modular widget library for the "awesome" window manager,
derived from the "Wicked" widget library. Vicious widget types are a
framework for creating your own widgets.

%description -l hu.UTF-8
Vicious egy moduláris widget könyvtár az "awesome" ablakkezelőhöz, a
Wicked widget könyvtár alapjain. Vicious egy keretrendszert is
biztosít saját widgetek létrehozásához.

%prep
%setup -q -n %{shortname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{shortname}/widgets
install *.lua $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{shortname}
install widgets/*.lua $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{shortname}/widgets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{_datadir}/awesome/lib/%{shortname}
