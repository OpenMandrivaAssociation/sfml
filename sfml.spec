Name:			sfml
Version:		1.5
Release:		%mkrel 1

%define	major		1
%define	minor		5
%define	libname_a	%mklibname sfml-audio %major.%minor
%define develname_a	%mklibname sfml-audio -d
%define	libname_g	%mklibname sfml-graphics %major.%minor
%define develname_g	%mklibname sfml-graphics -d
%define	libname_n	%mklibname sfml-network %major.%minor
%define develname_n	%mklibname sfml-network -d
%define	libname_s	%mklibname sfml-system %major.%minor
%define develname_s	%mklibname sfml-system -d
%define	libname_w	%mklibname sfml-window %major.%minor
%define develname_w	%mklibname sfml-window -d

Summary:	Simple and Fast Multimedia Library
License:	zlib/libpng License
Group:		System/Libraries
URL:		http://sourceforge.net/projects/sfml
Source0:	http://sourceforge.net/projects/sfml/files/sfml/1.5/SFML-1.5-sdk-linux-32.tar.gz
Source1:	http://sourceforge.net/projects/sfml/files/sfml/1.5/SFML-1.5-sdk-linux-64.tar.gz

BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	freetype2-devel
BuildRequires:	libx11-devel
BuildRequires:	libxrandr-devel
BuildRequires:	openal-devel
BuildRequires:	sndfile-devel
#for samples
BuildRequires:	qt4-devel
BuildRequires:	wxGTK2.8-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%package -n %{develname_a}
Summary:	Header files from %{name}-audio
Group:		Development/C++
Requires:	sfml-system-devel = %{version}
Requires:	libsfml-audio = %{version}
Provides:	%{name}-audio-devel = %{version}-%{release}

%description -n %{develname_a}
Includes files for developing programs based on %{name}-audio.

%package -n %{develname_g}
Summary:	Header files from %{name}-graphics
Group:		Development/C++
Requires:	sfml-window-devel = %{version}
Requires:	libsfml-grahics = %{version}
Provides:	%{name}-graphics-devel = %{version}-%{release}

%description -n %{develname_g}
Includes files for developing programs based on %{name}-graphics.

%package -n %{develname_n}
Summary:	Header files from %{name}-network
Group:		Development/C++
Requires:	sfml-system-devel = %{version}
Requires:	libsfml-network = %{version}
Provides:	%{name}-network-devel = %{version}-%{release}

%description -n %{develname_n}
Includes files for developing programs based on %{name}-network.

%package -n %{develname_s}
Summary:	Header files from %{name}-system
Group:		Development/C++
Requires:	libsfml-system = %{version}
Provides:	%{name}-system-devel = %{version}-%{release}

%description -n %{develname_s}
Includes files for developing programs based on %{name}-system.

%package -n %{develname_w}
Summary:	Header files from %{name}-window
Group:		Development/C++
Requires:	sfml-system-devel = %{version}
Requires:	libsfml-window = %{version}
Provides:	%{name}-window-devel = %{version}-%{release}

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

%prep
%setup -q -a1 -n SFML-%{version}
perl -pi -e "s|DESTDIR\)/lib|DESTDIR\)/lib64|" SFML-%{version}/src/SFML/Makefile
perl -pi -e "s|\r\n|\n|g" *.txt
recode l1..u8 *.txt

# fix samples build
perl -pi -e "s|export LDFLAGS  =|export LDFLAGS  = -L%{_libdir} -L../../lib|" \
 samples/Makefile SFML-%{version}/samples/Makefile
perl -pi -e "s|-I/usr/include/qt4|-I%{_libdir}/qt4/include|" \
 samples/qt/Makefile SFML-%{version}/samples/qt/Makefile

# fix samples data location
find samples -name "*.cpp" -exec perl -pi -e \
 "s|datas|%{_datadir}/%{name}/samples/bin/datas|g" {} +
find SFML-%{version}/samples -name "*.cpp" -exec perl -pi -e \
 "s|datas|%{_datadir}/%{name}/samples/bin/datas|g" {} +

%build
%ifarch x86_64
cd SFML-%{version}
%endif
%make
#samples
pushd lib
for i in *.so* ; do ln -s $i ${i%.1.5} ; done
popd
pushd samples
%make 
popd
rm -f lib/*.so

%install
rm -rf %{buildroot}
%ifarch x86_64
cd SFML-%{version}
%endif
%makeinstall_std DESTDIR=%{buildroot}%{_prefix}

# install sample source and data
rm -f %{buildroot}%{_datadir}/%{name}/samples/*/*.o
install -d -m 755 %{buildroot}%{_datadir}/%{name}/samples
cp -R ./samples/* %{buildroot}%{_datadir}/%{name}/samples/

# install sample binaries to sfml-sample*
install -d -m 755 %{buildroot}%{_bindir}
for i in %{buildroot}%{_datadir}/%{name}/samples/bin/[!d]* ; do \
 mv $i %{buildroot}%{_bindir}/sfml-sample-`basename $i` ; done

# fix links
pushd %{buildroot}%{_libdir}
for i in *.so ; do rm -f $i ; ln -s $i.* $i ; done
popd

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc *.txt doc/*
%attr(0755,root,root) %{_bindir}/sfml-sample-*
%{_datadir}/%{name}/samples

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
%defattr(0644,root,root,0755)
%{_libdir}/libsfml-audio.so.1.5

%files -n %{libname_g}
%defattr(0644,root,root,0755)
%{_libdir}/libsfml-graphics.so.1.5

%files -n %{libname_n}
%defattr(0644,root,root,0755)
%{_libdir}/libsfml-network.so.1.5

%files -n %{libname_s}
%defattr(0644,root,root,0755)
%{_libdir}/libsfml-system.so.1.5

%files -n %{libname_w}
%defattr(0644,root,root,0755)
%{_libdir}/libsfml-window.so.1.5

