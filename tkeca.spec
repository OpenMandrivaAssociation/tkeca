Name: 		tkeca
Summary: 	Tk GUI for Ecasound multitrack audio editor and recorder
Version: 	4.2.0
Release: 	%{mkrel 4}
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
URL:		http://tkeca.sourceforge.net/
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
# For macros
BuildRequires:	tcl-devel
Requires:	tk
Requires:	tcl
Requires:	ecasound
BuildArch:	noarch

%description
Tk Ecasound is a frontend for Ecasound. It has the look of a multitrack
recorder. It supports Ladspa plugins, multiple devices inputs/outputs,
and multiple effects.

%prep
%setup -q
										
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{tcl_sitelib}/%{name}
cp tkeca.tcl %{buildroot}/%{tcl_sitelib}/%{name}/

mkdir -p %{buildroot}/%{_bindir}
cat > %{buildroot}/%{_bindir}/%{name} << EOF
#!/bin/bash
if [ -e ~/.ecasoundrc ]
then echo "~/.ecasoundrc found"
else echo "creating ~/.ecasoundrc"; cp /usr/share/ecasound/ecasoundrc ~/.ecasoundrc
fi
if [ -e ~/.ecasound/ecasoundrc ]
then echo "~/.ecasound/ecasoundrc found"
else echo "creating ~/.ecasound/ecasoundrc"; mkdir -p ~/.ecasound; cp /usr/share/ecasound/ecasoundrc ~/.ecasound
fi
%{tcl_sitelib}/%{name}/tkeca.tcl
EOF
chmod ugo+x %{buildroot}/%{_bindir}/%{name}

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=TkEca
Comment=%{summary}
Exec=%{_bindir}/%{name} 
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Audio;AudioVideoEditing;
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README.tkeca *.html
%{_bindir}/%{name}
%{_datadir}/applications/*
%{tcl_sitelib}/%{name}

