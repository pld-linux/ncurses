#
# Conditional build:
%bcond_without cxx		# do not build C++ ncurses bindings and demo programs
#		  		# (this is neccessary to build ncurses linked with uClibc).
#
Summary:	curses terminal control library
Summary(de):	curses-Terminal-Control-Library
Summary(es):	Biblioteca de control de terminal curses
Summary(fr):	La bibliothИque de contrТle de terminal curses
Summary(pl):	Biblioteki do kontrolowania terminala
Summary(pt_BR):	Biblioteca de controle de terminal curses
Summary(ru):	ncurses - новая библиотека управления терминалами
Summary(tr):	Terminal kontrol kitaplЩПЩ
Summary(uk):	ncurses - нова б╕бл╕отека керування терм╕налами
Name:		ncurses
Version:	5.3
Release:	7
License:	distributable
Group:		Libraries
Source0:	ftp://dickey.his.com/ncurses/%{name}-%{version}.tar.gz
# Source0-md5: 5dcc9faa93157eafa572494bffed131a
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5: 3b05ee835dc20c306e9af2a9d3fbf1f1
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
Patch11:	%{name}-gnome-terminal.patch
%{?with_cxx:BuildRequires:	libstdc++-devel}
BuildRequires:	automake
BuildRequires:	sharutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libncurses5
Conflicts:	terminfo < 5.2-33

%define		_includedir	%{_prefix}/include/ncurses

%description
The curses library routines give the user a terminal-independent
method of updating character screens with reasonable optimization.
This implementation is ``new curses'' (ncurses) and is the approved
replacement for 4.4BSD classic curses, which is being discontinued.

%description -l de
Die curses-Library-Routinen geben dem Benutzer eine
Terminal-unabhДngige Methode zur optimierten Aktualisierung von
zeichenbasierenden Bildschirminhalten an die Hand. Die vorliegende
Implementierung ist NEW CURSES (ncurses), die offizielle
Nachfolgerversion fЭr 4.4BSC (die klassische curses-Version), welche
nicht weitergefЭhrt wird.

%description -l es
Las rutinas de la biblioteca curses ofrecen al usuario un mИtodo
independiente de terminal para actualizaciСn de las pantallas de
caracteres con optimizaciСn razonable. Este soporte es "nuevo curses"
(ncurses) y es el substituto aprobado para los clАsicos curses 4.4BSD,
que se quedaban desfasados.

%description -l fr
Les routines de la bibliothХque curses donnent Ю l'utilisateur une
mИthode indИpendante du terminal pour la mise Ю jour des Иcrans en
mode texte avec une optimisation correcte. Ceci est l'implantation du
╚ nouveau curses ╩ (ncurses) et est le remplacement du curses 4.4BSD
classique qui est abandonnИ.

%description -l pl
Biblioteka curses udostЙpnia funkcje pozwalaj╠ce u©ytkownikom na
odwoЁywanie siЙ do zawarto╤ci terminala niezale©nie od jego typu.
Pakiet ten zawiera implementacjЙ klasycznej biblioteki curses (z
systemu 4.4BSD) o nazwie ncurses (new curses) i jest zarazem jej
przyszЁym zamiennikiem.

%description -l pt_BR
As rotinas da biblioteca curses fornecem ao usuАrio um mИtodo
independente de terminal para atualizaГЦo das telas de caracteres com
otimizaГЦo razoАvel. Essa implementaГЦo И "novo curses" (ncurses) e И
o substituto aprovado para os clАssicos curses 4.4BSD, que estЦo se
tornando obsoletos.

%description -l ru
Программы библиотеки curses предоставляют пользователям возможность
терминально-независимого обновления символьных экранов с достаточной
оптимизацией. Эта реализация - "новые curses" (ncurses), которая
является одобренной заменой классической библиотеки curses из 4.4BSD,
в настоящее время "снятой с производства". В PLD Linux ncurses
является жизненно необходимой, без нее не будут функционировать многие
программы, составляющие базовую систему. Практически все программы,
которые выводят что-либо на терминал, используют ncurses. В PLD Linux
ни библиотека termcap, ни традиционный файл /etc/termcap, не
используются...

%description -l tr
curses kitaplЩПЩ ile kullanЩcЩya kullanЩlan terminal tipinden baПЩmsЩz
olarak karakter tabanlЩ ekranlara eriЧim olanaПЩ saПlanabilmektedir.
Bu uyarlama 'new curses' (ncurses), BSD deki klasik curses'in geliЧmiЧ
halidir.

%description -l uk
Програми б╕бл╕отеки curses дають користувачам можлив╕сть
терм╕нально-незалежного поновлення символьних екран╕в з достатньою
оптим╕зац╕╓ю. Ця реал╕зац╕я - "нов╕ curses" (ncurses), котра ╓
схваленою зам╕ною класично╖ б╕бл╕отеки curses з 4.4BSD, яка нараз╕
"знята з виробництва". В PLD Linux ncurses ╓ житт╓во необх╕дною, без
не╖ не буде працювати б╕льшость програм, що складають базову систему.
Практично вс╕ програми, котр╕ виводять щось на терм╕нал,
використовують ncurses. В PLD Linux ан╕ б╕бл╕отека termcap, ан╕
традиц╕йний файл /etc/termcap не використовуються...

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
sЁu©╠ce do Ёatwego tworzenia aplikacji peЁnoekranowych korzystaj╠cych
z ncurses.

%package -n terminfo
Summary:	Complete terminfo database
Summary(es):	Banco de datos terminfo para terminales extras (menos usados)
Summary(pl):	Kompletna baza terminfo
Summary(pt_BR):	Base de dados terminfo para terminais adicionais (menos usados)
Group:		Applications/Terminal
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ncurses-extraterms

%description -n terminfo
This package contain cmplet terminfo database. If you just use the
Linux console, xterm and VT100, you probably will not need this this -
a minimal %{_datadir}/terminfo tree for these terminal is already
included in the ncurses package.

%description -n terminfo -l es
Banco de datos terminfo para terminales extras. Las capacidades de los
terminales mАs usados ya estАn en el paquete principal ncurses.

%description -n terminfo -l pl
Pakiet ten zawiera kompletn╠ bazЙ terminfo. Je©eli u©ywasz terminali
linux, console, xterm, vt100 prawdopodobnie nie bedziesz potrzebowaЁ
tego pakietu gdy© definicje tych terminali s╠ wЁ╠czone w pakiet
ncurses.

%description -n terminfo -l pt_BR
Base de dados terminfo para terminais extras. As definiГУes dos
terminais mais usados jА estЦo no pacote principal ncurses.

%package devel
Summary:	Header files for develop ncurses based application
Summary(es):	Bibliotecas de desarrollo para ncurses
Summary(pl):	Pliki nagЁСwkowe do bibliotek ncurses
Summary(pt_BR):	Bibliotecas de desenvolvimento para ncurses
Summary(ru):	Хедеры и библиотеки для разработки программ с ncurses
Summary(uk):	Хедери та б╕бл╕отеки для розробки програм з ncurses
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	%{name}-ext = %{version}
Obsoletes:	libtermcap-devel
Obsoletes:	libncurses5-devel

%description devel
This package includes the header files and libraries necessary to
develop applications that use ncurses.

%description devel -l es
Este paquete incluye las bibliotecas y archivos de inclusiСn
necesarios al desarrollo de aplicaciones que usan ncurses.

%description devel -l pl
Pakiet ten zawiera pliki nagЁСwkowe niezbЙdne do pisania/kompilowania
programСw z wykorzystaniem bibliotek ncurses.

%description devel -l pt_BR
Este pacote inclui as bibliotecas e arquivos de inclusЦo necessАrios
ao desenvolvimento de aplicaГУes que usam ncurses.

%description devel -l ru
Этот пакет содержит хедеры и библиотеки, необходимые для разработки
программ, использующих ncurses.

%description devel -l uk
Цей пакет м╕стить хедери та б╕бл╕отеки, необх╕дн╕ для розробки
програм, що використовують ncurses.

%package static
Summary:	Static libraries for ncurses
Summary(es):	Static libraries for ncurses development
Summary(pl):	Biblioteki statyczne ncurses
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com ncurses
Summary(ru):	Статические библиотеки для разработки программ с ncurses
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки програм з ncurses
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
Bibliotecas estАticas para desenvolvimento com ncurses.

%description static -l ru
Этот пакет содержит статические библиотеки, необходимые для разработки
программ, использующих ncurses.

%description static -l uk
Цей пакет м╕стить статичн╕ б╕бл╕отеки, необх╕дн╕ для розробки програм,
що використовують ncurses.

%package c++-devel
Summary:	Header files for develop C++ ncurses based application
Summary(pl):	Pliki nagЁСwkowe do biblioteki C++ ncurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description c++-devel
This package includes the header files and libraries necessary to
develop applications that use C++ ncurses.

%description c++-devel -l pl
Pakiet ten zawiera pliki nagЁСwkowe niezbЙdne do pisania/kompilowania
programСw z wykorzystaniem biblioteki c++-ncurses.

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
%setup  -q
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
%patch11 -p1

%build
unset TERMINFO || :
CFLAGS="%{rpmcflags} -DPURE_TERMINFO"
cp -f /usr/share/automake/config.sub .
%configure \
	--with-install-prefix=$RPM_BUILD_ROOT \
	--with-normal \
	--with-shared \
	--without-ada \
	--with%{!?with_cxx:out}-cxx \
	--with%{!?with_cxx:out}-cxx-binding \
	--without-profile \
	--without-debug \
	--with-termlib \
	--with-manpage-format=normal

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib},%{_mandir}}

%{__make} install INSTALL_PREFIX=$RPM_BUILD_ROOT

ln -sf ../l/linux $RPM_BUILD_ROOT%{_datadir}/terminfo/c/console

mv -f $RPM_BUILD_ROOT%{_libdir}/libtinfo.so.*.* $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT%{_libdir}/libncurses.so.*.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/`cd $RPM_BUILD_ROOT/%{_lib} ; echo libtinfo.so.*.*` $RPM_BUILD_ROOT%{_libdir}/libtinfo.so
ln -sf /%{_lib}/`cd $RPM_BUILD_ROOT/%{_lib} ; echo libncurses.so.*.*` $RPM_BUILD_ROOT%{_libdir}/libcurses.so
ln -sf /%{_lib}/`cd $RPM_BUILD_ROOT/%{_lib} ; echo libncurses.so.*.*` $RPM_BUILD_ROOT%{_libdir}/libncurses.so

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   ext -p /sbin/ldconfig
%postun ext -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/lib*.so.*.*

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
