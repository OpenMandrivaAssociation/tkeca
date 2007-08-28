%define name 	tkeca
%define version 4.2.0
%define release %mkrel 1

Name: 		%{name}
Summary: 	Tk GUI for Ecasound multitrack audio editor and recorder
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/tkeca/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	tk tcl ecasound
BuildArch:	noarch

%description
Tk Ecasound is a frontend for Ecasound. It has the look of a multitrack
recorder. It supports Ladspa plugins, multiple devices inputs/outputs,
and multiple effects.

%prep
%setup -q
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_libdir/%name
cp tkeca.tcl $RPM_BUILD_ROOT/%_libdir/%name/
mkdir -p $RPM_BUILD_ROOT/%_bindir
echo '#!/bin/bash' > $RPM_BUILD_ROOT/%_bindir/%name
echo 'if [ -e ~/.ecasoundrc ]' >> $RPM_BUILD_ROOT/%_bindir/%name
echo 'then echo "~/.ecasoundrc found"' >> $RPM_BUILD_ROOT/%_bindir/%name
echo 'else echo "creating ~/.ecasoundrc"; cp /usr/share/ecasound/ecasoundrc ~/.ecasoundrc' >> $RPM_BUILD_ROOT/%_bindir/%name
echo 'fi' >> $RPM_BUILD_ROOT/%_bindir/%name
echo 'if [ -e ~/.ecasound/ecasoundrc ]' >> $RPM_BUILD_ROOT/%_bindir/%name
echo 'then echo "~/.ecasound/ecasoundrc found"' >> $RPM_BUILD_ROOT/%_bindir/%name
echo 'else echo "creating ~/.ecasound/ecasoundrc"; mkdir -p ~/.ecasound; cp /usr/share/ecasound/ecasoundrc ~/.ecasound' >> $RPM_BUILD_ROOT/%_bindir/%name
echo 'fi' >> $RPM_BUILD_ROOT/%_bindir/%name
echo '/usr/lib/tkeca/tkeca.tcl' >> $RPM_BUILD_ROOT/%_bindir/%name
chmod ugo+x $RPM_BUILD_ROOT/%_bindir/%name

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=TkEca
Comment=%{summary}
Exec=%{_bindir}/%{name} 
Icon=sound_section.png
Terminal=false
Type=Application
Categories=AudioVideo;Audio;AudioVideoEditing;X-MandrivaLinux-Multimedia-Sound;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README.tkeca license.txt *.html
%{_bindir}/%name
%{_datadir}/applications/*
%{_libdir}/%name
