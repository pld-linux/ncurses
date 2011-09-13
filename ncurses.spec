#
# Conditional build:
%bcond_without	ada		# do not build Ada95 bindings
%bcond_without	cxx		# do not build C++ ncurses bindings and demo programs
#				# (this is neccessary to build ncurses linked with uClibc).
%bcond_without	gpm		# build without (dynamically loadable) libgpm support
#
%ifarch sparc64
%undefine with_ada
%endif

Summary:	curses terminal control library
Summary(de.UTF-8):	curses-Terminal-Control-Library
Summary(es.UTF-8):	Biblioteca de control de terminal curses
Summary(fr.UTF-8):	La bibliothéque de contrôle de terminal curses
Summary(pl.UTF-8):	Biblioteki do kontrolowania terminala
Summary(pt_BR.UTF-8):	Biblioteca de controle de terminal curses
Summary(ru.UTF-8):	ncurses - новая библиотека управления терминалами
Summary(tr.UTF-8):	Terminal kontrol kitaplığı
Summary(uk.UTF-8):	ncurses - нова бібліотека керування терміналами
Name:		ncurses
Version:	5.9
Release:	5
License:	distributable
Group:		Libraries
Source0:	ftp://dickey.his.com/ncurses/%{name}-%{version}.tar.gz
# Source0-md5:	8cb9c412e5f2d96bc6f459aa8c6282a1
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	3b05ee835dc20c306e9af2a9d3fbf1f1

# source: ftp://dickey.his.com/ncurses/5.9/
Patch0:		ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110409.patch.gz
# Patch0-md5:	c26b6e57a553d1589c351fd975db715e
Patch1:		ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110416.patch.gz
# Patch1-md5:	0cd0a279dae5cb10c1f39a6663620f64
Patch2:		ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110423.patch.gz
# Patch2-md5:	5cfe7668aeb60e7d49411171cf7a3794
Patch3:		ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110430.patch.gz
# Patch3-md5:	279b7bc2ee75fd87c203a06f33da7f28
Patch4:		ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110507.patch.gz
# Patch4-md5:	0b49ef1f095782b7ec11443bf65807f6
Patch5:		ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110514.patch.gz
# Patch5-md5:	9259e608ede1cda1be0121ce9ebc09b3
Patch6:		ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110521.patch.gz
# Patch6-md5:	02df6dc377fca5aa657bf433f557f369
Patch7:		ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110528.patch.gz
# Patch7-md5:	8f76dfdda995d28db6aa81df400acfc8
Patch8:		ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110604.patch.gz
# Patch8-md5:	9096cf2939126cf846879805fcacf54f
Patch9:		ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110611.patch.gz
# Patch9-md5:	e015ed8feda52fdb42175972bbae524c
Patch10:	ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110625.patch.gz
# Patch10-md5:	aef165913af8c4429ea6952ada251050
Patch11:	ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110626.patch.gz
# Patch11-md5:	8b142ba05d78a4ecf544bd332aca0e89
Patch12:	ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110702.patch.gz
# Patch12-md5:	82c3c02925e43fa229a474a6b0bff5b1
Patch13:	ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110716.patch.gz
# Patch13-md5:	cd4d1a529ac4c7bc651d098b25103080
Patch14:	ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110723.patch.gz
# Patch14-md5:	41cc27d25b5af10aa44b961ec8e0c4c1
Patch15:	ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110730.patch.gz
# Patch15-md5:	ca003e277018cfe72a1c3952423b0c48
Patch16:	ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110807.patch.gz
# Patch16-md5:	ebe7c70030af0fe49c6573e43a78f7d8
Patch17:	ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110813.patch.gz
# Patch17-md5:	2766fb18a0d63837558ceae3b499ae01
Patch18:	ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110820.patch.gz
# Patch18-md5:	420ba8a3afeb6bf1309536194499d965
Patch19:	ftp://dickey.his.com/ncurses/5.9/ncurses-5.9-20110903.patch.gz
# Patch19-md5:	2f63ea871e1895adaf7a9135c2936c4e

Patch100:	%{name}-screen_hpa_fix.patch
Patch101:	%{name}-xterm_hpa_fix.patch
Patch102:	%{name}-meta.patch
Patch103:	%{name}-xterm-home-end.patch
Patch104:	%{name}-mouse_trafo-warning.patch
Patch105:	%{name}-gnome-terminal.patch
# disable rain demo; triggers gcc bug: http://gcc.gnu.org/bugzilla/show_bug.cgi?id=14998
Patch107:	%{name}-no-rain-demo.patch
URL:		http://dickey.his.com/ncurses/ncurses.html
BuildRequires:	automake
%if %{with ada}
BuildRequires:	gcc-ada
# gnat bug: https://bugzilla.redhat.com/show_bug.cgi?id=613407
# gcc patch: https://bugzilla.redhat.com/attachment.cgi?id=435931
BuildRequires:	libgnat-static
%endif
%{?with_gpm:BuildRequires:	gpm-devel}
%{?with_cxx:BuildRequires:	libstdc++-devel}
%{?with_ada:BuildRequires:	m4}
BuildRequires:	pkgconfig
BuildRequires:	sharutils
Obsoletes:	libncurses5
Conflicts:	terminfo < 5.4-0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/ncurses

%description
The curses library routines give the user a terminal-independent
method of updating character screens with reasonable optimization.
This implementation is ``new curses'' (ncurses) and is the approved
replacement for 4.4BSD classic curses, which is being discontinued.

%description -l de.UTF-8
Die curses-Library-Routinen geben dem Benutzer eine
Terminal-unabhängige Methode zur optimierten Aktualisierung von
zeichenbasierenden Bildschirminhalten an die Hand. Die vorliegende
Implementierung ist NEW CURSES (ncurses), die offizielle
Nachfolgerversion für 4.4BSC (die klassische curses-Version), welche
nicht weitergeführt wird.

%description -l es.UTF-8
Las rutinas de la biblioteca curses ofrecen al usuario un método
independiente de terminal para actualización de las pantallas de
caracteres con optimización razonable. Este soporte es "nuevo curses"
(ncurses) y es el substituto aprobado para los clásicos curses 4.4BSD,
que se quedaban desfasados.

%description -l fr.UTF-8
Les routines de la bibliothèque curses donnent à l'utilisateur une
méthode indépendante du terminal pour la mise à jour des écrans en
mode texte avec une optimisation correcte. Ceci est l'implantation du
« nouveau curses » (ncurses) et est le remplacement du curses 4.4BSD
classique qui est abandonné.

%description -l pl.UTF-8
Biblioteka curses udostępnia funkcje pozwalające użytkownikom na
odwoływanie się do zawartości terminala niezależnie od jego typu.
Pakiet ten zawiera implementację klasycznej biblioteki curses (z
systemu 4.4BSD) o nazwie ncurses (new curses) i jest zarazem jej
przyszłym zamiennikiem.

%description -l pt_BR.UTF-8
As rotinas da biblioteca curses fornecem ao usuário um método
independente de terminal para atualização das telas de caracteres com
otimização razoável. Essa implementação é "novo curses" (ncurses) e é
o substituto aprovado para os clássicos curses 4.4BSD, que estão se
tornando obsoletos.

%description -l ru.UTF-8
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

%description -l tr.UTF-8
curses kitaplığı ile kullanıcıya kullanılan terminal tipinden bağımsız
olarak karakter tabanlı ekranlara erişim olanağı sağlanabilmektedir.
Bu uyarlama 'new curses' (ncurses), BSD deki klasik curses'in gelişmiş
halidir.

%description -l uk.UTF-8
Програми бібліотеки curses дають користувачам можливість
термінально-незалежного поновлення символьних екранів з достатньою
оптимізацією. Ця реалізація - "нові curses" (ncurses), котра є
схваленою заміною класичної бібліотеки curses з 4.4BSD, яка наразі
"знята з виробництва". В PLD Linux ncurses є життєво необхідною, без
неї не буде працювати більшость програм, що складають базову систему.
Практично всі програми, котрі виводять щось на термінал,
використовують ncurses. В PLD Linux ані бібліотека termcap, ані
традиційний файл /etc/termcap не використовуються...

%package -n terminfo
Summary:	Complete terminfo database
Summary(es.UTF-8):	Banco de datos terminfo para terminales extras (menos usados)
Summary(pl.UTF-8):	Kompletna baza terminfo
Summary(pt_BR.UTF-8):	Base de dados terminfo para terminais adicionais (menos usados)
Group:		Applications/Terminal
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ncurses-extraterms

%description -n terminfo
This package contains complete terminfo database. If you just use the
Linux console, xterm and VT100, you probably will not need this this -
a minimal %{_datadir}/terminfo tree for these terminal is already
included in the ncurses package.

%description -n terminfo -l es.UTF-8
Banco de datos terminfo para terminales extras. Las capacidades de los
terminales más usados ya están en el paquete principal ncurses.

%description -n terminfo -l pl.UTF-8
Pakiet ten zawiera kompletną bazę terminfo. Jeżeli używasz terminali
linux, console, xterm, vt100 prawdopodobnie nie bedziesz potrzebował
tego pakietu gdyż definicje tych terminali są włączone w pakiet
ncurses.

%description -n terminfo -l pt_BR.UTF-8
Base de dados terminfo para terminais extras. As definições dos
terminais mais usados já estão no pacote principal ncurses.

%package devel
Summary:	Header files for develop ncurses based application
Summary(es.UTF-8):	Bibliotecas de desarrollo para ncurses
Summary(pl.UTF-8):	Pliki nagłówkowe do bibliotek ncurses
Summary(pt_BR.UTF-8):	Bibliotecas de desenvolvimento para ncurses
Summary(ru.UTF-8):	Хедеры и библиотеки для разработки программ с ncurses
Summary(uk.UTF-8):	Хедери та бібліотеки для розробки програм з ncurses
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libncurses5-devel
Obsoletes:	libtermcap-devel

%description devel
This package includes the header files and libraries necessary to
develop applications that use ncurses.

%description devel -l es.UTF-8
Este paquete incluye las bibliotecas y archivos de inclusión
necesarios al desarrollo de aplicaciones que usan ncurses.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe niezbędne do pisania/kompilowania
programów z wykorzystaniem bibliotek ncurses.

%description devel -l pt_BR.UTF-8
Este pacote inclui as bibliotecas e arquivos de inclusão necessários
ao desenvolvimento de aplicações que usam ncurses.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры и библиотеки, необходимые для разработки
программ, использующих ncurses.

%description devel -l uk.UTF-8
Цей пакет містить хедери та бібліотеки, необхідні для розробки
програм, що використовують ncurses.

%package static
Summary:	Static libraries for ncurses
Summary(es.UTF-8):	Static libraries for ncurses development
Summary(pl.UTF-8):	Biblioteki statyczne ncurses
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com ncurses
Summary(ru.UTF-8):	Статические библиотеки для разработки программ с ncurses
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм з ncurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package includes the static libraries necessary to develop
applications that use ncurses.

%description static -l es.UTF-8
Static libraries for ncurses development.

%description static -l pl.UTF-8
Pakiet ten zawiera biblioteki statyczne ncurses.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com ncurses.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки, необходимые для разработки
программ, использующих ncurses.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки, необхідні для розробки програм,
що використовують ncurses.

%package ext
Summary:	Additional ncurses libraries
Summary(pl.UTF-8):	Dodatkowe biblioteki ncurses
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ext
This package contains addidion ncurses libraries like libforms,
libmenu and libpanel for easy making full screen curse application.

%description ext -l pl.UTF-8
Pakiet ten zawiera dodatkowe biblioteki libforms, libmenu i libpanel
służące do łatwego tworzenia aplikacji pełnoekranowych korzystających
z ncurses.

%package ext-devel
Summary:	Header files for additional ncurses libraries
Summary(pl.UTF-8):	Pliki nagłówkowe dodatkowych bibliotek ncurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ext = %{version}-%{release}

%description ext-devel
Header files for additional ncurses libraries (form, menu, panel).

%description ext-devel -l pl.UTF-8
Pliki nagłówkowe dodatkowych bibliotek ncurses (form, menu, panel).

%package ext-static
Summary:	Static versions of additional ncurses libraries
Summary(pl.UTF-8):	Statyczne wersje dodatkowych bibliotek ncurses
Group:		Development/Libraries
Requires:	%{name}-ext-devel = %{version}-%{release}

%description ext-static
Static versions of additional ncurses libraries (form, menu, panel).

%description ext-static -l pl.UTF-8
Statyczne wersje dodatkowych bibliotek ncurses (form, menu, panel).

%package c++-devel
Summary:	Header files for develop C++ ncurses based application
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki C++ ncurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description c++-devel
This package includes the header files and libraries necessary to
develop applications that use C++ ncurses.

%description c++-devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe niezbędne do kompilacji programów
z wykorzystaniem biblioteki c++-ncurses.

%package c++-static
Summary:	Static libraries for C++ ncurses
Summary(pl.UTF-8):	Biblioteki statyczne C++ ncurses
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
This package includes the static libraries necessary to develop
applications that use C++ ncurses.

%description c++-static -l pl.UTF-8
Pakiet ten zawiera biblioteki statyczne C++ ncurses.

%package ada-devel
Summary:	Header files for develop Ada95 ncurses based application
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki Ada95 ncurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
%{?with_ada:%requires_eq	gcc-ada}

%description ada-devel
This package includes the header files and libraries necessary to
develop applications that use Ada95 ncurses.

%description ada-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do
tworzenia aplikacji używających ncurses w języku Ada95.

%prep
%setup -q
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
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch107 -p1

%build
unset TERMINFO || :
gcc_target=$(gcc -dumpmachine)
gcc_version=%{cc_version}
CFLAGS="%{rpmcflags} -DPURE_TERMINFO -D_FILE_OFFSET_BITS=64"
export PKG_CONFIG_LIBDIR=%{_libdir}/pkgconfig
cp -f /usr/share/automake/config.sub .

%if "%{pld_release}" == "ti"
for t in narrowc widec; do
%else
for t in narrowc wideclowcolor widec; do
%endif
install -d obj-$t
cd obj-$t
../%configure \
	--with-install-prefix=$RPM_BUILD_ROOT \
	--with-normal \
	--with-shared \
	--with%{!?with_ada:out}-ada \
	--with%{!?with_cxx:out}-cxx \
	--with%{!?with_cxx:out}-cxx-binding \
	--with%{!?debug:out}-debug \
	--with%{!?with_gpm:out}-gpm \
	--without-profile \
	--with-largefile \
	--with-ospeed=unsigned \
	--disable-lp64 \
	--enable-hard-tabs \
	--enable-xmc-glitch \
	--enable-pc-files \
	--enable-colorfgbg \
	--with-chtype='long' \
	--with-mmask-t='long' \
	--with-manpage-aliases \
	--with-manpage-format=normal \
	--without-manpage-symlinks \
	--with-ada-include=%{_libdir}/gcc/$gcc_target/$gcc_version/adainclude/ \
	--with-ada-objects=%{_libdir}/gcc/$gcc_target/$gcc_version/adalib/ \
%if "%{pld_release}" == "ti"
	`[ "$t" != "widec" ] && echo --with-termlib=tinfo` \
	`[ "$t" = "widec" ] && echo --with-termlib=tinfow --enable-widec --includedir=%{_includedir}w`
%else
	`[ "$t" = "wideclowcolor" ] && echo --enable-widec --disable-ext-colors --includedir=%{_includedir}wlc` \
	`[ "$t" = "widec" ] && echo --enable-widec --enable-ext-colors --includedir=%{_includedir}w`
%endif

%{__make} -j1

cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib},%{_mandir}}

%if "%{pld_release}" == "ti"
for t in widec narrowc; do
%else
for t in narrowc widec; do
%endif
%{__make} -C obj-$t install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT
done

ln -sf ../l/linux $RPM_BUILD_ROOT%{_datadir}/terminfo/c/console

%if "%{pld_release}" != "ti"
mv -f $RPM_BUILD_ROOT%{_libdir}/libncursesw.so.6* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libtinfow.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libncursesw.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libcursesw.so
%else
mv -f $RPM_BUILD_ROOT%{_libdir}/libtinfow.so.5* $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT%{_libdir}/libncursesw.so.5* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libtinfow.so.5.*) $RPM_BUILD_ROOT%{_libdir}/libtinfow.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.5.*) $RPM_BUILD_ROOT%{_libdir}/libcursesw.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.5.*) $RPM_BUILD_ROOT%{_libdir}/libncursesw.so
%endif
mv -f $RPM_BUILD_ROOT%{_libdir}/libncurses.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncurses.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libtinfo.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncurses.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libcurses.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncurses.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libncurses.so

ln -sf libncursesw.a $RPM_BUILD_ROOT%{_libdir}/libcursesw.a

%if "%{pld_release}" != "ti"
cp -a obj-wideclowcolor/lib/lib*w.so.5* $RPM_BUILD_ROOT%{_libdir}
%endif

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

rm $RPM_BUILD_ROOT%{_libdir}/libcurses.a
rm $RPM_BUILD_ROOT%{_libdir}/libcursesw.a
rm $RPM_BUILD_ROOT%{_mandir}/README.ncurses-non-english-man-pages

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	ext -p /sbin/ldconfig
%postun	ext -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE README
%attr(755,root,root) %{_bindir}/captoinfo
%attr(755,root,root) %{_bindir}/clear
%attr(755,root,root) %{_bindir}/infocmp
%attr(755,root,root) %{_bindir}/infotocap
%attr(755,root,root) %{_bindir}/reset
%attr(755,root,root) %{_bindir}/tabs
%attr(755,root,root) %{_bindir}/tic
%attr(755,root,root) %{_bindir}/toe
%attr(755,root,root) %{_bindir}/tput
%attr(755,root,root) %{_bindir}/tset
%attr(755,root,root) /%{_lib}/libncurses.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libncurses.so.5
%attr(755,root,root) /%{_lib}/libncursesw.so.*.*
%if "%{pld_release}" != "ti"
%attr(755,root,root) %ghost /%{_lib}/libncursesw.so.6
%endif
%if "%{pld_release}" != "ti"
%attr(755,root,root) %{_libdir}/libncursesw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libncursesw.so.5
%else
%attr(755,root,root) %ghost /%{_lib}/libtinfow.so.5
%attr(755,root,root) %ghost /%{_lib}/libncursesw.so.5
%endif

%{_datadir}/tabset

%dir %{_datadir}/terminfo
%{_datadir}/terminfo/E
%dir %{_datadir}/terminfo/[cdgklprsvx]

%{_datadir}/terminfo/c/cygwin*
%{_datadir}/terminfo/d/dumb
%{_datadir}/terminfo/g/gnome*
%{_datadir}/terminfo/k/klone+color
%{_datadir}/terminfo/k/konsole*
%{_datadir}/terminfo/l/linux*
%{_datadir}/terminfo/p/putty*
%{_datadir}/terminfo/r/rxvt*
%{_datadir}/terminfo/s/screen*
%{_datadir}/terminfo/v/vt100
%{_datadir}/terminfo/v/vt220
%{_datadir}/terminfo/v/vt220-8
%{_datadir}/terminfo/v/vt52
%{_datadir}/terminfo/x/xterm*

%{_mandir}/man[157]/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(id) %{_mandir}/id/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man[157]/*

%files -n terminfo
%defattr(644,root,root,755)
%{_datadir}/terminfo/[1-9ALMNPQXa-ce-jm-rt-uwz]
%{_datadir}/terminfo/[dklsvx]/*
%exclude %{_datadir}/terminfo/c/cygwin*
%exclude %{_datadir}/terminfo/d/dumb
%exclude %{_datadir}/terminfo/g/gnome*
%exclude %{_datadir}/terminfo/k/klone+color
%exclude %{_datadir}/terminfo/k/konsole*
%exclude %{_datadir}/terminfo/l/linux*
%exclude %{_datadir}/terminfo/p/putty*
%exclude %{_datadir}/terminfo/r/rxvt*
%exclude %{_datadir}/terminfo/s/screen*
%exclude %{_datadir}/terminfo/v/vt100
%exclude %{_datadir}/terminfo/v/vt220
%exclude %{_datadir}/terminfo/v/vt220-8
%exclude %{_datadir}/terminfo/v/vt52
%exclude %{_datadir}/terminfo/x/xterm*

%files devel
%defattr(644,root,root,755)
%doc doc/html/ncurses-intro.html
%attr(755,root,root) %{_bindir}/ncurses5-config
%if "%{pld_release}" == "ti"
%attr(755,root,root) %{_bindir}/ncursesw5-config
%else
%attr(755,root,root) %{_bindir}/ncursesw6-config
%endif
%attr(755,root,root) %{_libdir}/libcurses.so
%attr(755,root,root) %{_libdir}/libncurses.so
%attr(755,root,root) %{_libdir}/libtinfo.so
%attr(755,root,root) %{_libdir}/libcursesw.so
%attr(755,root,root) %{_libdir}/libncursesw.so
%attr(755,root,root) %{_libdir}/libtinfow.so
%dir %{_includedir}
%{_includedir}/curses.h
%{_includedir}/eti.h
%{_includedir}/nc_tparm.h
%{_includedir}/ncurses.h
%{_includedir}/ncurses_dll.h
%{_includedir}/term.h
%{_includedir}/term_entry.h
%{_includedir}/termcap.h
%{_includedir}/tic.h
%{_includedir}/unctrl.h
%dir %{_includedir}w
%{_includedir}w/curses.h
%{_includedir}w/eti.h
%{_includedir}w/nc_tparm.h
%{_includedir}w/ncurses.h
%{_includedir}w/ncurses_dll.h
%{_includedir}w/term.h
%{_includedir}w/term_entry.h
%{_includedir}w/termcap.h
%{_includedir}w/tic.h
%{_includedir}w/unctrl.h
%{_pkgconfigdir}/*.pc

%{_mandir}/man3/*
%exclude %{_mandir}/man3/form*
%exclude %{_mandir}/man3/menu*
%exclude %{_mandir}/man3/panel*
%lang(pl) %{_mandir}/pl/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libncurses.a
%{_libdir}/libncursesw.a

%files ext
%defattr(644,root,root,755)
%if "%{pld_release}" == "ti"
%attr(755,root,root) %{_libdir}/libform.so.*
%attr(755,root,root) %{_libdir}/libmenu.so.*
%attr(755,root,root) %{_libdir}/libpanel.so.*
%attr(755,root,root) %{_libdir}/libformw.so.*
%attr(755,root,root) %{_libdir}/libmenuw.so.*
%attr(755,root,root) %{_libdir}/libpanelw.so.*
%else
%attr(755,root,root) %{_libdir}/libform.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libform.so.[56]
%attr(755,root,root) %{_libdir}/libmenu.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmenu.so.[56]
%attr(755,root,root) %{_libdir}/libpanel.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpanel.so.[56]
%attr(755,root,root) %{_libdir}/libformw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libformw.so.[56]
%attr(755,root,root) %{_libdir}/libmenuw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmenuw.so.[56]
%attr(755,root,root) %{_libdir}/libpanelw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpanelw.so.[56]
%endif

%files ext-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libform.so
%attr(755,root,root) %{_libdir}/libmenu.so
%attr(755,root,root) %{_libdir}/libpanel.so
%attr(755,root,root) %{_libdir}/libformw.so
%attr(755,root,root) %{_libdir}/libmenuw.so
%attr(755,root,root) %{_libdir}/libpanelw.so
%{_includedir}/form.h
%{_includedir}/menu.h
%{_includedir}/panel.h
%{_includedir}w/form.h
%{_includedir}w/menu.h
%{_includedir}w/panel.h
%{_mandir}/man3/form*
%{_mandir}/man3/menu*
%{_mandir}/man3/panel*

%files ext-static
%defattr(644,root,root,755)
%{_libdir}/libform.a
%{_libdir}/libmenu.a
%{_libdir}/libpanel.a
%{_libdir}/libformw.a
%{_libdir}/libmenuw.a
%{_libdir}/libpanelw.a

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
%{_includedir}w/cursesapp.h
%{_includedir}w/cursesf.h
%{_includedir}w/cursesm.h
%{_includedir}w/cursesp.h
%{_includedir}w/cursesw.h
%{_includedir}w/etip.h
%{_includedir}w/cursslk.h

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libncurses++.a
%{_libdir}/libncurses++w.a
%endif

%if %{with ada}
%files ada-devel
%defattr(644,root,root,755)
%doc Ada95/{README,TODO}
%attr(755,root,root) %{_bindir}/adacurses-config
%attr(755,root,root) %{_bindir}/adacursesw-config
%{_libdir}/gcc/*/*/adainclude/*
%{_libdir}/gcc/*/*/adalib/*
%endif
