#
# Conditional build:
%bcond_with	ada		# do not build Ada95 bindings
%bcond_without	cxx		# do not build C++ ncurses bindings and demo programs
#				# (this is neccessary to build ncurses linked with uClibc).
%bcond_without	gpm		# build without (dynamically loadable) libgpm support

%ifarch sparc64 x32
%undefine with_ada
%endif

%define	basever	5.9
%define	patchlevel	20150117
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
Version:	%{basever}.%{patchlevel}
Release:	4
License:	distributable
Group:		Libraries
Source0:	ftp://dickey.his.com/ncurses/%{name}-%{basever}.tar.gz
# Source0-md5:	8cb9c412e5f2d96bc6f459aa8c6282a1
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	3b05ee835dc20c306e9af2a9d3fbf1f1
# source: ftp://dickey.his.com/ncurses/5.9/
Patch0:		ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140308-patch.sh.bz2
# Patch0-md5:	8bd412a9c9ac97a2c504780ae87aa5d8
Patch1:		ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140315.patch.gz
# Patch1-md5:	1ddb1fbc5b301506e0522cc1364579b7
Patch2:		ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140322.patch.gz
# Patch2-md5:	e8af8722ca80e2c7693d07a1cb475235
Patch3:		ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140323.patch.gz
# Patch3-md5:	24fbdef991dd67b2557177e453efd572
Patch4:		ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140329.patch.gz
# Patch4-md5:	e7a772214088ca55185cd2230df2e9ee
Patch5:		ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140412.patch.gz
# Patch5-md5:	49762dfcdeb3f5da933319f58b9b4f18
Patch6:		ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140419.patch.gz
# Patch6-md5:	ec3760d2142cd0106a20db17a356a8cf
Patch7:		ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140426.patch.gz
# Patch7-md5:	b5df540a93b170ff946724b3a02125a2
Patch8:		ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140503.patch.gz
# Patch8-md5:	9885526f6f734e001ed6f55cd39a9feb
Patch9:		ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140510.patch.gz
# Patch9-md5:	bc591f4e1bf5dbf785b8c4c4eb5afce3
Patch10:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140524.patch.gz
# Patch10-md5:	b35022e923b354b95325e7f5f817c989
Patch11:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140607.patch.gz
# Patch11-md5:	ddfe11b9ed9477c785849c1b606d90dd
Patch12:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140609.patch.gz
# Patch12-md5:	769c45c1317021c471dd5036e7c172db
Patch13:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140614.patch.gz
# Patch13-md5:	13db4a8a7c62b4d825707c12e855dc57
Patch14:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140621.patch.gz
# Patch14-md5:	f6f582b7e76a9c1fedde3aafe6849f76
Patch15:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140629.patch.gz
# Patch15-md5:	65aa63ff4072642110f80542b3d9f885
Patch16:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140705.patch.gz
# Patch16-md5:	b5d3a9365a777e1ba0809edbca8fdebd
Patch17:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140712.patch.gz
# Patch17-md5:	9b97478790d5d6a539e6a4c0f9865ac6
Patch18:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140719.patch.gz
# Patch18-md5:	9bb67f50b2a08c8f2e1b909f68592ce8
Patch19:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140726.patch.gz
# Patch19-md5:	e45bdb82f2b3d03b5c42b85bf8f45365
Patch20:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140802.patch.gz
# Patch20-md5:	3afc2b4dd4afc2061705dd5ad3827e6b
Patch21:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140809.patch.gz
# Patch21-md5:	745c7b4660cc6a8b2982bfaefecb2184
Patch22:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140816.patch.gz
# Patch22-md5:	5aac11e74427728fa7a69d50fcdc6b6d
Patch23:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140823.patch.gz
# Patch23-md5:	a947c90441a6d1b2c8b3ce479938366c
Patch24:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140831.patch.gz
# Patch24-md5:	c44d667bacb27a46630e09ece9065468
Patch25:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140906.patch.gz
# Patch25-md5:	ff6b277fa958cccd9f74b403250bd0cf
Patch26:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140913.patch.gz
# Patch26-md5:	92433359cf3bf4d202212a2832b2521f
Patch27:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140920.patch.gz
# Patch27-md5:	70f40973fe4d96a58fb5b635be662bd5
Patch28:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20140927.patch.gz
# Patch28-md5:	649bd0ca7a2912b1b128b2073774f679
Patch29:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20141011.patch.gz
# Patch29-md5:	17e081953c7b54f12a53cd897a4edb60
Patch30:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20141018.patch.gz
# Patch30-md5:	eb676c1321f2964a9cb6d18dcfdc1a19
Patch31:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20141025.patch.gz
# Patch31-md5:	52c96fc7ec949b3c6e7fc765260eaaa4
Patch32:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20141101.patch.gz
# Patch32-md5:	e0644cdbb30184f3a424674d1480ce94
Patch33:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20141115.patch.gz
# Patch33-md5:	8fd3f6de88bec7a8afaa35d2e8c3ffb5
Patch34:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20141129.patch.gz
# Patch34-md5:	a3fd7e0cd2285dfcd47e43a6990b11d6
Patch35:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20141206.patch.gz
# Patch35-md5:	ba576465adfa4d9fadd2a1e4be5f0524
Patch36:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20141213.patch.gz
# Patch36-md5:	5b4cb12b7482133b2ce4d89ba8773200
Patch37:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20141220.patch.gz
# Patch37-md5:	793509c4f50168f6e152dca7fc9d91e5
Patch38:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20141221.patch.gz
# Patch38-md5:	0456dd738ecf3e58a0dc5d71efbd776f
Patch39:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20141227.patch.gz
# Patch39-md5:	8be86a8ff3da664b06a2b04ffc41318f
Patch40:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20150103.patch.gz
# Patch40-md5:	b5c653dbe82b7464a36ecc2e89b40da1
Patch41:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20150110.patch.gz
# Patch41-md5:	e662f8fd07bcb57fac68d9b05559929e
Patch42:	ftp://dickey.his.com/ncurses/5.9/%{name}-%{basever}-20150117.patch.gz
# Patch42-md5:	dcadc2d0b2bcc22f5546d5e02f51c26c

Patch100:	%{name}-screen_hpa_fix.patch
Patch101:	%{name}-xterm_hpa_fix.patch
Patch102:	%{name}-meta.patch
Patch103:	%{name}-xterm-home-end.patch
Patch104:	%{name}-mouse_trafo-warning.patch
Patch105:	%{name}-gnome-terminal.patch
# disable rain demo; triggers gcc bug: http://gcc.gnu.org/bugzilla/show_bug.cgi?id=14998
Patch107:	%{name}-no-rain-demo.patch
Patch108:	%{name}-fix-nonunicode-breakage.patch
URL:		http://dickey.his.com/ncurses/ncurses.html
BuildRequires:	automake
%if %{with ada}
BuildRequires:	gcc-ada
# gnat bug: https://bugzilla.redhat.com/show_bug.cgi?id=613407
# gcc patch: https://bugzilla.redhat.com/attachment.cgi?id=435931
# seems worker around when using gcc 4.6.2? --q
#BuildRequires:	libgnat-static
%endif
%{?with_gpm:BuildRequires:	gpm-devel}
%{?with_cxx:BuildRequires:	libstdc++-devel}
%{?with_ada:BuildRequires:	m4}
BuildRequires:	pkgconfig
BuildRequires:	sharutils
# for compatibility with old PLD packages
%ifarch %{x8664} ppc64 sparc64 s390x
Provides:	libtinfo.so.5()(64bit)
Provides:	libtinfow.so.5()(64bit)
Provides:	libtinfow.so.6()(64bit)
%else
Provides:	libtinfo.so.5
Provides:	libtinfow.so.5
Provides:	libtinfow.so.6
%endif
Obsoletes:	libncurses5
Conflicts:	terminfo < 5.4-0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
linux, console, xterm, vt100, vt102 prawdopodobnie nie bedziesz
potrzebował tego pakietu gdyż definicje tych terminali są włączone w
pakiet ncurses.

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
%setup -qc
mv %{name}-%{basever}/* .
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
rm -f Ada95/src/library.gpr*
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch107 -p1
%patch108 -p1

%build
unset TERMINFO || :
gcc_target=$(gcc -dumpmachine)
gcc_version=%{cc_version}
CFLAGS="%{rpmcflags} -DPURE_TERMINFO -D_FILE_OFFSET_BITS=64"
cp -f /usr/share/automake/config.sub .

for t in narrowc wideclowcolor widec; do
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
	--with-pkg-config-libdir=%{_pkgconfigdir} \
	--enable-colorfgbg \
	--with-chtype='long' \
	--with-mmask-t='long' \
	--with-manpage-aliases \
	--with-manpage-format=normal \
	--with-ada-include=%{_libdir}/gcc/$gcc_target/$gcc_version/adainclude/ \
	--with-ada-objects=%{_libdir}/gcc/$gcc_target/$gcc_version/adalib/ \
	`[ "$t" = "narrowc" ] && echo --includedir=%{_includedir}/ncursesn` \
	`[ "$t" = "wideclowcolor" ] && echo --enable-widec --disable-ext-colors --includedir=%{_includedir}/ncurseswlc` \
	`[ "$t" = "widec" ] && echo --enable-widec --enable-ext-colors --includedir=%{_includedir}/ncursesw` \
	--without-manpage-symlinks

%{__make} -j1

cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib},%{_mandir}}

for t in narrowc widec; do
%{__make} -C obj-$t install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT
done

# make ncursesw headers available also as default and ncurses/*.h headers
mkdir $RPM_BUILD_ROOT%{_includedir}/ncurses
for l in $RPM_BUILD_ROOT%{_includedir}/ncursesw/*.h; do
	bl=$(basename $l)
	ln -s ../ncursesw/$bl $RPM_BUILD_ROOT%{_includedir}/ncurses/$bl
	ln -s ncursesw/$bl $RPM_BUILD_ROOT%{_includedir}/$bl
done
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/ncursesn

ln -sf ../l/linux $RPM_BUILD_ROOT%{_datadir}/terminfo/c/console

# used by /{bin,sbin} programs
mv -f $RPM_BUILD_ROOT%{_libdir}/libncursesw.so.6* $RPM_BUILD_ROOT/%{_lib}
# adjust symlinks for libncursesw.so.6 in /%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libtinfow.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libncursesw.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libcursesw.so

# libncurses.so.5 for legacy programs
mv -f $RPM_BUILD_ROOT%{_libdir}/libncurses.so.5* $RPM_BUILD_ROOT/%{_lib}
# binary compatibility for packages using libncursesw.so.5 (without ext-colors)
cp -a obj-wideclowcolor/lib/libncursesw.so.5* $RPM_BUILD_ROOT%{_libdir}
# binary compatibility for packages using libtinfo.so.5/libtinfow.so.5/libtinfow.so.6
ln -sf $(basename $RPM_BUILD_ROOT/%{_lib}/libncurses.so.5.*) $RPM_BUILD_ROOT/%{_lib}/libtinfo.so.5
ln -sf $(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.6.*) $RPM_BUILD_ROOT/%{_lib}/libtinfow.so.6
ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libncursesw.so.5.*) $RPM_BUILD_ROOT%{_libdir}/libtinfow.so.5

# force ncursesw also for legacy -lncurses/-lcurses/-ltinfo linking
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libtinfo.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libcurses.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libncursesw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libncurses.so
# force wide ext libraries
ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libformw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libform.so
ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libmenuw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libmenu.so
ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libpanelw.so.6.*) $RPM_BUILD_ROOT%{_libdir}/libpanel.so

# similarly for static linking
ln -sf libncursesw.a $RPM_BUILD_ROOT%{_libdir}/libcursesw.a
ln -sf libncursesw.a $RPM_BUILD_ROOT%{_libdir}/libtinfow.a
ln -sf libncursesw.a $RPM_BUILD_ROOT%{_libdir}/libncurses.a
ln -sf libncursesw.a $RPM_BUILD_ROOT%{_libdir}/libcurses.a
ln -sf libncursesw.a $RPM_BUILD_ROOT%{_libdir}/libtinfo.a
ln -sf libformw.a $RPM_BUILD_ROOT%{_libdir}/libform.a
ln -sf libmenuw.a $RPM_BUILD_ROOT%{_libdir}/libmenu.a
ln -sf libpanelw.a $RPM_BUILD_ROOT%{_libdir}/libpanel.a
ln -sf libncurses++w.a $RPM_BUILD_ROOT%{_libdir}/libncurses++.a

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.ncurses-non-english-man-pages

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	ext -p /sbin/ldconfig
%postun	ext -p /sbin/ldconfig

%triggerpostun -- %{name} < 5.9-3
# rpm seems to remove them as those was %ghosts in ncurses < 5.9-3
# despite existing now as normal files/symlinks
ln -sf /%{_lib}/libncurses.so.5.* /%{_lib}/libtinfo.so.5
ln -sf /%{_lib}/libncursesw.so.6.* /%{_lib}/libtinfow.so.6
ln -sf %{_libdir}/libncursesw.so.5.* %{_libdir}/libtinfow.so.5
exit 0

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
%attr(755,root,root) %ghost /%{_lib}/libncursesw.so.6
%attr(755,root,root) %{_libdir}/libncursesw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libncursesw.so.5
# compatibility symlinks
%attr(755,root,root) /%{_lib}/libtinfo.so.5
%attr(755,root,root) /%{_lib}/libtinfow.so.6
%attr(755,root,root) %{_libdir}/libtinfow.so.5

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
%{_datadir}/terminfo/v/vt102
%{_datadir}/terminfo/v/vt220
%{_datadir}/terminfo/v/vt220-8
%{_datadir}/terminfo/v/vt52
%{_datadir}/terminfo/x/xterm*

%{_mandir}/man1/captoinfo.1m*
%{_mandir}/man1/clear.1*
%{_mandir}/man1/infocmp.1m*
%{_mandir}/man1/infotocap.1m*
%{_mandir}/man1/reset.1*
%{_mandir}/man1/tabs.1*
%{_mandir}/man1/tic.1m*
%{_mandir}/man1/toe.1m*
%{_mandir}/man1/tput.1*
%{_mandir}/man1/tset.1*
%{_mandir}/man5/term.5*
%{_mandir}/man5/terminfo.5*
%{_mandir}/man7/term.7*
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
%exclude %{_datadir}/terminfo/v/vt102
%exclude %{_datadir}/terminfo/v/vt220
%exclude %{_datadir}/terminfo/v/vt220-8
%exclude %{_datadir}/terminfo/v/vt52
%exclude %{_datadir}/terminfo/x/xterm*

%files devel
%defattr(644,root,root,755)
%doc doc/html/ncurses-intro.html
%attr(755,root,root) %{_bindir}/ncurses5-config
%attr(755,root,root) %{_bindir}/ncursesw6-config
%attr(755,root,root) %{_libdir}/libcurses.so
%attr(755,root,root) %{_libdir}/libncurses.so
%attr(755,root,root) %{_libdir}/libtinfo.so
%attr(755,root,root) %{_libdir}/libcursesw.so
%attr(755,root,root) %{_libdir}/libncursesw.so
%attr(755,root,root) %{_libdir}/libtinfow.so
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
%dir %{_includedir}/ncurses
%{_includedir}/ncurses/curses.h
%{_includedir}/ncurses/eti.h
%{_includedir}/ncurses/nc_tparm.h
%{_includedir}/ncurses/ncurses.h
%{_includedir}/ncurses/ncurses_dll.h
%{_includedir}/ncurses/term.h
%{_includedir}/ncurses/term_entry.h
%{_includedir}/ncurses/termcap.h
%{_includedir}/ncurses/tic.h
%{_includedir}/ncurses/unctrl.h
%dir %{_includedir}/ncursesw
%{_includedir}/ncursesw/curses.h
%{_includedir}/ncursesw/eti.h
%{_includedir}/ncursesw/nc_tparm.h
%{_includedir}/ncursesw/ncurses.h
%{_includedir}/ncursesw/ncurses_dll.h
%{_includedir}/ncursesw/term.h
%{_includedir}/ncursesw/term_entry.h
%{_includedir}/ncursesw/termcap.h
%{_includedir}/ncursesw/tic.h
%{_includedir}/ncursesw/unctrl.h
%{_pkgconfigdir}/ncurses.pc
%{_pkgconfigdir}/ncursesw.pc
%{_mandir}/man1/ncurses5-config.1*
%{_mandir}/man1/ncursesw6-config.1*
%{_mandir}/man3/BC.3x*
%{_mandir}/man3/COLORS.3x*
%{_mandir}/man3/COLOR_PAIR.3x*
%{_mandir}/man3/COLOR_PAIRS.3x*
%{_mandir}/man3/COLS.3x*
%{_mandir}/man3/ESCDELAY.3x*
%{_mandir}/man3/LINES.3x*
%{_mandir}/man3/PAIR_NUMBER.3x*
%{_mandir}/man3/PC.3x*
%{_mandir}/man3/SP.3x*
%{_mandir}/man3/TABSIZE.3x*
%{_mandir}/man3/UP.3x*
%{_mandir}/man3/_nc_*.3x*
%{_mandir}/man3/_trace*.3x*
%{_mandir}/man3/acs_map.3x*
%{_mandir}/man3/add*.3x*
%{_mandir}/man3/assume_default_colors*.3x*
%{_mandir}/man3/attr*.3x*
%{_mandir}/man3/baudrate*.3x*
%{_mandir}/man3/beep*.3x*
%{_mandir}/man3/bkgd*.3x*
%{_mandir}/man3/bkgrnd*.3x*
%{_mandir}/man3/bool*.3x*
%{_mandir}/man3/border*.3x*
%{_mandir}/man3/box*.3x*
%{_mandir}/man3/can_change_color*.3x*
%{_mandir}/man3/cbreak*.3x*
%{_mandir}/man3/ceiling_panel.3x*
%{_mandir}/man3/chgat.3x*
%{_mandir}/man3/clear*.3x*
%{_mandir}/man3/clrto*.3x*
%{_mandir}/man3/color_*.3x*
%{_mandir}/man3/copywin.3x*
%{_mandir}/man3/cur_term.3x*
%{_mandir}/man3/curs_*.3x*
%{_mandir}/man3/curscr.3x*
%{_mandir}/man3/curses_version.3x*
%{_mandir}/man3/def_*.3x*
%{_mandir}/man3/default_colors.3x*
%{_mandir}/man3/define_key*.3x*
%{_mandir}/man3/del_curterm*.3x*
%{_mandir}/man3/delay_output*.3x*
%{_mandir}/man3/delch.3x*
%{_mandir}/man3/deleteln.3x*
%{_mandir}/man3/delscreen.3x*
%{_mandir}/man3/delwin.3x*
%{_mandir}/man3/derwin.3x*
%{_mandir}/man3/doupdate*.3x*
%{_mandir}/man3/dupwin.3x*
%{_mandir}/man3/echo*.3x*
%{_mandir}/man3/endwin*.3x*
%{_mandir}/man3/erase*.3x*
%{_mandir}/man3/filter*.3x*
%{_mandir}/man3/flash*.3x*
%{_mandir}/man3/flushinp*.3x*
%{_mandir}/man3/get*.3x*
%{_mandir}/man3/ground_panel.3x*
%{_mandir}/man3/halfdelay*.3x*
%{_mandir}/man3/has_*.3x*
%{_mandir}/man3/hline*.3x*
%{_mandir}/man3/idcok.3x*
%{_mandir}/man3/idlok.3x*
%{_mandir}/man3/immedok.3x*
%{_mandir}/man3/in_*.3x*
%{_mandir}/man3/inch*.3x*
%{_mandir}/man3/init_color*.3x*
%{_mandir}/man3/init_pair*.3x*
%{_mandir}/man3/initscr.3x*
%{_mandir}/man3/innstr.3x*
%{_mandir}/man3/innwstr.3x*
%{_mandir}/man3/ins*.3x*
%{_mandir}/man3/intrflush*.3x*
%{_mandir}/man3/inwstr.3x*
%{_mandir}/man3/is_*.3x*
%{_mandir}/man3/isendwin*.3x*
%{_mandir}/man3/key*.3x*
%{_mandir}/man3/kill*.3x*
%{_mandir}/man3/leaveok.3x*
%{_mandir}/man3/legacy_coding.3x*
%{_mandir}/man3/longname.3x*
%{_mandir}/man3/mcprint*.3x*
%{_mandir}/man3/meta.3x*
%{_mandir}/man3/mouse*.3x*
%{_mandir}/man3/move.3x*
%{_mandir}/man3/mv*.3x*
%{_mandir}/man3/napms*.3x*
%{_mandir}/man3/ncurses.3x*
%{_mandir}/man3/new_prescr.3x*
%{_mandir}/man3/newpad*.3x*
%{_mandir}/man3/newscr.3x*
%{_mandir}/man3/newterm*.3x*
%{_mandir}/man3/newwin*.3x*
%{_mandir}/man3/nl*.3x*
%{_mandir}/man3/no*.3x*
%{_mandir}/man3/num*.3x*
%{_mandir}/man3/ospeed.3x*
%{_mandir}/man3/overlay.3x*
%{_mandir}/man3/overwrite.3x*
%{_mandir}/man3/pair_content*.3x*
%{_mandir}/man3/pecho*.3x*
%{_mandir}/man3/pnoutrefresh.3x*
%{_mandir}/man3/prefresh.3x*
%{_mandir}/man3/printw.3x*
%{_mandir}/man3/put*.3x*
%{_mandir}/man3/qiflush*.3x*
%{_mandir}/man3/raw*.3x*
%{_mandir}/man3/redrawwin.3x*
%{_mandir}/man3/refresh.3x*
%{_mandir}/man3/reset_*.3x*
%{_mandir}/man3/resetty*.3x*
%{_mandir}/man3/resize_term*.3x*
%{_mandir}/man3/resizeterm*.3x*
%{_mandir}/man3/restartterm*.3x*
%{_mandir}/man3/ripoffline*.3x*
%{_mandir}/man3/savetty*.3x*
%{_mandir}/man3/scanw.3x*
%{_mandir}/man3/scr_*.3x*
%{_mandir}/man3/scrl.3x*
%{_mandir}/man3/scroll*.3x*
%{_mandir}/man3/set_curterm*.3x*
%{_mandir}/man3/set_escdelay*.3x*
%{_mandir}/man3/set_tabsize*.3x*
%{_mandir}/man3/set_term.3x*
%{_mandir}/man3/setcchar.3x*
%{_mandir}/man3/setscrreg.3x*
%{_mandir}/man3/setsyx.3x*
%{_mandir}/man3/setterm.3x*
%{_mandir}/man3/setupterm.3x*
%{_mandir}/man3/slk_*.3x*
%{_mandir}/man3/stand*.3x*
%{_mandir}/man3/start_color*.3x*
%{_mandir}/man3/stdscr.3x*
%{_mandir}/man3/str*.3x*
%{_mandir}/man3/subpad.3x*
%{_mandir}/man3/subwin.3x*
%{_mandir}/man3/syncok.3x*
%{_mandir}/man3/term*.3x*
%{_mandir}/man3/tget*.3x*
%{_mandir}/man3/tgoto.3x*
%{_mandir}/man3/tiget*.3x*
%{_mandir}/man3/timeout.3x*
%{_mandir}/man3/tiparm.3x*
%{_mandir}/man3/touchline.3x*
%{_mandir}/man3/touchwin.3x*
%{_mandir}/man3/tparm.3x*
%{_mandir}/man3/tputs*.3x*
%{_mandir}/man3/trace.3x*
%{_mandir}/man3/ttytype.3x*
%{_mandir}/man3/typeahead*.3x*
%{_mandir}/man3/unctrl*.3x*
%{_mandir}/man3/unget*.3x*
%{_mandir}/man3/untouchwin.3x*
%{_mandir}/man3/use_*.3x*
%{_mandir}/man3/vid*.3x*
%{_mandir}/man3/vline*.3x*
%{_mandir}/man3/vw*.3x*
%{_mandir}/man3/wadd*.3x*
%{_mandir}/man3/wattr*.3x*
%{_mandir}/man3/wbkgd*.3x*
%{_mandir}/man3/wbkgrnd*.3x*
%{_mandir}/man3/wborder*.3x*
%{_mandir}/man3/wchgat.3x*
%{_mandir}/man3/wclear.3x*
%{_mandir}/man3/wclrto*.3x*
%{_mandir}/man3/wcolor_set.3x*
%{_mandir}/man3/wcursyncup.3x*
%{_mandir}/man3/wdel*.3x*
%{_mandir}/man3/wecho*.3x*
%{_mandir}/man3/wenclose.3x*
%{_mandir}/man3/werase.3x*
%{_mandir}/man3/wget*.3x*
%{_mandir}/man3/whline*.3x*
%{_mandir}/man3/win*.3x*
%{_mandir}/man3/wmouse_trafo.3x*
%{_mandir}/man3/wmove.3x*
%{_mandir}/man3/wnoutrefresh.3x*
%{_mandir}/man3/wprintw.3x*
%{_mandir}/man3/wredrawln.3x*
%{_mandir}/man3/wrefresh.3x*
%{_mandir}/man3/wresize.3x*
%{_mandir}/man3/wscanw.3x*
%{_mandir}/man3/wscrl.3x*
%{_mandir}/man3/wsetscrreg.3x*
%{_mandir}/man3/wstand*.3x*
%{_mandir}/man3/wsync*.3x*
%{_mandir}/man3/wtimeout.3x*
%{_mandir}/man3/wtouchln.3x*
%{_mandir}/man3/wunctrl*.3x*
%{_mandir}/man3/wvline*.3x*
%lang(pl) %{_mandir}/pl/man3/ncurses.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcurses.a
%{_libdir}/libncurses.a
%{_libdir}/libtinfo.a
%{_libdir}/libcursesw.a
%{_libdir}/libncursesw.a
%{_libdir}/libtinfow.a

%files ext
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libform.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libform.so.5
%attr(755,root,root) %{_libdir}/libmenu.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmenu.so.5
%attr(755,root,root) %{_libdir}/libpanel.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpanel.so.5
%attr(755,root,root) %{_libdir}/libformw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libformw.so.6
%attr(755,root,root) %{_libdir}/libmenuw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmenuw.so.6
%attr(755,root,root) %{_libdir}/libpanelw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpanelw.so.6

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
%{_includedir}/ncurses/form.h
%{_includedir}/ncurses/menu.h
%{_includedir}/ncurses/panel.h
%{_includedir}/ncursesw/form.h
%{_includedir}/ncursesw/menu.h
%{_includedir}/ncursesw/panel.h
%{_pkgconfigdir}/form.pc
%{_pkgconfigdir}/formw.pc
%{_pkgconfigdir}/menu.pc
%{_pkgconfigdir}/menuw.pc
%{_pkgconfigdir}/panel.pc
%{_pkgconfigdir}/panelw.pc
%{_mandir}/man3/TYPE_ALNUM.3x*
%{_mandir}/man3/TYPE_ALPHA.3x*
%{_mandir}/man3/TYPE_ENUM.3x*
%{_mandir}/man3/TYPE_INTEGER.3x*
%{_mandir}/man3/TYPE_IPV4.3x*
%{_mandir}/man3/TYPE_NUMERIC.3x*
%{_mandir}/man3/TYPE_REGEXP.3x*
%{_mandir}/man3/bottom_panel.3x*
%{_mandir}/man3/current_field.3x*
%{_mandir}/man3/current_item.3x*
%{_mandir}/man3/data_ahead.3x*
%{_mandir}/man3/data_behind.3x*
%{_mandir}/man3/del_panel.3x*
%{_mandir}/man3/dup_field.3x*
%{_mandir}/man3/dynamic_field_info.3x*
%{_mandir}/man3/field_*.3x*
%{_mandir}/man3/form*.3x*
%{_mandir}/man3/free_*.3x*
%{_mandir}/man3/hide_panel.3x*
%{_mandir}/man3/item_*.3x*
%{_mandir}/man3/link_field*.3x*
%{_mandir}/man3/menu*.3x*
%{_mandir}/man3/mitem_*.3x*
%{_mandir}/man3/move_field.3x*
%{_mandir}/man3/move_panel.3x*
%{_mandir}/man3/new_field*.3x*
%{_mandir}/man3/new_form*.3x*
%{_mandir}/man3/new_item.3x*
%{_mandir}/man3/new_menu*.3x*
%{_mandir}/man3/new_page.3x*
%{_mandir}/man3/new_panel.3x*
%{_mandir}/man3/panel*.3x*
%{_mandir}/man3/pos_form_cursor.3x*
%{_mandir}/man3/pos_menu_cursor.3x*
%{_mandir}/man3/post_form.3x*
%{_mandir}/man3/post_menu.3x*
%{_mandir}/man3/replace_panel.3x*
%{_mandir}/man3/scale_form.3x*
%{_mandir}/man3/scale_menu.3x*
%{_mandir}/man3/set_current_field.3x*
%{_mandir}/man3/set_current_item.3x*
%{_mandir}/man3/set_field*.3x*
%{_mandir}/man3/set_form_*.3x*
%{_mandir}/man3/set_item_*.3x*
%{_mandir}/man3/set_max_field.3x*
%{_mandir}/man3/set_menu_*.3x*
%{_mandir}/man3/set_new_page.3x*
%{_mandir}/man3/set_panel_userptr.3x*
%{_mandir}/man3/set_top_row.3x*
%{_mandir}/man3/show_panel.3x*
%{_mandir}/man3/top_panel.3x*
%{_mandir}/man3/top_row.3x*
%{_mandir}/man3/unpost_form.3x*
%{_mandir}/man3/unpost_menu.3x*
%{_mandir}/man3/update_panels*.3x*

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
%{_includedir}/ncurses/cursesapp.h
%{_includedir}/ncurses/cursesf.h
%{_includedir}/ncurses/cursesm.h
%{_includedir}/ncurses/cursesp.h
%{_includedir}/ncurses/cursesw.h
%{_includedir}/ncurses/etip.h
%{_includedir}/ncurses/cursslk.h
%{_includedir}/ncursesw/cursesapp.h
%{_includedir}/ncursesw/cursesf.h
%{_includedir}/ncursesw/cursesm.h
%{_includedir}/ncursesw/cursesp.h
%{_includedir}/ncursesw/cursesw.h
%{_includedir}/ncursesw/etip.h
%{_includedir}/ncursesw/cursslk.h
%{_pkgconfigdir}/ncurses++.pc
%{_pkgconfigdir}/ncurses++w.pc

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
%{_libdir}/gcc/*/*/adainclude/*.ad[bs]
%{_libdir}/gcc/*/*/adalib/libAdaCurses.a
%{_mandir}/man1/adacurses-config.1*
%{_mandir}/man1/adacurses.1*
%{_mandir}/man1/adacursesw-config.1*
%endif
