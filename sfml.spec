%define	_duplicate_files_terminate_build 0

%define debug_package %{nil}

Name:			sfml
Version:		2.3.1
Release:		1

%define	major		%(echo %{version} |cut -d. -f1)
%define	minor		%(echo %{version} |cut -d. -f2)

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

Summary:	Simple and Fast Multimedia Library
License:	zlib/libpng License
Group:		System/Libraries
URL:		http://www.sfml-dev.org/
Source0:	http://www.sfml-dev.org/files/SFML-%{version}-sources.zip
Source1:	http://www.sfml-dev.org/files/SFML-%{version}-doc.zip
Source3:	sfml.rpmlintrc
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

%description -n %{develname_a}
Includes files for developing programs based on %{name}-audio.

%package -n %{develname_g}
Summary:	Header files from %{name}-graphics
Group:		Development/C++
Requires:	sfml-window-devel = %{version}
Requires:	%{libname_g} = %{version}
Provides:	%{name}-graphics-devel = %{version}-%{release}

%description -n %{develname_g}
Includes files for developing programs based on %{name}-graphics.

%package -n %{develname_n}
Summary:	Header files from %{name}-network
Group:		Development/C++
Requires:	sfml-system-devel = %{version}
Requires:	%{libname_n} = %{version}
Provides:	%{name}-network-devel = %{version}-%{release}

%description -n %{develname_n}
Includes files for developing programs based on %{name}-network.

%package -n %{develname_s}
Summary:	Header files from %{name}-system
Group:		Development/C++
Requires:	%{libname_s} = %{version}
Provides:	%{name}-system-devel = %{version}-%{release}

%description -n %{develname_s}
Includes files for developing programs based on %{name}-system.

%package -n %{develname_w}
Summary:	Header files from %{name}-window
Group:		Development/C++
Requires:	sfml-system-devel = %{version}
Requires:	%{libname_w} = %{version}
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
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR=%{buildroot} ninja -C build install

%files
%defattr(0644,root,root,0755)
%dir %{_datadir}/SFML
%{_datadir}/SFML/*.txt

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
%{_includedir}/SFML/OpenGL.hpp
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
%{_includedir}/SFML/Main.hpp
%{_includedir}/SFML/System
%{_libdir}/libsfml-system.so
%{_datadir}/SFML/cmake

%files -n %{develname_w}
%defattr(0644,root,root,0755)
%{_includedir}/SFML/Window.hpp
%{_includedir}/SFML/Window
%{_libdir}/libsfml-window.so

%files -n %{libname_a}
%defattr(0755,root,root,0755)
%{_libdir}/libsfml-audio.so.*

%files -n %{libname_g}
%defattr(0755,root,root,0755)
%{_libdir}/libsfml-graphics.so.*

%files -n %{libname_n}
%defattr(0755,root,root,0755)
%{_libdir}/libsfml-network.so.*

%files -n %{libname_s}
%defattr(0755,root,root,0755)
%{_libdir}/libsfml-system.so.*

%files -n %{libname_w}
%defattr(0755,root,root,0755)
%{_libdir}/libsfml-window.so.*
