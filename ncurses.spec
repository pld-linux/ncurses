#
# Conditional build:
%bcond_with	ada		# build Ada95 bindings
%bcond_without	cxx		# do not build C++ ncurses bindings and demo programs
#		  		# (this is neccessary to build ncurses linked with uClibc).
Summary:	curses terminal control library
Summary(de):	curses-Terminal-Control-Library
Summary(es):	Biblioteca de control de terminal curses
Summary(fr):	La biblioth�que de contr�le de terminal curses
Summary(pl):	Biblioteki do kontrolowania terminala
Summary(pt_BR):	Biblioteca de controle de terminal curses
Summary(ru):	ncurses - ����� ���������� ���������� �����������
Summary(tr):	Terminal kontrol kitapl���
Summary(uk):	ncurses - ���� ¦�̦����� ��������� ���ͦ������
Name:		ncurses
Version:	5.4
Release:	2
License:	distributable
Group:		Libraries
Source0:	ftp://dickey.his.com/ncurses/%{name}-%{version}.tar.gz
# Source0-md5:	069c8880072060373290a4fefff43520
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	3b05ee835dc20c306e9af2a9d3fbf1f1
Patch0:		ftp://dickey.his.com/ncurses/5.4/%{name}-5.4-20040711-patch.sh.bz2
Patch1:		ftp://dickey.his.com/ncurses/5.4/%{name}-5.4-20040718.patch.gz
Patch2:		ftp://dickey.his.com/ncurses/5.4/%{name}-5.4-20040724.patch.gz
Patch3:		ftp://dickey.his.com/ncurses/5.4/%{name}-5.4-20040731.patch.gz
Patch13:	%{name}-screen_hpa_fix.patch
Patch14:	%{name}-xterm_hpa_fix.patch
Patch15:	%{name}-rxvt.patch
Patch16:	%{name}-meta.patch
Patch17:	%{name}-ac_hack.patch
Patch18:	%{name}-xterm-home-end.patch
Patch19:	%{name}-mouse_trafo-warning.patch
Patch20:	%{name}-gnome-terminal.patch
BuildRequires:	automake
%{?with_ada:BuildRequires:	gcc-ada}
%{?with_cxx:BuildRequires:	libstdc++-devel}
BuildRequires:	sharutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libncurses5
Conflicts:	terminfo < 5.4-0.6

%define		_includedir	%{_prefix}/include/ncurses

%description
The curses library routines give the user a terminal-independent
method of updating character screens with reasonable optimization.
This implementation is ``new curses'' (ncurses) and is the approved
replacement for 4.4BSD classic curses, which is being discontinued.

%description -l de
Die curses-Library-Routinen geben dem Benutzer eine
Terminal-unabh�ngige Methode zur optimierten Aktualisierung von
zeichenbasierenden Bildschirminhalten an die Hand. Die vorliegende
Implementierung ist NEW CURSES (ncurses), die offizielle
Nachfolgerversion f�r 4.4BSC (die klassische curses-Version), welche
nicht weitergef�hrt wird.

%description -l es
Las rutinas de la biblioteca curses ofrecen al usuario un m�todo
independiente de terminal para actualizaci�n de las pantallas de
caracteres con optimizaci�n razonable. Este soporte es "nuevo curses"
(ncurses) y es el substituto aprobado para los cl�sicos curses 4.4BSD,
que se quedaban desfasados.

%description -l fr
Les routines de la biblioth�que curses donnent � l'utilisateur une
m�thode ind�pendante du terminal pour la mise � jour des �crans en
mode texte avec une optimisation correcte. Ceci est l'implantation du
� nouveau curses � (ncurses) et est le remplacement du curses 4.4BSD
classique qui est abandonn�.

%description -l pl
Biblioteka curses udost�pnia funkcje pozwalaj�ce u�ytkownikom na
odwo�ywanie si� do zawarto�ci terminala niezale�nie od jego typu.
Pakiet ten zawiera implementacj� klasycznej biblioteki curses (z
systemu 4.4BSD) o nazwie ncurses (new curses) i jest zarazem jej
przysz�ym zamiennikiem.

%description -l pt_BR
As rotinas da biblioteca curses fornecem ao usu�rio um m�todo
independente de terminal para atualiza��o das telas de caracteres com
otimiza��o razo�vel. Essa implementa��o � "novo curses" (ncurses) e �
o substituto aprovado para os cl�ssicos curses 4.4BSD, que est�o se
tornando obsoletos.

%description -l ru
��������� ���������� curses ������������� ������������� �����������
�����������-������������ ���������� ���������� ������� � �����������
������������. ��� ���������� - "����� curses" (ncurses), �������
�������� ���������� ������� ������������ ���������� curses �� 4.4BSD,
� ��������� ����� "������ � ������������". � PLD Linux ncurses
�������� �������� �����������, ��� ��� �� ����� ��������������� ������
���������, ������������ ������� �������. ����������� ��� ���������,
������� ������� ���-���� �� ��������, ���������� ncurses. � PLD Linux
�� ���������� termcap, �� ������������ ���� /etc/termcap, ��
������������...

%description -l tr
curses kitapl��� ile kullan�c�ya kullan�lan terminal tipinden ba��ms�z
olarak karakter tabanl� ekranlara eri�im olana�� sa�lanabilmektedir.
Bu uyarlama 'new curses' (ncurses), BSD deki klasik curses'in geli�mi�
halidir.

%description -l uk
�������� ¦�̦����� curses ����� ������������ �����צ���
���ͦ������-����������� ���������� ���������� ����Φ� � ����������
����ͦ��æ��. �� ���̦��æ� - "��צ curses" (ncurses), ����� �
��������� ��ͦ��� �������ϧ ¦�̦����� curses � 4.4BSD, ��� ����ڦ
"����� � �����������". � PLD Linux ncurses � ���Ԥ�� ����Ȧ����, ���
�ŧ �� ���� ��������� ¦������� �������, �� ��������� ������ �������.
��������� �Ӧ ��������, ���Ҧ �������� ���� �� ���ͦ���,
�������������� ncurses. � PLD Linux �Φ ¦�̦����� termcap, �Φ
�����æ���� ���� /etc/termcap �� ����������������...

%package -n terminfo
Summary:	Complete terminfo database
Summary(es):	Banco de datos terminfo para terminales extras (menos usados)
Summary(pl):	Kompletna baza terminfo
Summary(pt_BR):	Base de dados terminfo para terminais adicionais (menos usados)
Group:		Applications/Terminal
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ncurses-extraterms

%description -n terminfo
This package contains cmplet terminfo database. If you just use the
Linux console, xterm and VT100, you probably will not need this this -
a minimal %{_datadir}/terminfo tree for these terminal is already
included in the ncurses package.

%description -n terminfo -l es
Banco de datos terminfo para terminales extras. Las capacidades de los
terminales m�s usados ya est�n en el paquete principal ncurses.

%description -n terminfo -l pl
Pakiet ten zawiera kompletn� baz� terminfo. Je�eli u�ywasz terminali
linux, console, xterm, vt100 prawdopodobnie nie bedziesz potrzebowa�
tego pakietu gdy� definicje tych terminali s� w��czone w pakiet
ncurses.

%description -n terminfo -l pt_BR
Base de dados terminfo para terminais extras. As defini��es dos
terminais mais usados j� est�o no pacote principal ncurses.

%package devel
Summary:	Header files for develop ncurses based application
Summary(es):	Bibliotecas de desarrollo para ncurses
Summary(pl):	Pliki nag��wkowe do bibliotek ncurses
Summary(pt_BR):	Bibliotecas de desenvolvimento para ncurses
Summary(ru):	������ � ���������� ��� ���������� �������� � ncurses
Summary(uk):	������ �� ¦�̦����� ��� �������� ������� � ncurses
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libtermcap-devel
Obsoletes:	libncurses5-devel

%description devel
This package includes the header files and libraries necessary to
develop applications that use ncurses.

%description devel -l es
Este paquete incluye las bibliotecas y archivos de inclusi�n
necesarios al desarrollo de aplicaciones que usan ncurses.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe niezb�dne do pisania/kompilowania
program�w z wykorzystaniem bibliotek ncurses.

%description devel -l pt_BR
Este pacote inclui as bibliotecas e arquivos de inclus�o necess�rios
ao desenvolvimento de aplica��es que usam ncurses.

%description devel -l ru
���� ����� �������� ������ � ����������, ����������� ��� ����������
��������, ������������ ncurses.

%description devel -l uk
��� ����� ͦ����� ������ �� ¦�̦�����, ����Ȧ�Φ ��� ��������
�������, �� �������������� ncurses.

%package static
Summary:	Static libraries for ncurses
Summary(es):	Static libraries for ncurses development
Summary(pl):	Biblioteki statyczne ncurses
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com ncurses
Summary(ru):	����������� ���������� ��� ���������� �������� � ncurses
Summary(uk):	������Φ ¦�̦����� ��� �������� ������� � ncurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package includes the static libraries necessary to develop
applications that use ncurses.

%description static -l es
Static libraries for ncurses development.

%description static -l pl
Pakiet ten zawiera biblioteki statyczne ncurses.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com ncurses.

%description static -l ru
���� ����� �������� ����������� ����������, ����������� ��� ����������
��������, ������������ ncurses.

%description static -l uk
��� ����� ͦ����� ������Φ ¦�̦�����, ����Ȧ�Φ ��� �������� �������,
�� �������������� ncurses.

%package ext
Summary:	Additional ncurses libraries
Summary(pl):	Dodatkowe biblioteki ncurses
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ext
This package contains addidion ncurses libraries like libforms,
libmenu and libpanel for easy making full screen curse application.

%description ext -l pl
Pakiet ten zawiera dodatkowe biblioteki libforms, libmenu i libpanel
s�u��ce do �atwego tworzenia aplikacji pe�noekranowych korzystaj�cych
z ncurses.

%package ext-devel
Summary:	Header files for additional ncurses libraries
Summary(pl):	Pliki nag��wkowe dodatkowych bibliotek ncurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ext = %{version}-%{release}

%description ext-devel
Header files for additional ncurses libraries (form, menu, panel).

%description ext-devel -l pl
Pliki nag��wkowe dodatkowych bibliotek ncurses (form, menu, panel).

%package ext-static
Summary:	Static versions of additional ncurses libraries
Summary(pl):	Statyczne wersje dodatkowych bibliotek ncurses
Group:		Development/Libraries
Requires:	%{name}-ext-devel = %{version}-%{release}

%description ext-static
Static versions of additional ncurses libraries (form, menu, panel).

%description ext-static -l pl
Statyczne wersje dodatkowych bibliotek ncurses (form, menu, panel).

%package c++-devel
Summary:	Header files for develop C++ ncurses based application
Summary(pl):	Pliki nag��wkowe do biblioteki C++ ncurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description c++-devel
This package includes the header files and libraries necessary to
develop applications that use C++ ncurses.

%description c++-devel -l pl
Pakiet ten zawiera pliki nag��wkowe niezb�dne do kompilacji
program�w z wykorzystaniem biblioteki c++-ncurses.

%package c++-static
Summary:	Static libraries for C++ ncurses
Summary(pl):	Biblioteki statyczne C++ ncurses
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
This package includes the static libraries necessary to develop
applications that use C++ ncurses.

%description c++-static -l pl
Pakiet ten zawiera biblioteki statyczne C++ ncurses.

%package ada-devel
Summary:	Header files for develop Ada95 ncurses based application
Summary(pl):	Pliki nag��wkowe do biblioteki Ada95 ncurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description ada-devel
This package includes the header files and libraries necessary to
develop applications that use Ada95 ncurses.

%description ada-devel -l pl
Ten pakiet zawiera pliki nag��wkowe i biblioteki potrzebne do
tworzenia aplikacji u�ywaj�cych ncurses w j�zyku Ada95.

%prep
%setup -q
bzcat %{PATCH0} > patch.sh
sh patch.sh
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch13 -p1
%patch14 -p1
#%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1

%build
unset TERMINFO || :
CFLAGS="%{rpmcflags} -DPURE_TERMINFO"
cp -f /usr/share/automake/config.sub .
for t in narrowc widec; do
install -d obj-$t
cd obj-$t
ln -sf ../configure .
%configure \
	--with-install-prefix=$RPM_BUILD_ROOT \
	--with-normal \
	--with-shared \
	--with%{!?with_ada:out}-ada \
	--with%{!?with_cxx:out}-cxx \
	--with%{!?with_cxx:out}-cxx-binding \
	--with%{!?debug:out}-debug \
	--without-profile \
	--with-termlib \
	--with-manpage-aliases \
	--with-manpage-format=normal \
	--without-manpage-symlinks \
	`[ "$t" = "widec" ] && echo --enable-widec --includedir=%{_includedir}w`
%{__make}
cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib},%{_mandir}}

for t in widec narrowc; do
%{__make} -C obj-$t install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT
done

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
%doc ANNOUNCE README
%attr(755,root,root) /%{_lib}/libncurses.so.*.*
%attr(755,root,root) /%{_lib}/libtinfo.so.*.*
%attr(755,root,root) %{_libdir}/libncursesw.so.*.*
%attr(755,root,root) %{_libdir}/libtinfow.so.*.*

%{_datadir}/tabset

%dir %{_datadir}/terminfo
%{_datadir}/terminfo/E
%dir %{_datadir}/terminfo/[dklsvx]

%{_datadir}/terminfo/d/dumb
%{_datadir}/terminfo/k/klone+color
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

%files -n terminfo
%defattr(644,root,root,755)
%{_datadir}/terminfo/[1-9ALMNPQXa-ce-jm-rt-uwz]
%{_datadir}/terminfo/[dklsvx]/*
%exclude %{_datadir}/terminfo/d/dumb
%exclude %{_datadir}/terminfo/k/klone+color
%exclude %{_datadir}/terminfo/l/linux*
%exclude %{_datadir}/terminfo/s/screen*
%exclude %{_datadir}/terminfo/v/vt100
%exclude %{_datadir}/terminfo/v/vt220
%exclude %{_datadir}/terminfo/v/vt220-8
%exclude %{_datadir}/terminfo/v/vt52
%exclude %{_datadir}/terminfo/x/xterm*

%files devel
%defattr(644,root,root,755)
%doc doc/html/ncurses-intro.html
%attr(755,root,root) %{_libdir}/libcurses.so
%attr(755,root,root) %{_libdir}/libncurses.so
%attr(755,root,root) %{_libdir}/libtinfo.so
%attr(755,root,root) %{_libdir}/libcursesw.so
%attr(755,root,root) %{_libdir}/libncursesw.so
%attr(755,root,root) %{_libdir}/libtinfow.so
%dir %{_includedir}
%{_includedir}/curses.h
%{_includedir}/eti.h
%{_includedir}/ncurses.h
%{_includedir}/ncurses_dll.h
%{_includedir}/term.h
%{_includedir}/termcap.h
%{_includedir}/unctrl.h
%dir %{_includedir}w
%{_includedir}w/curses.h
%{_includedir}w/eti.h
%{_includedir}w/ncurses.h
%{_includedir}w/ncurses_dll.h
%{_includedir}w/term.h
%{_includedir}w/termcap.h
%{_includedir}w/unctrl.h
%{_mandir}/man3/*
%exclude %{_mandir}/man3/form*
%exclude %{_mandir}/man3/menu*
%exclude %{_mandir}/man3/panel*
%lang(pl) %{_mandir}/pl/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libncurses.a
%{_libdir}/libtinfo.a
%{_libdir}/libncursesw.a
%{_libdir}/libtinfow.a

%files ext
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libform.so.*.*
%attr(755,root,root) %{_libdir}/libmenu.so.*.*
%attr(755,root,root) %{_libdir}/libpanel.so.*.*
%attr(755,root,root) %{_libdir}/libformw.so.*.*
%attr(755,root,root) %{_libdir}/libmenuw.so.*.*
%attr(755,root,root) %{_libdir}/libpanelw.so.*.*

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
%{_libdir}/ada/adainclude/*
%{_libdir}/ada/adalib/*
%endif
