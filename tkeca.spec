Name: 		tkeca
Summary: 	Tk GUI for Ecasound multitrack audio editor and recorder
Version: 	4.4.3
Release: 	2
Source0:	http://sourceforge.net/projects/tkeca/files/%{name}-%{version}.tar.gz
URL:		http://tkeca.sourceforge.net/
License:	GPLv2+
Group:		Sound
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

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%doc README.tkeca *.html
%{_bindir}/%{name}
%{_datadir}/applications/*
%{tcl_sitelib}/%{name}



%changelog
* Fri Nov 27 2009 Jérôme Brenier <incubusss@mandriva.org> 4.4.0-1mdv2010.1
+ Revision: 470586
- new version 4.4.0

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 4.2.0-5mdv2010.0
+ Revision: 445486
- rebuild

* Fri Dec 05 2008 Adam Williamson <awilliamson@mandriva.org> 4.2.0-4mdv2009.1
+ Revision: 310827
- clean file list
- drop old MDV category from menu
- create the script with cat, not a bunch of sequential echos...
- move to new location per policy
- buildrequires tcl-devel (for macros)
- new license policy
- spec clean

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 4.2.0-3mdv2009.0
+ Revision: 269436
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun May 11 2008 Funda Wang <fwang@mandriva.org> 4.2.0-2mdv2009.0
+ Revision: 205535
- fix location of tkeca.tcl

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 4.2.0-1mdv2008.1
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill explicit icon extension
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Wed Aug 22 2007 Austin Acton <austin@mandriva.org> 4.2.0-1mdv2008.0
+ Revision: 68969
- XDG menu
- mkrel
- new version
- Import tkeca



* Sun Feb 6 2005 Austin Acton <austin@mandrake.org> 4.0.2-2mdk
- birthday
- fix summary

* Fri Jan 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.0.2-1mdk
- 4.0.2

* Tue Jan 27 2004 Austin Acton <austin@mandrake.org> 4.0.1-1mdk
- 4.0.1

* Tue Nov 18 2003 Austin Acton <austin@linux.ca> 3.0.0-1mdk
- 3.0.0

* Sun Jul 6 2003 Austin Acton <aacton@yorku.ca> 2.0.0-1mdk
- 2.0.0

* Thu Jun 4 2003 Austin Acton <aacton@yorku.ca> 1.8.0-1mdk
- 1.8.0

* Mon Jun 2 2003 Austin Acton <aacton@yorku.ca> 1.6.0-1mdk
- 1.6.0

* Sun May 25 2003 Austin Acton <aacton@yorku.ca> 1.4.0-1mdk
- 1.4.0

* Tue Jan 28 2003 Austin Acton <aacton@yorku.ca> 1.0.2-1mdk
- initial package

