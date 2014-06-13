%define	_duplicate_files_terminate_build 0

%define debug_package %{nil}

Name:			sfml
Version:		1.6
Release:		11

%define	major		1
%define	minor		6

%define	libname_a	%mklibname sfml-audio %{major}.%{minor}
%define develname_a	%mklibname sfml-audio -d
%define	libname_g	%mklibname sfml-graphics %{major}.%{minor}
%define develname_g	%mklibname sfml-graphics -d
%define	libname_n	%mklibname sfml-network %{major}.%{minor}
%define develname_n	%mklibname sfml-network -d
%define	libname_s	%mklibname sfml-system %{major}.%{minor}
%define develname_s	%mklibname sfml-system -d
%define	libname_w	%mklibname sfml-window %{major}.%{minor}
%define develname_w	%mklibname sfml-window -d

%define	cname		c%{name}

%define	libname_ac	%mklibname csfml-audio %{major}.%{minor}
%define develname_ac	%mklibname csfml-audio -d
%define	libname_gc	%mklibname csfml-graphics %{major}.%{minor}
%define develname_gc	%mklibname csfml-graphics -d
%define	libname_nc	%mklibname csfml-network %{major}.%{minor}
%define develname_nc	%mklibname csfml-network -d
%define	libname_sc	%mklibname csfml-system %{major}.%{minor}
%define develname_sc	%mklibname csfml-system -d
%define	libname_wc	%mklibname csfml-window %{major}.%{minor}
%define develname_wc	%mklibname csfml-window -d

Summary:	Simple and Fast Multimedia Library
License:	zlib/libpng License
Group:		System/Libraries
URL:		http://sourceforge.net/projects/sfml
Source0:	http://sourceforge.net/projects/sfml/files/sfml/%{version}/SFML-%{version}-sdk-linux-32.tar.gz
Source1:	http://sourceforge.net/projects/sfml/files/sfml/%{version}/SFML-%{version}-c-sdk-linux-32.tar.gz
# real links:
# wget http://sourceforge.net/projects/sfml/files/sfml/%{version}/SFML-%{version}-sdk-linux-32.tar.gz/download
# wget http://sourceforge.net/projects/sfml/files/sfml/%{version}/SFML-%{version}-c-sdk-linux-32.tar.gz/download
Patch0:		samples-qt-Makefile-qt-inc-path.patch
Patch1:		sfml-c-makefile.patch
Patch2:		rem-included-libs.patch
Patch3:		SFML-1.6-png15.patch
Patch4:		SFML-1.6-gcc4.7.patch
Patch5:		SFML-1.6-dso.patch
Patch6:		SFML-1.6-png16.patch

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	recode
#for samples
BuildRequires:	qt4-devel
BuildRequires:	wxgtku-devel

%description
SFML is a portable and easy to use multimedia API written in C++.

Its features are :
 - portability,
 - object-oriented design,
 - flexibility (a lot of small packages),
 - easy to use,
 - easy to integrate with GUI toolkits.

The library is divided in 5 small packages :
 - audio
 - graphics
 - network
 - system
 - window

This package contains documentation and samples.

########################################################
# C++ libs

%package -n %{develname_a}
Summary:	Header files from %{name}-audio
Group:		Development/C++
Requires:	sfml-system-devel = %{version}
Requires:	%{libname_a} = %{version}
Provides:	%{name}-audio-devel = %{version}-%{release}
Conflicts:	%{develname_ac}

%description -n %{develname_a}
Includes files for developing programs based on %{name}-audio.

%package -n %{develname_g}
Summary:	Header files from %{name}-graphics
Group:		Development/C++
Requires:	sfml-window-devel = %{version}
Requires:	%{libname_g} = %{version}
Provides:	%{name}-graphics-devel = %{version}-%{release}
Conflicts:	%{develname_gc}

%description -n %{develname_g}
Includes files for developing programs based on %{name}-graphics.

%package -n %{develname_n}
Summary:	Header files from %{name}-network
Group:		Development/C++
Requires:	sfml-system-devel = %{version}
Requires:	%{libname_n} = %{version}
Provides:	%{name}-network-devel = %{version}-%{release}
Conflicts:	%{develname_nc}

%description -n %{develname_n}
Includes files for developing programs based on %{name}-network.

%package -n %{develname_s}
Summary:	Header files from %{name}-system
Group:		Development/C++
Requires:	%{libname_s} = %{version}
Provides:	%{name}-system-devel = %{version}-%{release}
Conflicts:	%{develname_sc}

%description -n %{develname_s}
Includes files for developing programs based on %{name}-system.

%package -n %{develname_w}
Summary:	Header files from %{name}-window
Group:		Development/C++
Requires:	sfml-system-devel = %{version}
Requires:	%{libname_w} = %{version}
Provides:	%{name}-window-devel = %{version}-%{release}
Conflicts:	%{develname_wc}

%description -n %{develname_w}
Includes files for developing programs based on %{name}-window.

%package -n %{libname_a}
Summary:	Dynamic libraries from %{name}-audio
Group:		System/Libraries
Provides:	%{name}-audio = %{version}-%{release}

%description -n %{libname_a}
Dynamic libraries from %{name}-audio.

%package -n %{libname_g}
Summary:	Dynamic libraries from %{name}-graphics
Group:		System/Libraries
Provides:	%{name}-graphics = %{version}-%{release}

%description -n %{libname_g}
Dynamic libraries from %{name}-graphics.

%package -n %{libname_n}
Summary:	Dynamic libraries from %{name}-network
Group:		System/Libraries
Provides:	%{name}-network = %{version}-%{release}

%description -n %{libname_n}
Dynamic libraries from %{name}-network.

%package -n %{libname_s}
Summary:	Dynamic libraries from %{name}-system
Group:		System/Libraries
Provides:	%{name}-system = %{version}-%{release}

%description -n %{libname_s}
Dynamic libraries from %{name}-system.

%package -n %{libname_w}
Summary:	Dynamic libraries from %{name}-window
Group:		System/Libraries
Provides:	%{name}-window = %{version}-%{release}

%description -n %{libname_w}
Dynamic libraries from %{name}-window.

########################################################
# C libs

%package -n %{develname_ac}
Summary:	Header files from %{cname}-audio
Group:		Development/C
Requires:	sfml-system-devel = %{version}
Requires:	%{libname_ac} = %{version}
Requires:	%{libname_a} = %{version}
Requires:	%{develname_a} = %{version}
Provides:	%{cname}-audio-devel = %{version}-%{release}

%description -n %{develname_ac}
Includes files for developing programs based on %{cname}-audio.

%package -n %{develname_gc}
Summary:	Header files from %{cname}-graphics
Group:		Development/C
Requires:	sfml-window-devel = %{version}
Requires:	%{libname_gc} = %{version}
Requires:	%{libname_g} = %{version}
Requires:	%{develname_g} = %{version}
Provides:	%{cname}-graphics-devel = %{version}-%{release}

%description -n %{develname_gc}
Includes files for developing programs based on %{cname}-graphics.

%package -n %{develname_nc}
Summary:	Header files from %{cname}-network
Group:		Development/C
Requires:	sfml-system-devel = %{version}
Requires:	%{libname_nc} = %{version}
Requires:	%{libname_n} = %{version}
Requires:	%{develname_n} = %{version}
Provides:	%{cname}-network-devel = %{version}-%{release}

%description -n %{develname_nc}
Includes files for developing programs based on %{cname}-network.

%package -n %{develname_sc}
Summary:	Header files from %{cname}-system
Group:		Development/C
Requires:	%{libname_sc} = %{version}
Requires:	%{libname_s} = %{version}
Requires:	%{develname_s} = %{version}
Provides:	%{cname}-system-devel = %{version}-%{release}

%description -n %{develname_sc}
Includes files for developing programs based on %{cname}-system.

%package -n %{develname_wc}
Summary:	Header files from %{cname}-window
Group:		Development/C
Requires:	sfml-system-devel = %{version}
Requires:	%{libname_wc} = %{version}
Requires:	%{libname_w} = %{version}
Requires:	%{develname_w} = %{version}
Provides:	%{cname}-window-devel = %{version}-%{release}

%description -n %{develname_wc}
Includes files for developing programs based on %{cname}-window.

%package -n %{libname_ac}
Summary:	Dynamic libraries from %{cname}-audio
Group:		System/Libraries
Requires:	%{libname_a} = %{version}
Provides:	%{cname}-audio = %{version}-%{release}

%description -n %{libname_ac}
Dynamic libraries from %{cname}-audio.

%package -n %{libname_gc}
Summary:	Dynamic libraries from %{cname}-graphics
Group:		System/Libraries
Requires:	%{libname_g} = %{version}
Provides:	%{cname}-graphics = %{version}-%{release}

%description -n %{libname_gc}
Dynamic libraries from %{cname}-graphics.

%package -n %{libname_nc}
Summary:	Dynamic libraries from %{cname}-network
Group:		System/Libraries
Requires:	%{libname_n} = %{version}
Provides:	%{cname}-network = %{version}-%{release}

%description -n %{libname_nc}
Dynamic libraries from %{cname}-network.

%package -n %{libname_sc}
Summary:	Dynamic libraries from %{cname}-system
Group:		System/Libraries
Requires:	%{libname_s} = %{version}
Provides:	%{cname}-system = %{version}-%{release}

%description -n %{libname_sc}
Dynamic libraries from %{cname}-system.

%package -n %{libname_wc}
Summary:	Dynamic libraries from %{cname}-window
Group:		System/Libraries
Requires:	%{libname_w} = %{version}
Provides:	%{cname}-window = %{version}-%{release}

%description -n %{libname_wc}
Dynamic libraries from %{cname}-window.

########################################################

%prep
%setup -q -b1 -n SFML-%{version}
rm -f lib/*.so*
# removing included libs
rm -rf src/SFML/Graphics/libjpeg/
rm -rf src/SFML/Graphics/libpng/
rm -rf src/SFML/Graphics/zlib/
%patch0 -p0 -b .qtincpath
%patch1 -p0 -b .csfml
%patch2 -p1 -b .inclibs
%patch3 -p1 -b .png15
%patch4 -p1 -b .gcc46
%patch5 -p1 -b .dso
%patch6 -p1 -b .png16~
%ifarch x86_64
perl -pi -e "s|DESTDIR\)/lib|DESTDIR\)/lib64|" src/SFML/Makefile
%endif
perl -pi -e "s|\r\n|\n|g" *.txt
recode l1..u8 *.txt

%ifarch x86_64
perl -pi -e "s|DESTDIR\)/lib|DESTDIR\)/lib64|" CSFML/src/SFML/Makefile
%endif

# fix samples build
perl -pi -e "s|export LDFLAGS  =|export LDFLAGS  = -L%{_libdir} -L../../lib|" \
 samples/Makefile
perl -pi -e "s|-I/usr/include/qt4|-I/usr/lib/qt4/include|" \
 samples/qt/Makefile

# fix samples data location
find samples -name "*.cpp" -exec perl -pi -e \
 "s|datas|%{_datadir}/%{name}/samples/bin/datas|g" {} +

%build
%make
#samples
pushd lib
for i in *.so* ; do ln -s $i ${i%.1.6} ; done
popd
pushd samples
%make
popd
pushd CSFML
%make
popd

%install
%makeinstall_std DESTDIR=%{buildroot}%{_prefix}

pushd CSFML
%makeinstall_std DESTDIR=%{buildroot}%{_prefix}
popd

# install sample source and data
rm -f %{buildroot}%{_datadir}/%{name}/samples/*/*.o
install -d -m 755 %{buildroot}%{_datadir}/%{name}/samples
cp -R ./samples/* %{buildroot}%{_datadir}/%{name}/samples/
rm -f %{buildroot}%{_datadir}/%{name}/samples/*/*.o

# install sample binaries to sfml-sample*
install -d -m 755 %{buildroot}%{_bindir}
for i in %{buildroot}%{_datadir}/%{name}/samples/bin/[!d]* ; do \
 mv $i %{buildroot}%{_bindir}/sfml-sample-`basename $i` ; done

%files
%defattr(0644,root,root,0755)
%doc *.txt doc/*
%attr(0755,root,root) %{_bindir}/sfml-sample-*
%{_datadir}/%{name}/samples

##############################
# C++ libs

%files -n %{develname_a}
%defattr(0644,root,root,0755)
%{_includedir}/SFML/Audio.hpp
%{_includedir}/SFML/Audio
%{_libdir}/libsfml-audio.so

%files -n %{develname_g}
%defattr(0644,root,root,0755)
%{_includedir}/SFML/Graphics.hpp
%{_includedir}/SFML/Graphics
%{_libdir}/libsfml-graphics.so

%files -n %{develname_n}
%defattr(0644,root,root,0755)
%{_includedir}/SFML/Network.hpp
%{_includedir}/SFML/Network
%{_libdir}/libsfml-network.so

%files -n %{develname_s}
%defattr(0644,root,root,0755)
%dir %{_includedir}/SFML
%{_includedir}/SFML/Config.hpp
%{_includedir}/SFML/System.hpp
%{_includedir}/SFML/System
%{_libdir}/libsfml-system.so

%files -n %{develname_w}
%defattr(0644,root,root,0755)
%{_includedir}/SFML/Window.hpp
%{_includedir}/SFML/Window
%{_libdir}/libsfml-window.so

%files -n %{libname_a}
%defattr(0755,root,root,0755)
%{_libdir}/libsfml-audio.so.%{major}.%{minor}

%files -n %{libname_g}
%defattr(0755,root,root,0755)
%{_libdir}/libsfml-graphics.so.%{major}.%{minor}

%files -n %{libname_n}
%defattr(0755,root,root,0755)
%{_libdir}/libsfml-network.so.%{major}.%{minor}

%files -n %{libname_s}
%defattr(0755,root,root,0755)
%{_libdir}/libsfml-system.so.%{major}.%{minor}

%files -n %{libname_w}
%defattr(0755,root,root,0755)
%{_libdir}/libsfml-window.so.%{major}.%{minor}

##############################
# C libs

%files -n %{develname_ac}
%defattr(0644,root,root,0755)
%{_includedir}/SFML/Audio.h
%{_libdir}/libcsfml-audio.so

%files -n %{develname_gc}
%defattr(0644,root,root,0755)
%{_includedir}/SFML/Graphics.h
%{_libdir}/libcsfml-graphics.so

%files -n %{develname_nc}
%defattr(0644,root,root,0755)
%{_includedir}/SFML/Network.h
%{_libdir}/libcsfml-network.so

%files -n %{develname_sc}
%defattr(0644,root,root,0755)
%{_includedir}/SFML/Config.h
%{_includedir}/SFML/System.h
%{_libdir}/libcsfml-system.so

%files -n %{develname_wc}
%defattr(0644,root,root,0755)
%{_includedir}/SFML/Window.h
%{_libdir}/libcsfml-window.so

%files -n %{libname_ac}
%defattr(0755,root,root,0755)
%{_libdir}/libcsfml-audio.so.%{major}.%{minor}

%files -n %{libname_gc}
%defattr(0755,root,root,0755)
%{_libdir}/libcsfml-graphics.so.%{major}.%{minor}

%files -n %{libname_nc}
%defattr(0755,root,root,0755)
%{_libdir}/libcsfml-network.so.%{major}.%{minor}

%files -n %{libname_sc}
%defattr(0755,root,root,0755)
%{_libdir}/libcsfml-system.so.%{major}.%{minor}

%files -n %{libname_wc}
%defattr(0755,root,root,0755)
%{_libdir}/libcsfml-window.so.%{major}.%{minor}



%changelog
* Fri Jan 13 2012 Andrey Bondrov <abondrov@mandriva.org> 1.6-4
+ Revision: 760614
- Deal with duplicate files issue, drop .o files from packaged samples
- Fix build against png15, some other minor build fixes
- Rebuild against utf8 wxGTK2.8, minor spec cleanup

* Tue Aug 03 2010 Florent Monnier <blue_prawn@mandriva.org> 1.6-3mdv2011.0
+ Revision: 565181
- removed included libs that may cause segfaults
- increm mkrel
- providing the C libs too

* Sun Aug 01 2010 Florent Monnier <blue_prawn@mandriva.org> 1.6-1mdv2011.0
+ Revision: 564874
- only one source tarball
- updated to last version 1.6

* Fri Mar 05 2010 Shlomi Fish <shlomif@mandriva.org> 1.5-2mdv2010.1
+ Revision: 514783
- Fixed the requires - libsfml-network is needed (thanks to Zombie)

* Tue Sep 15 2009 Guillaume Bedot <littletux@mandriva.org> 1.5-1mdv2010.0
+ Revision: 443012
- First package of SFML for Mandriva
- create sfml

