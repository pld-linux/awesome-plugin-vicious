%define	shortname	vicious
Summary:	Vicious is a modular widget library for the "awesome" window manager
Summary(hu.UTF-8):	Vicious egy moduláris widget könyvtár az "awesome" ablakkezelőhöz
Name:		awesome-plugin-%{shortname}
Version:	2.0.2
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://git.sysphere.org/vicious/snapshot/vicious-%{version}.tar.gz
# Source0-md5:	72416b8339d229dd1d1bfa00921416aa
Patch0:		%{name}-graph.patch
URL:		http://awesome.naquadah.org/wiki/Vicious
Requires:	awesome >= 3.4
Suggests:	alsa-utils
Suggests:	curl
Suggests:	hddtemp
Suggests:	wireless-tools
Obsoletes:	awesome-plugin-wicked
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vicious is a modular widget library for the "awesome" window manager,
derived from the "Wicked" widget library. Vicious widget types are a
framework for creating your own widgets.

Volume widget needs alsa-utils.
Gmail widget needs curl.
HDD Temperature widget needs hddtemp.
Wireless widget needs wireless-tools.

%description -l hu.UTF-8
Vicious egy moduláris widget könyvtár az "awesome" ablakkezelőhöz, a
Wicked widget könyvtár alapjain. Vicious egy keretrendszert is
biztosít saját widgetek létrehozásához.

Volume widgetnek kell alsa-utils.
Gmail widgetnek kell curl.
HDD Temperature widgetnek kell hddtemp.
Wireless widgetnek kell wireless-tools.

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
