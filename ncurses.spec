Summary:	curses terminal control library
Summary(de):	curses-Terminal-Control-Library
Summary(fr):	La bibliothéque de contrôle de terminal curses.
Summary(pl):	Biblioteki do kontrolowania terminala
Summary(tr):	Terminal kontrol kitaplýðý
Name:		ncurses
Version:	4.2
Release:	19
Copyright:	distributable
Group:		Libraries
Group(pl):	Biblioteki
Source0:	ftp://ftp.clark.net/pub/dickey/ncurses/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.clark.net/pub/dickey/ncurses/4.2/patches/patch-4.2-990213.sh
Source2:	captoinfo.1m.pl
Source3:	clear.1.pl
Source4:	term.7.pl
Patch0:		ncurses-rh.patch
Patch1:		ncurses-setuid.patch
Patch2:		ncurses-arm.patch
BuildPrereq:	sharutils, patch, bash, gawk, sed, gzip
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The curses library routines give the user a terminal-independent method of
updating character screens with reasonable optimization. This
implementation is ``new curses'' (ncurses) and is the approved replacement
for 4.4BSD classic curses, which is being discontinued. 

%description -l de
Die curses-Library-Routinen geben dem Benutzer eine Terminal-unabhängige
Methode zur optimierten Aktualisierung von zeichenbasierenden
Bildschirminhalten an die Hand. Die vorliegende Implementierung ist NEW
CURSES (ncurses), die offizielle Nachfolgerversion für 4.4BSC (die
klassische curses-Version), welche nicht weitergeführt wird.

%description -l fr
Les routines de la bibliothèque curses donnent à l'utilisateur une méthode
indépendante du terminal pour la mise à jour des écrans en mode texte avec une
optimisation correcte. Ceci est l'implantation du « nouveau curses » (ncurses)
et est le remplacement du curses 4.4BSD classique qui est abandonné.

%description -l pl
Biblioteka curses udostêpnia funkcje pozwalaj±ce u¿ytkownikom na odwo³ywanie
siê do zawarto¶ci terminala niezale¿nie od jego typu. Pakiet ten zawiera
implementacjê klasycznej biblioteki curses (z systemu 4.4BSD) o nazwie
ncurses (new curses) i jest zarazem jej przysz³ym zamiennikiem.

%description -l tr
curses kitaplýðý ile kullanýcýya kullanýlan terminal tipinden baðýmsýz olarak
karakter tabanlý ekranlara eriþim olanaðý saðlanabilmektedir. Bu uyarlama
'new curses' (ncurses), BSD deki klasik curses'in geliþmiþ halidir.

%package ext
Summary:	Additionan ncurses libraries
Summary(pl):	Dodatkowe biblioteki ncurses
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description ext
This package contain addidion ncurses libraries like libforms, libmenu and
libpanel for easy making full screen curse application.

%description -l pl ext
Pakiet ten zawiera dodatkowe biblioteki libforms, libmenu i libpanel s³u¿±ce
do ³atwego tworzenia aplikacji pe³noekranowych korzystaj±cych z ncurses.

%package -n terminfo
Summary:	Complete terminfo database
Summary(pl):	Kompletna baza terminfo 
Group:		Utilities/Terminal
Group(pl):	Narzêdzia/Terminal
Requires:	%{name} = %{version}

%description -n terminfo
This package contain cmplet terminfo database. If you just use the Linux
console, xterm and VT100, you probably will not need this this - a
minimal %{_datadir}/terminfo tree for these terminal is already included in the
ncurses package.

%description -l pl -n terminfo
Pakiet ten zawiera kompletn± bazê terminfo. Je¿eli u¿ywasz terminali
linux, console, xterm, vt100 prawdopodobnie nie bedziesz potrzebowa³ tego
pakietu gdy¿ definicje tych terminali s± w³±czone w pakiet ncurses.

%package devel
Summary:	Header files for develop ncurses based application
Summary(pl):	Pliki nag³ówkowe do bibliotek ncurses
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	%{name}-ext = %{version}

%description devel
This package includes the header files and libraries necessary to develop
applications that use ncurses.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe niezbêdne do pisania/kompilowania
programów z wykorzystaniem bibliotek ncurses.

%package static
Summary:	Static libraries for ncurses
Summary(pl):	Biblioteki statyczne ncurses
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package includes the static libraries necessary to develop
applications that use ncurses.

%description -l pl static
Pakiet ten zawiera biblioteki statyczne ncurses.

%package c++-devel
Summary:     Header files for develop C++ ncurses based application
Summary(pl): Pliki nag³ówkowe do biblioteki C++ ncurses
Group:       Development/Libraries
Group(pl):   Programowanie/Biblioteki
Requires:    %{name}-devel = %{version}

%description c++-devel
This package includes the header files and libraries necessary to develop
applications that use C++ ncurses.

%description -l pl c++-devel
Pakiet ten zawiera pliki nag³ówkowe niezbêdne do pisania/kompilowania
programów z wykorzystaniem biblioteki c++-ncurses.

%package c++-static
Summary:	Static libraries for C++ ncurses
Summary(pl):	Biblioteki statyczne C++ ncurses
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-c++-devel = %{version}

%description c++-static
This package includes the static libraries necessary to develop
applications that use C++ ncurses.

%description -l pl c++-static
Pakiet ten zawiera biblioteki statyczne C++ ncurses.

%prep
%setup  -q
sh %{SOURCE1}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -DPURE_TERMINFO" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--includedir=%{_includedir}/ncurses \
	--mandir=%{_mandir} \
	--with-install-prefix=$RPM_BUILD_ROOT \
	--with-normal \
	--with-shared \
	--without-ada \
	--without-profile \
	--without-debug

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_mandir}/pl/man{1,7}}

make install INSTALL_PREFIX=$RPM_BUILD_ROOT

ln -sf ../l/linux $RPM_BUILD_ROOT%{_datadir}/terminfo/c/console

strip $RPM_BUILD_ROOT{%{_bindir}/*,%{_libdir}/lib*so.*.*}

mv $RPM_BUILD_ROOT%{_libdir}/libncurses.so.*.* $RPM_BUILD_ROOT/lib
ln -sf ../../lib/libncurses.so.4.2 $RPM_BUILD_ROOT%{_libdir}/libncurses.so

install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/captoinfo.1m
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1/clear.1
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/pl/man7/term.7

rm -f $RPM_BUILD_ROOT%{_libdir}/libncurses.so.4

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/pl/man*/* README ANNOUNCE \
	misc/*.doc misc/*.html c++/{README-first,NEWS,PROBLEMS,demo.cc}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   ext -p /sbin/ldconfig
%postun ext -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) /lib/libncurses.so.*.*

%{_datadir}/tabset

%dir %{_datadir}/terminfo
%dir %{_datadir}/terminfo/l
%dir %{_datadir}/terminfo/v
%dir %{_datadir}/terminfo/x

%{_datadir}/terminfo/l/linux*
%{_datadir}/terminfo/v/vt100
%{_datadir}/terminfo/v/vt220
%{_datadir}/terminfo/v/vt220-8
%{_datadir}/terminfo/v/vt52
%{_datadir}/terminfo/x/xterm*

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man[157]/*
%lang(pl) %{_mandir}/pl/man[17]/*

%files ext
%attr(755,root,root) %{_libdir}/lib*so.*.*

%files -n terminfo
%defattr(644,root,root,755)

%{_datadir}/terminfo/[1-9NPXa-km-uwz]
%{_datadir}/terminfo/l/la120
%{_datadir}/terminfo/l/layer
%{_datadir}/terminfo/l/lisa
%{_datadir}/terminfo/l/lisaterm
%{_datadir}/terminfo/l/lisaterm-w
%{_datadir}/terminfo/l/liswb
%{_datadir}/terminfo/l/ln03
%{_datadir}/terminfo/l/ln03-w
%{_datadir}/terminfo/l/lpr
%{_datadir}/terminfo/l/luna
%{_datadir}/terminfo/l/luna68k
%{_datadir}/terminfo/v/v200-nam
%{_datadir}/terminfo/v/v320n
%{_datadir}/terminfo/v/v3220
%{_datadir}/terminfo/v/v5410
%{_datadir}/terminfo/v/vapple
%{_datadir}/terminfo/v/vc103
%{_datadir}/terminfo/v/vc203
%{_datadir}/terminfo/v/vc303
%{_datadir}/terminfo/v/vc303a
%{_datadir}/terminfo/v/vc403a
%{_datadir}/terminfo/v/vc404
%{_datadir}/terminfo/v/vc404-s
%{_datadir}/terminfo/v/vc414
%{_datadir}/terminfo/v/vc414h
%{_datadir}/terminfo/v/vc415
%{_datadir}/terminfo/v/venix
%{_datadir}/terminfo/v/versaterm
%{_datadir}/terminfo/v/vi200
%{_datadir}/terminfo/v/vi200-f
%{_datadir}/terminfo/v/vi200-rv
%{_datadir}/terminfo/v/vi300
%{_datadir}/terminfo/v/vi300-old
%{_datadir}/terminfo/v/vi50
%{_datadir}/terminfo/v/vi500
%{_datadir}/terminfo/v/vi50adm
%{_datadir}/terminfo/v/vi55
%{_datadir}/terminfo/v/vi550
%{_datadir}/terminfo/v/vi603
%{_datadir}/terminfo/v/viewpoint
%{_datadir}/terminfo/v/viewpoint3a+
%{_datadir}/terminfo/v/viewpoint60
%{_datadir}/terminfo/v/viewpoint90
%{_datadir}/terminfo/v/visa50
%{_datadir}/terminfo/v/visual603
%{_datadir}/terminfo/v/vitty
%{_datadir}/terminfo/v/vk100
%{_datadir}/terminfo/v/vp3a+
%{_datadir}/terminfo/v/vp60
%{_datadir}/terminfo/v/vp90
%{_datadir}/terminfo/v/vremote
%{_datadir}/terminfo/v/vs100
%{_datadir}/terminfo/v/vs100-x10
%{_datadir}/terminfo/v/vsc
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
%{_datadir}/terminfo/x/x10term
%{_datadir}/terminfo/x/x1700
%{_datadir}/terminfo/x/x1700-lm
%{_datadir}/terminfo/x/x1720
%{_datadir}/terminfo/x/x1750
%{_datadir}/terminfo/x/x68k
%{_datadir}/terminfo/x/x68k-ite
%{_datadir}/terminfo/x/x820
%{_datadir}/terminfo/x/xenix
%{_datadir}/terminfo/x/xerox
%{_datadir}/terminfo/x/xerox-lm
%{_datadir}/terminfo/x/xerox1720
%{_datadir}/terminfo/x/xerox820
%{_datadir}/terminfo/x/xl83
%{_datadir}/terminfo/x/xtalk
%{_datadir}/terminfo/x/xwsh

%files devel
%defattr(644,root,root,755)
%doc {README,ANNOUNCE}.gz misc/*.{doc,html}.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/ncurses/curses.h
%{_includedir}/ncurses/eti.h
%{_includedir}/ncurses/form.h
%{_includedir}/ncurses/menu.h
%{_includedir}/ncurses/ncurses.h
%{_includedir}/ncurses/panel.h
%{_includedir}/ncurses/term.h
%{_includedir}/ncurses/termcap.h
%{_includedir}/ncurses/unctrl.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libncurses.a
%{_libdir}/libform.a
%{_libdir}/libpanel.a
%{_libdir}/libmenu.a

%files c++-devel
%defattr(644,root,root,755)
%doc c++/{demo.cc,README-first,NEWS,PROBLEMS}.gz
%{_includedir}/ncurses/cursesapp.h
%{_includedir}/ncurses/cursesf.h
%{_includedir}/ncurses/cursesm.h
%{_includedir}/ncurses/cursesp.h
%{_includedir}/ncurses/cursesw.h
%{_includedir}/ncurses/etip.h
%{_includedir}/ncurses/cursslk.h

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libncurses++.a

%changelog
* Fri May 28 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.2-19]
- based on RH spec,
- spec rewrited by PLD team.c
