Summary:	curses terminal control library
Summary(de):	curses-Terminal-Control-Library
Summary(fr):	La bibliothéque de contrôle de terminal curses
Summary(pl):	Biblioteki do kontrolowania terminala
Summary(tr):	Terminal kontrol kitaplýðý
Name:		ncurses
Version:	5.2
Release:	2
License:	Distributable
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://dickey.his.com/ncurses/%{name}-%{version}.tar.gz
Source2:	captoinfo.1m.pl
Source3:	clear.1.pl
Source4:	term.7.pl
Patch0:		%{name}-rh.patch
Patch1:		%{name}-setuid.patch
Patch2:		%{name}-arm.patch
Patch3:		%{name}-libyx-lat.patch
Patch4:		%{name}-xtermchanges.patch
Patch5:		%{name}-no_symlinks.patch
BuildRequires:	sharutils, patch, bash, mawk, sed, gzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/ncurses

%description
The curses library routines give the user a terminal-independent
method of updating character screens with reasonable optimization.
This implementation is ``new curses'' (ncurses) and is the approved
replacement for 4.4BSD classic curses, which is being discontinued.

%description -l de
Die curses-Library-Routinen geben dem Benutzer eine
Terminal-unabhängige Methode zur optimierten Aktualisierung von
zeichenbasierenden Bildschirminhalten an die Hand. Die vorliegende
Implementierung ist NEW CURSES (ncurses), die offizielle
Nachfolgerversion für 4.4BSC (die klassische curses-Version), welche
nicht weitergeführt wird.

%description -l fr
Les routines de la bibliothèque curses donnent à l'utilisateur une
méthode indépendante du terminal pour la mise à jour des écrans en
mode texte avec une optimisation correcte. Ceci est l'implantation du
« nouveau curses » (ncurses) et est le remplacement du curses 4.4BSD
classique qui est abandonné.

%description -l pl
Biblioteka curses udostêpnia funkcje pozwalaj±ce u¿ytkownikom na
odwo³ywanie siê do zawarto¶ci terminala niezale¿nie od jego typu.
Pakiet ten zawiera implementacjê klasycznej biblioteki curses (z
systemu 4.4BSD) o nazwie ncurses (new curses) i jest zarazem jej
przysz³ym zamiennikiem.

%description -l tr
curses kitaplýðý ile kullanýcýya kullanýlan terminal tipinden baðýmsýz
olarak karakter tabanlý ekranlara eriþim olanaðý saðlanabilmektedir.
Bu uyarlama 'new curses' (ncurses), BSD deki klasik curses'in geliþmiþ
halidir.

%package ext
Summary:	Additional ncurses libraries
Summary(pl):	Dodatkowe biblioteki ncurses
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description ext
This package contain addidion ncurses libraries like libforms, libmenu
and libpanel for easy making full screen curse application.

%description -l pl ext
Pakiet ten zawiera dodatkowe biblioteki libforms, libmenu i libpanel
s³u¿±ce do ³atwego tworzenia aplikacji pe³noekranowych korzystaj±cych
z ncurses.

%package -n terminfo
Summary:	Complete terminfo database
Summary(pl):	Kompletna baza terminfo 
Group:		Applications/Terminal
Group(de):	Applikationen/Terminal
Group(pl):	Aplikacje/Terminal
Requires:	%{name} = %{version}

%description -n terminfo
This package contain cmplet terminfo database. If you just use the
Linux console, xterm and VT100, you probably will not need this this -
a minimal %{_datadir}/terminfo tree for these terminal is already
included in the ncurses package.

%description -l pl -n terminfo
Pakiet ten zawiera kompletn± bazê terminfo. Je¿eli u¿ywasz terminali
linux, console, xterm, vt100 prawdopodobnie nie bedziesz potrzebowa³
tego pakietu gdy¿ definicje tych terminali s± w³±czone w pakiet
ncurses.

%package devel
Summary:	Header files for develop ncurses based application
Summary(pl):	Pliki nag³ówkowe do bibliotek ncurses
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	%{name}-ext = %{version}
Obsoletes:	libtermcap-devel

%description devel
This package includes the header files and libraries necessary to
develop applications that use ncurses.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe niezbêdne do pisania/kompilowania
programów z wykorzystaniem bibliotek ncurses.

%package static
Summary:	Static libraries for ncurses
Summary(pl):	Biblioteki statyczne ncurses
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package includes the static libraries necessary to develop
applications that use ncurses.

%description -l pl static
Pakiet ten zawiera biblioteki statyczne ncurses.

%package c++-devel
Summary:	Header files for develop C++ ncurses based application
Summary(pl):	Pliki nag³ówkowe do biblioteki C++ ncurses
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description c++-devel
This package includes the header files and libraries necessary to
develop applications that use C++ ncurses.

%description -l pl c++-devel
Pakiet ten zawiera pliki nag³ówkowe niezbêdne do pisania/kompilowania
programów z wykorzystaniem biblioteki c++-ncurses.

%package c++-static
Summary:	Static libraries for C++ ncurses
Summary(pl):	Biblioteki statyczne C++ ncurses
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-c++-devel = %{version}

%description c++-static
This package includes the static libraries necessary to develop
applications that use C++ ncurses.

%description -l pl c++-static
Pakiet ten zawiera biblioteki statyczne C++ ncurses.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
CFLAGS="%{?debug:-O0 -g}%{!?debug:%{!?debug:%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}}%{?debug:-O0 -g}} -DPURE_TERMINFO"
%configure \
	--with-install-prefix=$RPM_BUILD_ROOT \
	--with-normal \
	--with-shared \
	--without-ada \
	--without-profile \
	--without-debug \
	--with-termlib \
	--enable-safe-sprintf \
	--with-manpage-format=normal

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_mandir}/pl/man{1,7}}

%{__make} install INSTALL_PREFIX=$RPM_BUILD_ROOT

ln -sf ../l/linux $RPM_BUILD_ROOT%{_datadir}/terminfo/c/console

mv -f $RPM_BUILD_ROOT%{_libdir}/libtinfo.so.*.* $RPM_BUILD_ROOT/lib
mv -f $RPM_BUILD_ROOT%{_libdir}/libncurses.so.*.* $RPM_BUILD_ROOT/lib
ln -sf ../../lib/libtinfo.so.5 $RPM_BUILD_ROOT%{_libdir}/libtinfo.so
ln -sf ../../lib/libncurses.so.5 $RPM_BUILD_ROOT%{_libdir}/libncurses.so

install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/captoinfo.1m
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1/clear.1
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/pl/man7/term.7

gzip -9nf README ANNOUNCE c++/{README-first,NEWS,PROBLEMS,demo.cc}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   ext -p /sbin/ldconfig
%postun ext -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /lib/lib*.so.*.*

%{_datadir}/tabset

%dir %{_datadir}/terminfo
%dir %{_datadir}/terminfo/l
%dir %{_datadir}/terminfo/s
%dir %{_datadir}/terminfo/v
%dir %{_datadir}/terminfo/x

%{_datadir}/terminfo/l/linux*
%{_datadir}/terminfo/s/screen
%{_datadir}/terminfo/s/screen-w
%{_datadir}/terminfo/v/vt100
%{_datadir}/terminfo/v/vt220
%{_datadir}/terminfo/v/vt220-8
%{_datadir}/terminfo/v/vt52
%{_datadir}/terminfo/x/xterm*

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man[157]/*
%lang(pl) %{_mandir}/pl/man[17]/*

%files ext
%defattr(644,root,root,755)
%{_libdir}/libform.so.*.*
%{_libdir}/libpanel.so.*.*
%{_libdir}/libmenu.so.*.*

%files -n terminfo
%defattr(644,root,root,755)
%{_datadir}/terminfo/[1-9NPXa-km-rt-uwz]
%{_datadir}/terminfo/l/l[anpu]*
%{_datadir}/terminfo/l/lisa
%{_datadir}/terminfo/l/lisaterm
%{_datadir}/terminfo/l/lisaterm-w
%{_datadir}/terminfo/l/liswb
%{_datadir}/terminfo/s/s[4bioptuvwy]*
%{_datadir}/terminfo/s/sc410
%{_datadir}/terminfo/s/sc415
%{_datadir}/terminfo/s/scanset
%{_datadir}/terminfo/s/scoansi
%{_datadir}/terminfo/s/screen-w
%{_datadir}/terminfo/s/screen2
%{_datadir}/terminfo/s/screen3
%{_datadir}/terminfo/s/screwpoint
%{_datadir}/terminfo/s/scrhp
%{_datadir}/terminfo/v/v[235aceikpr]*
%{_datadir}/terminfo/v/vt-61
%{_datadir}/terminfo/v/vt100-am
%{_datadir}/terminfo/v/vt100-bot-s
%{_datadir}/terminfo/v/vt100-nam
%{_datadir}/terminfo/v/vt100-nam-w
%{_datadir}/terminfo/v/vt100-nav
%{_datadir}/terminfo/v/vt100-nav-w
%{_datadir}/terminfo/v/vt100-s
%{_datadir}/terminfo/v/vt100-s-bot
%{_datadir}/terminfo/v/vt100-s-top
%{_datadir}/terminfo/v/vt100-top-s
%{_datadir}/terminfo/v/vt100-w
%{_datadir}/terminfo/v/vt100-w-am
%{_datadir}/terminfo/v/vt100-w-nam
%{_datadir}/terminfo/v/vt100-w-nav
%{_datadir}/terminfo/v/vt100nam
%{_datadir}/terminfo/v/vt102
%{_datadir}/terminfo/v/vt102-nsgr
%{_datadir}/terminfo/v/vt102-w
%{_datadir}/terminfo/v/vt125
%{_datadir}/terminfo/v/vt131
%{_datadir}/terminfo/v/vt132
%{_datadir}/terminfo/v/vt200
%{_datadir}/terminfo/v/vt200-js
%{_datadir}/terminfo/v/vt200-w
%{_datadir}/terminfo/v/vt220-js
%{_datadir}/terminfo/v/vt220-nam
%{_datadir}/terminfo/v/vt220-w
%{_datadir}/terminfo/v/vt220d
%{_datadir}/terminfo/v/vt300
%{_datadir}/terminfo/v/vt300-nam
%{_datadir}/terminfo/v/vt300-w
%{_datadir}/terminfo/v/vt300-w-nam
%{_datadir}/terminfo/v/vt320
%{_datadir}/terminfo/v/vt320-k3
%{_datadir}/terminfo/v/vt320-k311
%{_datadir}/terminfo/v/vt320-nam
%{_datadir}/terminfo/v/vt320-w
%{_datadir}/terminfo/v/vt320-w-nam
%{_datadir}/terminfo/v/vt320nam
%{_datadir}/terminfo/v/vt330
%{_datadir}/terminfo/v/vt340
%{_datadir}/terminfo/v/vt400
%{_datadir}/terminfo/v/vt400-24
%{_datadir}/terminfo/v/vt420
%{_datadir}/terminfo/v/vt420f
%{_datadir}/terminfo/v/vt420pc
%{_datadir}/terminfo/v/vt420pcdos
%{_datadir}/terminfo/v/vt50
%{_datadir}/terminfo/v/vt50h
%{_datadir}/terminfo/v/vt510
%{_datadir}/terminfo/v/vt510pc
%{_datadir}/terminfo/v/vt510pcdos
%{_datadir}/terminfo/v/vt520
%{_datadir}/terminfo/v/vt525
%{_datadir}/terminfo/v/vt61
%{_datadir}/terminfo/v/vt61.5
%{_datadir}/terminfo/x/x[168elw]*
%{_datadir}/terminfo/x/xtalk

%files devel
%defattr(644,root,root,755)
%doc {README,ANNOUNCE}.gz
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}
%{_includedir}/curses.h
%{_includedir}/eti.h
%{_includedir}/form.h
%{_includedir}/menu.h
%{_includedir}/ncurses.h
%{_includedir}/panel.h
%{_includedir}/term.h
%{_includedir}/termcap.h
%{_includedir}/unctrl.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libncurses.a
%{_libdir}/libtinfo.a
%{_libdir}/libform.a
%{_libdir}/libpanel.a
%{_libdir}/libmenu.a

%files c++-devel
%defattr(644,root,root,755)
%doc c++/{demo.cc,README-first,NEWS,PROBLEMS}.gz
%{_includedir}/cursesapp.h
%{_includedir}/cursesf.h
%{_includedir}/cursesm.h
%{_includedir}/cursesp.h
%{_includedir}/cursesw.h
%{_includedir}/etip.h
%{_includedir}/cursslk.h

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libncurses++.a
