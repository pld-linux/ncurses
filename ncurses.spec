Summary:	curses terminal control library
Summary(de):	curses-Terminal-Control-Library
Summary(fr):	La bibliothéque de contrôle de terminal curses.
Summary(pl):	Biblioteki do kontrolowania terminala
Summary(tr):	Terminal kontrol kitaplýðý
Name:		ncurses
Version:	4.2
Release:	15
Copyright:	distributable
Group:		Libraries
Group(pl):	Biblioteki
Source0:	ftp://ftp.clark.net/pub/dickey/ncurses/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.clark.net/pub/dickey/ncurses/4.2/patch-4.2-990213.sh
Source2:	captoinfo.1m.pl
Source3:	clear.1.pl
Source4:	term.7.pl
Patch0:		ncurses-rh.patch
Patch1:		ncurses-setuid.patch
Patch2:		ncurses-arm.patch
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
Biblioteka curses udostêpnia funkcje pozwalaj±ce u¿ytkownikom odwo³ywanie
siê do zawarto¶ci terminala niezale¿nie od jego typu. Pakiet tez zawiera
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
do ³atwego robienia plikacji pe³noekranowych korzystaj±cych z ncurses.

%package -n terminfo
Summary:	Complete terminfo database
Summary(pl):	Kompletna baza terminfo 
Group:		Utilities/Terminal
Group(pl):	Narzêdzia/Terminal
Requires:	%{name} = %{version}

%description -n terminfo
This package contain cmplet terminfo database. If you just use the Linux
console, xterm and VT100, you probably will not need this this - a
minimal /usr/lib/terminfo tree for these terminal is already included in the
ncurses package.

%description -l pl -n terminfo
Pakiet ten zconsoleawiera kompletn± bazê terminfo. Ke¿eli u¿ywasz terminali
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
Pakiet ten zawiera pliki nag³ówkowe - niezbêdne do pisania/kompilowania
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

%prep
%setup  -q
sh %{SOURCE1}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -DPURE_TERMINFO" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--with-install-prefix=$RPM_BUILD_ROOT \
	--with-normal \
	--with-shared \
	--without-cxx \
	--without-ada \
	--without-profile \
	--without-debug

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{lib,usr/man/pl/man{1,7}}

make install INSTALL_PREFIX=$RPM_BUILD_ROOT \
	includedir=/usr/include/ncurses

ln -sf ../l/linux $RPM_BUILD_ROOT/usr/share/terminfo/c/console

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*so.*.*}

mv $RPM_BUILD_ROOT/usr/lib/libncurses.so.*.* $RPM_BUILD_ROOT/lib
ln -sf ../../lib/libncurses.so.4.2 $RPM_BUILD_ROOT/usr/lib/libncurses.so

install %{SOURCE2} $RPM_BUILD_ROOT/usr/man/pl/man1/captoinfo.1m
install %{SOURCE3} $RPM_BUILD_ROOT/usr/man/pl/man1/clear.1
install %{SOURCE4} $RPM_BUILD_ROOT/usr/man/pl/man7/term.7

rm -f $RPM_BUILD_ROOT/usr/lib/libncurses.so.4

gzip -9nf $RPM_BUILD_ROOT/usr/man/pl/man*/* \
	README ANNOUNCE 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   ext -p /sbin/ldconfig
%postun ext -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) /lib/libncurses.so.*.*

/usr/share/tabset

%dir /usr/share/terminfo
%dir /usr/share/terminfo/l
%dir /usr/share/terminfo/v
%dir /usr/share/terminfo/x

/usr/share/terminfo/l/linux*
/usr/share/terminfo/v/vt100
/usr/share/terminfo/v/vt220
/usr/share/terminfo/v/vt220-8
/usr/share/terminfo/v/vt52
/usr/share/terminfo/x/xterm*

%attr(755,root,root) /usr/bin/*

/usr/man/man[157]/*
%lang(pl) /usr/man/pl/man[17]/*

%files ext
%attr(755,root,root) /usr/lib/lib*so.*.*

%files -n terminfo
%defattr(644,root,root,755)

/usr/share/terminfo/[1-9NPXa-km-uwz]
/usr/share/terminfo/l/la120
/usr/share/terminfo/l/layer
/usr/share/terminfo/l/lisa
/usr/share/terminfo/l/lisaterm
/usr/share/terminfo/l/lisaterm-w
/usr/share/terminfo/l/liswb
/usr/share/terminfo/l/ln03
/usr/share/terminfo/l/ln03-w
/usr/share/terminfo/l/lpr
/usr/share/terminfo/l/luna
/usr/share/terminfo/l/luna68k
/usr/share/terminfo/v/v200-nam
/usr/share/terminfo/v/v320n
/usr/share/terminfo/v/v3220
/usr/share/terminfo/v/v5410
/usr/share/terminfo/v/vapple
/usr/share/terminfo/v/vc103
/usr/share/terminfo/v/vc203
/usr/share/terminfo/v/vc303
/usr/share/terminfo/v/vc303a
/usr/share/terminfo/v/vc403a
/usr/share/terminfo/v/vc404
/usr/share/terminfo/v/vc404-s
/usr/share/terminfo/v/vc414
/usr/share/terminfo/v/vc414h
/usr/share/terminfo/v/vc415
/usr/share/terminfo/v/venix
/usr/share/terminfo/v/versaterm
/usr/share/terminfo/v/vi200
/usr/share/terminfo/v/vi200-f
/usr/share/terminfo/v/vi200-rv
/usr/share/terminfo/v/vi300
/usr/share/terminfo/v/vi300-old
/usr/share/terminfo/v/vi50
/usr/share/terminfo/v/vi500
/usr/share/terminfo/v/vi50adm
/usr/share/terminfo/v/vi55
/usr/share/terminfo/v/vi550
/usr/share/terminfo/v/vi603
/usr/share/terminfo/v/viewpoint
/usr/share/terminfo/v/viewpoint3a+
/usr/share/terminfo/v/viewpoint60
/usr/share/terminfo/v/viewpoint90
/usr/share/terminfo/v/visa50
/usr/share/terminfo/v/visual603
/usr/share/terminfo/v/vitty
/usr/share/terminfo/v/vk100
/usr/share/terminfo/v/vp3a+
/usr/share/terminfo/v/vp60
/usr/share/terminfo/v/vp90
/usr/share/terminfo/v/vremote
/usr/share/terminfo/v/vs100
/usr/share/terminfo/v/vs100-x10
/usr/share/terminfo/v/vsc
/usr/share/terminfo/v/vt-61
/usr/share/terminfo/v/vt100-am
/usr/share/terminfo/v/vt100-bot-s
/usr/share/terminfo/v/vt100-nam
/usr/share/terminfo/v/vt100-nam-w
/usr/share/terminfo/v/vt100-nav
/usr/share/terminfo/v/vt100-nav-w
/usr/share/terminfo/v/vt100-s
/usr/share/terminfo/v/vt100-s-bot
/usr/share/terminfo/v/vt100-s-top
/usr/share/terminfo/v/vt100-top-s
/usr/share/terminfo/v/vt100-w
/usr/share/terminfo/v/vt100-w-am
/usr/share/terminfo/v/vt100-w-nam
/usr/share/terminfo/v/vt100-w-nav
/usr/share/terminfo/v/vt100nam
/usr/share/terminfo/v/vt102
/usr/share/terminfo/v/vt102-nsgr
/usr/share/terminfo/v/vt102-w
/usr/share/terminfo/v/vt125
/usr/share/terminfo/v/vt131
/usr/share/terminfo/v/vt132
/usr/share/terminfo/v/vt200
/usr/share/terminfo/v/vt200-js
/usr/share/terminfo/v/vt200-w
/usr/share/terminfo/v/vt220-js
/usr/share/terminfo/v/vt220-nam
/usr/share/terminfo/v/vt220-w
/usr/share/terminfo/v/vt220d
/usr/share/terminfo/v/vt300
/usr/share/terminfo/v/vt300-nam
/usr/share/terminfo/v/vt300-w
/usr/share/terminfo/v/vt300-w-nam
/usr/share/terminfo/v/vt320
/usr/share/terminfo/v/vt320-k3
/usr/share/terminfo/v/vt320-k311
/usr/share/terminfo/v/vt320-nam
/usr/share/terminfo/v/vt320-w
/usr/share/terminfo/v/vt320-w-nam
/usr/share/terminfo/v/vt320nam
/usr/share/terminfo/v/vt330
/usr/share/terminfo/v/vt340
/usr/share/terminfo/v/vt400
/usr/share/terminfo/v/vt400-24
/usr/share/terminfo/v/vt420
/usr/share/terminfo/v/vt420f
/usr/share/terminfo/v/vt420pc
/usr/share/terminfo/v/vt420pcdos
/usr/share/terminfo/v/vt50
/usr/share/terminfo/v/vt50h
/usr/share/terminfo/v/vt510
/usr/share/terminfo/v/vt510pc
/usr/share/terminfo/v/vt510pcdos
/usr/share/terminfo/v/vt520
/usr/share/terminfo/v/vt525
/usr/share/terminfo/v/vt61
/usr/share/terminfo/v/vt61.5
/usr/share/terminfo/x/x10term
/usr/share/terminfo/x/x1700
/usr/share/terminfo/x/x1700-lm
/usr/share/terminfo/x/x1720
/usr/share/terminfo/x/x1750
/usr/share/terminfo/x/x68k
/usr/share/terminfo/x/x68k-ite
/usr/share/terminfo/x/x820
/usr/share/terminfo/x/xenix
/usr/share/terminfo/x/xerox
/usr/share/terminfo/x/xerox-lm
/usr/share/terminfo/x/xerox1720
/usr/share/terminfo/x/xerox820
/usr/share/terminfo/x/xl83
/usr/share/terminfo/x/xtalk
/usr/share/terminfo/x/xwsh

%files devel
%defattr(644,root,root,755)
%doc {README,ANNOUNCE}.gz 

%attr(755,root,root) /usr/lib/lib*.so

/usr/include/ncurses

/usr/man/man3/*

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Mon Apr 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  []
- removed Conflicts: glibc (not neccesary now),
- recompiles on new rpm.

* Sun Mar 14 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.2-14]
- compressed documentation,
- added so-links of shared libraries,
- added Group(pl) in devel subpackage,
- fixed double compressing of man pages,
- removed test/* from documentation.

* Mon Feb 22 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.2-13]
- removed man group from man pages.

* Wed Feb 17 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.2-12]
- updated to 990213 snapshot,
- removed hjl patch (now is in 990213 snap),
- added LDFLAGS="-s" to ./configure enviroment,
- removed removing linux, linux-m terminfo on sparc,
- added terminfo subbackage with full terminfo database (minimal
  term db is in main package),
- added "Conflicts: glibc <= 2.0.7" in main,
- added pl man pages for captoinfo(1), clear(1), term(7),
- added separated subpackage ext with non base ncurses libraries (separating
  this allow minimize minimal system size).

* Wed Nov 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.2-4d]
- added more patches from rawhide ncurses,
- use INSTALL_PREFIX instead prefix on "make install" (without this some
  binaries like tset have internal paths padded with Buildroot),
- shares libncurses moved to /lib,
- fixed pl translation.

* Sat Nov 07 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.2-3d]
- added some patches .. ;)
- fixed ol translation,
- full %file description,
- fixed files permissions,
- minor changes.

* Tue Sep 09 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.2-2d]
- translation modified for pl,
- build against GNU libc-2.1,
- fixed permissions of ELF binaries,
- moved Buildroot to /var/tmp/%{name}-%{version}-root
- added a static package,
- added %defattr support,
- build from non root's account, 
- start at invalid RH spec file.
