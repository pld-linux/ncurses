%bcond_without cxx		# do not build C++ ncurses bindings and demo programs
#				# (this is neccessary to build ncurses linked with uClibc).
#
Summary:	curses terminal control library
Summary(de):	curses-Terminal-Control-Library
Summary(es):	Biblioteca de control de terminal curses
Summary(fr):	La bibliothéque de contrôle de terminal curses
Summary(pl):	Biblioteki do kontrolowania terminala
Summary(pt_BR):	Biblioteca de controle de terminal curses
Summary(ru):	ncurses - ÎÏ×ÁÑ ÂÉÂÌÉÏÔÅËÁ ÕÐÒÁ×ÌÅÎÉÑ ÔÅÒÍÉÎÁÌÁÍÉ
Summary(tr):	Terminal kontrol kitaplýðý
Summary(uk):	ncurses - ÎÏ×Á Â¦ÂÌ¦ÏÔÅËÁ ËÅÒÕ×ÁÎÎÑ ÔÅÒÍ¦ÎÁÌÁÍÉ
Name:		ncurses
Version:	5.2
Release:	35.1
License:	distributable
Group:		Libraries
Source0:	ftp://dickey.his.com/ncurses/%{name}-%{version}.tar.gz
# Source0-md5:	464d6a49010cf2a6eb9ce59a264d4d47
Source1:	%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	3b05ee835dc20c306e9af2a9d3fbf1f1
Source2:	ftp://dickey.his.com/ncurses/5.2/patch-5.2-20020727.sh.gz
Patch0:		%{name}-rh.patch
Patch1:		%{name}-libyx-lat.patch
Patch2:		%{name}-no_symlinks.patch
Patch3:		%{name}-screen_hpa_fix.patch
Patch4:		%{name}-xterm-color.patch
Patch5:		%{name}-xterm_hpa_fix.patch
Patch6:		%{name}-rxvt.patch
Patch7:		%{name}-meta.patch
Patch8:		%{name}-ac_hack.patch
Patch9:		%{name}-xterm-home-end.patch
Patch10:	%{name}-mouse_trafo-warning.patch
%{?with_cxx:BuildRequires:	libstdc++-devel}
BuildRequires:	sharutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libncurses5

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

%description -l es
Las rutinas de la biblioteca curses ofrecen al usuario un método
independiente de terminal para actualización de las pantallas de
caracteres con optimización razonable. Este soporte es "nuevo curses"
(ncurses) y es el substituto aprobado para los clásicos curses 4.4BSD,
que se quedaban desfasados.

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

%description -l pt_BR
As rotinas da biblioteca curses fornecem ao usuário um método
independente de terminal para atualização das telas de caracteres com
otimização razoável. Essa implementação é "novo curses" (ncurses) e é
o substituto aprovado para os clássicos curses 4.4BSD, que estão se
tornando obsoletos.

%description -l ru
ðÒÏÇÒÁÍÍÙ ÂÉÂÌÉÏÔÅËÉ curses ÐÒÅÄÏÓÔÁ×ÌÑÀÔ ÐÏÌØÚÏ×ÁÔÅÌÑÍ ×ÏÚÍÏÖÎÏÓÔØ
ÔÅÒÍÉÎÁÌØÎÏ-ÎÅÚÁ×ÉÓÉÍÏÇÏ ÏÂÎÏ×ÌÅÎÉÑ ÓÉÍ×ÏÌØÎÙÈ ÜËÒÁÎÏ× Ó ÄÏÓÔÁÔÏÞÎÏÊ
ÏÐÔÉÍÉÚÁÃÉÅÊ. üÔÁ ÒÅÁÌÉÚÁÃÉÑ - "ÎÏ×ÙÅ curses" (ncurses), ËÏÔÏÒÁÑ
Ñ×ÌÑÅÔÓÑ ÏÄÏÂÒÅÎÎÏÊ ÚÁÍÅÎÏÊ ËÌÁÓÓÉÞÅÓËÏÊ ÂÉÂÌÉÏÔÅËÉ curses ÉÚ 4.4BSD,
× ÎÁÓÔÏÑÝÅÅ ×ÒÅÍÑ "ÓÎÑÔÏÊ Ó ÐÒÏÉÚ×ÏÄÓÔ×Á". ÷ PLD Linux ncurses
Ñ×ÌÑÅÔÓÑ ÖÉÚÎÅÎÎÏ ÎÅÏÂÈÏÄÉÍÏÊ, ÂÅÚ ÎÅÅ ÎÅ ÂÕÄÕÔ ÆÕÎËÃÉÏÎÉÒÏ×ÁÔØ ÍÎÏÇÉÅ
ÐÒÏÇÒÁÍÍÙ, ÓÏÓÔÁ×ÌÑÀÝÉÅ ÂÁÚÏ×ÕÀ ÓÉÓÔÅÍÕ. ðÒÁËÔÉÞÅÓËÉ ×ÓÅ ÐÒÏÇÒÁÍÍÙ,
ËÏÔÏÒÙÅ ×Ù×ÏÄÑÔ ÞÔÏ-ÌÉÂÏ ÎÁ ÔÅÒÍÉÎÁÌ, ÉÓÐÏÌØÚÕÀÔ ncurses. ÷ PLD Linux
ÎÉ ÂÉÂÌÉÏÔÅËÁ termcap, ÎÉ ÔÒÁÄÉÃÉÏÎÎÙÊ ÆÁÊÌ /etc/termcap, ÎÅ
ÉÓÐÏÌØÚÕÀÔÓÑ...

%description -l tr
curses kitaplýðý ile kullanýcýya kullanýlan terminal tipinden baðýmsýz
olarak karakter tabanlý ekranlara eriþim olanaðý saðlanabilmektedir.
Bu uyarlama 'new curses' (ncurses), BSD deki klasik curses'in geliþmiþ
halidir.

%description -l uk
ðÒÏÇÒÁÍÉ Â¦ÂÌ¦ÏÔÅËÉ curses ÄÁÀÔØ ËÏÒÉÓÔÕ×ÁÞÁÍ ÍÏÖÌÉ×¦ÓÔØ
ÔÅÒÍ¦ÎÁÌØÎÏ-ÎÅÚÁÌÅÖÎÏÇÏ ÐÏÎÏ×ÌÅÎÎÑ ÓÉÍ×ÏÌØÎÉÈ ÅËÒÁÎ¦× Ú ÄÏÓÔÁÔÎØÏÀ
ÏÐÔÉÍ¦ÚÁÃ¦¤À. ãÑ ÒÅÁÌ¦ÚÁÃ¦Ñ - "ÎÏ×¦ curses" (ncurses), ËÏÔÒÁ ¤
ÓÈ×ÁÌÅÎÏÀ ÚÁÍ¦ÎÏÀ ËÌÁÓÉÞÎÏ§ Â¦ÂÌ¦ÏÔÅËÉ curses Ú 4.4BSD, ÑËÁ ÎÁÒÁÚ¦
"ÚÎÑÔÁ Ú ×ÉÒÏÂÎÉÃÔ×Á". ÷ PLD Linux ncurses ¤ ÖÉÔÔ¤×Ï ÎÅÏÂÈ¦ÄÎÏÀ, ÂÅÚ
ÎÅ§ ÎÅ ÂÕÄÅ ÐÒÁÃÀ×ÁÔÉ Â¦ÌØÛÏÓÔØ ÐÒÏÇÒÁÍ, ÝÏ ÓËÌÁÄÁÀÔØ ÂÁÚÏ×Õ ÓÉÓÔÅÍÕ.
ðÒÁËÔÉÞÎÏ ×Ó¦ ÐÒÏÇÒÁÍÉ, ËÏÔÒ¦ ×É×ÏÄÑÔØ ÝÏÓØ ÎÁ ÔÅÒÍ¦ÎÁÌ,
×ÉËÏÒÉÓÔÏ×ÕÀÔØ ncurses. ÷ PLD Linux ÁÎ¦ Â¦ÂÌ¦ÏÔÅËÁ termcap, ÁÎ¦
ÔÒÁÄÉÃ¦ÊÎÉÊ ÆÁÊÌ /etc/termcap ÎÅ ×ÉËÏÒÉÓÔÏ×ÕÀÔØÓÑ...

%package ext
Summary:	Additional ncurses libraries
Summary(pl):	Dodatkowe biblioteki ncurses
Group:		Libraries
Requires:	%{name} = %{version}

%description ext
This package contain addidion ncurses libraries like libforms, libmenu
and libpanel for easy making full screen curse application.

%description ext -l pl
Pakiet ten zawiera dodatkowe biblioteki libforms, libmenu i libpanel
s³u¿±ce do ³atwego tworzenia aplikacji pe³noekranowych korzystaj±cych
z ncurses.

%package -n terminfo
Summary:	Complete terminfo database
Summary(es):	Banco de datos terminfo para terminales extras (menos usados)
Summary(pl):	Kompletna baza terminfo
Summary(pt_BR):	Base de dados terminfo para terminais adicionais (menos usados)
Group:		Applications/Terminal
Requires:	%{name} = %{version}
Obsoletes:	ncurses-extraterms

%description -n terminfo
This package contain cmplet terminfo database. If you just use the
Linux console, xterm and VT100, you probably will not need this this -
a minimal %{_datadir}/terminfo tree for these terminal is already
included in the ncurses package.

%description -n terminfo -l es
Banco de datos terminfo para terminales extras. Las capacidades de los
terminales más usados ya están en el paquete principal ncurses.

%description -n terminfo -l pl
Pakiet ten zawiera kompletn± bazê terminfo. Je¿eli u¿ywasz terminali
linux, console, xterm, vt100 prawdopodobnie nie bedziesz potrzebowa³
tego pakietu gdy¿ definicje tych terminali s± w³±czone w pakiet
ncurses.

%description -n terminfo -l pt_BR
Base de dados terminfo para terminais extras. As definições dos
terminais mais usados já estão no pacote principal ncurses.

%package devel
Summary:	Header files for develop ncurses based application
Summary(es):	Bibliotecas de desarrollo para ncurses
Summary(pl):	Pliki nag³ówkowe do bibliotek ncurses
Summary(pt_BR):	Bibliotecas de desenvolvimento para ncurses
Summary(ru):	èÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ncurses
Summary(uk):	èÅÄÅÒÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ncurses
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	%{name}-ext = %{version}
Obsoletes:	libtermcap-devel
Obsoletes:	libncurses5-devel

%description devel
This package includes the header files and libraries necessary to
develop applications that use ncurses.

%description devel -l es
Este paquete incluye las bibliotecas y archivos de inclusión
necesarios al desarrollo de aplicaciones que usan ncurses.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe niezbêdne do pisania/kompilowania
programów z wykorzystaniem bibliotek ncurses.

%description devel -l pt_BR
Este pacote inclui as bibliotecas e arquivos de inclusão necessários
ao desenvolvimento de aplicações que usam ncurses.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÈÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ
ÐÒÏÇÒÁÍÍ, ÉÓÐÏÌØÚÕÀÝÉÈ ncurses.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÈÅÄÅÒÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ
ÐÒÏÇÒÁÍ, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ ncurses.

%package static
Summary:	Static libraries for ncurses
Summary(es):	Static libraries for ncurses development
Summary(pl):	Biblioteki statyczne ncurses
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com ncurses
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ncurses
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ncurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package includes the static libraries necessary to develop
applications that use ncurses.

%description static -l es
Static libraries for ncurses development.

%description static -l pl
Pakiet ten zawiera biblioteki statyczne ncurses.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com ncurses.

%description static -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÓÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ
ÐÒÏÇÒÁÍÍ, ÉÓÐÏÌØÚÕÀÝÉÈ ncurses.

%description static -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ,
ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ ncurses.

%package c++-devel
Summary:	Header files for develop C++ ncurses based application
Summary(pl):	Pliki nag³ówkowe do biblioteki C++ ncurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description c++-devel
This package includes the header files and libraries necessary to
develop applications that use C++ ncurses.

%description c++-devel -l pl
Pakiet ten zawiera pliki nag³ówkowe niezbêdne do pisania/kompilowania
programów z wykorzystaniem biblioteki c++-ncurses.

%package c++-static
Summary:	Static libraries for C++ ncurses
Summary(pl):	Biblioteki statyczne C++ ncurses
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}

%description c++-static
This package includes the static libraries necessary to develop
applications that use C++ ncurses.

%description c++-static -l pl
Pakiet ten zawiera biblioteki statyczne C++ ncurses.

%prep
%setup -q
zcat %{SOURCE2} > patch.sh
sh patch.sh
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
CFLAGS="%{rpmcflags} -DPURE_TERMINFO"
%configure2_13 \
	--with-install-prefix=$RPM_BUILD_ROOT \
	--with-normal \
	--with-shared \
	--without-ada \
	--with%{!?with_cxx:out}-cxx \
	--with%{!?with_cxx:out}-cxx-binding \
	--without-profile \
	--without-debug \
	--with-termlib \
%ifnarch ppc
	--enable-safe-sprintf \
%endif
	--with-manpage-format=normal

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_mandir}}

%{__make} install INSTALL_PREFIX=$RPM_BUILD_ROOT

ln -sf ../l/linux $RPM_BUILD_ROOT%{_datadir}/terminfo/c/console

mv -f $RPM_BUILD_ROOT%{_libdir}/libtinfo.so.*.* $RPM_BUILD_ROOT/lib
mv -f $RPM_BUILD_ROOT%{_libdir}/libncurses.so.*.* $RPM_BUILD_ROOT/lib
ln -sf /lib/libtinfo.so.5.2 $RPM_BUILD_ROOT%{_libdir}/libtinfo.so
ln -sf /lib/libncurses.so.5.2 $RPM_BUILD_ROOT%{_libdir}/libcurses.so
ln -sf /lib/libncurses.so.5.2 $RPM_BUILD_ROOT%{_libdir}/libncurses.so

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	ext -p /sbin/ldconfig
%postun	ext -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) /lib/lib*.so.*.*

%{_datadir}/tabset

%dir %{_datadir}/terminfo
%{_datadir}/terminfo/E
%dir %{_datadir}/terminfo/d
%dir %{_datadir}/terminfo/l
%dir %{_datadir}/terminfo/s
%dir %{_datadir}/terminfo/v
%dir %{_datadir}/terminfo/x

%{_datadir}/terminfo/d/dumb
%{_datadir}/terminfo/l/linux*
%{_datadir}/terminfo/s/screen*
%{_datadir}/terminfo/v/vt100
%{_datadir}/terminfo/v/vt220
%{_datadir}/terminfo/v/vt220-8
%{_datadir}/terminfo/v/vt52
%{_datadir}/terminfo/x/xterm*

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man[157]/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(id) %{_mandir}/id/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man[157]/*

%files ext
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libform.so.*
%attr(755,root,root) %{_libdir}/libpanel.so.*
%attr(755,root,root) %{_libdir}/libmenu.so.*

%files -n terminfo
%defattr(644,root,root,755)
%{_datadir}/terminfo/[1-9ALMNPQXa-ce-km-rt-uwz]
%{_datadir}/terminfo/d/d[1-tw]*
%{_datadir}/terminfo/l/l[afnpu]*
%{_datadir}/terminfo/l/lisa
%{_datadir}/terminfo/l/lisaterm
%{_datadir}/terminfo/l/lisaterm-w
%{_datadir}/terminfo/l/liswb
%{_datadir}/terminfo/s/s[4bioptuvwy]*
%{_datadir}/terminfo/s/sc410
%{_datadir}/terminfo/s/sc415
%{_datadir}/terminfo/s/scanset
%{_datadir}/terminfo/s/sco*
%{_datadir}/terminfo/s/screwpoint
%{_datadir}/terminfo/s/scrhp
%{_datadir}/terminfo/v/v[235aceikprs]*
%{_datadir}/terminfo/v/vt-61
%{_datadir}/terminfo/v/vt100-am
%{_datadir}/terminfo/v/vt100-bm
%{_datadir}/terminfo/v/vt100-bm-o
%{_datadir}/terminfo/v/vt100-bot-s
%{_datadir}/terminfo/v/vt100nam
%{_datadir}/terminfo/v/vt100-nam
%{_datadir}/terminfo/v/vt100-nam-w
%{_datadir}/terminfo/v/vt100-nav
%{_datadir}/terminfo/v/vt100-nav-w
%{_datadir}/terminfo/v/vt100-s
%{_datadir}/terminfo/v/vt100-s-bot
%{_datadir}/terminfo/v/vt100-s-top
%{_datadir}/terminfo/v/vt100-top-s
%{_datadir}/terminfo/v/vt100-vb
%{_datadir}/terminfo/v/vt100-w
%{_datadir}/terminfo/v/vt100-w-am
%{_datadir}/terminfo/v/vt100-w-nam
%{_datadir}/terminfo/v/vt100-w-nav
%{_datadir}/terminfo/v/vt102
%{_datadir}/terminfo/v/vt102-nsgr
%{_datadir}/terminfo/v/vt102-w
%{_datadir}/terminfo/v/vt125
%{_datadir}/terminfo/v/vt131
%{_datadir}/terminfo/v/vt132
%{_datadir}/terminfo/v/vt200
%{_datadir}/terminfo/v/vt200-8
%{_datadir}/terminfo/v/vt200-8bit
%{_datadir}/terminfo/v/vt200-js
%{_datadir}/terminfo/v/vt200-old
%{_datadir}/terminfo/v/vt200-w
%{_datadir}/terminfo/v/vt220-8bit
%{_datadir}/terminfo/v/vt220d
%{_datadir}/terminfo/v/vt220-js
%{_datadir}/terminfo/v/vt220-nam
%{_datadir}/terminfo/v/vt220-old
%{_datadir}/terminfo/v/vt220-w
%{_datadir}/terminfo/v/vt300
%{_datadir}/terminfo/v/vt300-nam
%{_datadir}/terminfo/v/vt300-w
%{_datadir}/terminfo/v/vt300-w-nam
%{_datadir}/terminfo/v/vt320
%{_datadir}/terminfo/v/vt320-k3
%{_datadir}/terminfo/v/vt320-k311
%{_datadir}/terminfo/v/vt320nam
%{_datadir}/terminfo/v/vt320-nam
%{_datadir}/terminfo/v/vt320-w
%{_datadir}/terminfo/v/vt320-w-nam
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
%{_datadir}/terminfo/v/vv100
%{_datadir}/terminfo/x/x[168delnw]*
%{_datadir}/terminfo/x/xtalk

%files devel
%defattr(644,root,root,755)
%doc README ANNOUNCE
%doc doc/html/ncurses-intro.html
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}
%{_includedir}/curses.h
%{_includedir}/eti.h
%{_includedir}/form.h
%{_includedir}/menu.h
%{_includedir}/ncurses.h
%{_includedir}/ncurses_dll.h
%{_includedir}/panel.h
%{_includedir}/term.h
%{_includedir}/termcap.h
%{_includedir}/unctrl.h
%{_mandir}/man3/*
%lang(pl) %{_mandir}/pl/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libncurses.a
%{_libdir}/libtinfo.a
%{_libdir}/libform.a
%{_libdir}/libpanel.a
%{_libdir}/libmenu.a

%if %{with cxx}
%files c++-devel
%defattr(644,root,root,755)
%doc c++/{demo.cc,README-first,NEWS,PROBLEMS}
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
%endif
