Summary:     curses terminal control library
Summary(de): curses-Terminal-Control-Library
Summary(fr): La bibliothéque de contrôle de terminal curses.
Summary(pl): Biblioteki do kontrolowania terminala
Summary(tr): Terminal kontrol kitaplýðý
Name:        ncurses
Version:     4.2
Release:     11
Copyright:   distributable
Group:       Libraries
Source0:     ftp://ftp.clark.net/pub/dickey/ncurses/%{name}-%{version}.tar.gz
Patch00:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980307.patch.gz
Patch01:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980314.patch.gz
Patch02:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980321.patch.gz
Patch03:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980328.patch.gz
Patch04:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980404.patch.gz
Patch05:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980411.patch.gz
Patch06:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980418.patch.gz
Patch07:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980425.patch.gz
Patch08:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980509.patch.gz
Patch09:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980516.patch.gz
Patch10:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980523.patch.gz
Patch11:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980530.patch.gz
Patch12:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980606.patch.gz
Patch13:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980613.patch.gz
Patch14:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980620.patch.gz
Patch15:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980627.patch.gz
Patch16:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980704.patch.gz
Patch17:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980711.patch.gz
Patch18:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980718.patch.gz
Patch19:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980725.patch.gz
Patch20:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980801.patch.gz
Patch21:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980808.patch.gz
Patch22:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980809.patch.gz
Patch23:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980815.patch.gz
Patch24:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980822.patch.gz
Patch25:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980829.patch.gz
Patch26:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980905.patch.gz
Patch27:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980912.patch.gz
Patch28:     ftp://ftp.clark.net/pub/dickey/ncurses/4.2/ncurses-4.2-980919.patch.gz
Patch100:    ncurses-4.2-hjl.patch
Patch101:    ncurses-4.2-rh.patch
Patch102:    ncurses-4.2-setuid2.patch
BuildRoot:   /tmp/%{name}-%{version}-root

%description
The curses library routines give the user a terminal-independent method of
updating character screens with reasonable optimization.  This
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

%package devel
Summary:     Heade files for develop ncurses based application
Summary(pl): Pliki nag³ówkowe dla ncurses
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
This package includes the header files and libraries necessary to develop
applications that use ncurses.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe - niezbêdne do pisania/kompilowania
programów z wykorzystaniem ncurses.

%package static
Summary:     Static ncurses libraries
Summary(pl): Biblioteki statyczne ncurses
Group:       Development/Libraries
Requires:    %{name}-devel = %{version}

%description static
Static ncurses libraries.

%description -l pl static
Pakiet ten zawiera biblioteki statyczne dla ncurses.

%prep
%setup -q
%patch00 -p1
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
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
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1

%patch100 -p0 -b .hjlu
%patch101 -p1 -b .rh
%patch102 -p1 -b .setuid
find . -name "*.orig" -exec rm -f {} \;

%build
CFLAGS="$RPM_OPT_FLAGS -DPURE_TERMINFO" ./configure \
	--prefix=/usr --with-normal --with-shared --with-debug --with-profile

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{lib,usr/include/ncurses}

make install INSTALL_PREFIX=$RPM_BUILD_ROOT \
	includedir=/usr/include/ncurses
ln -sf ../l/linux $RPM_BUILD_ROOT/usr/share/terminfo/c/console
ln -sf ncurses/curses.h $RPM_BUILD_ROOT/usr/include/ncurses.h
for I in curses unctrl eti form menu panel term; do
	ln -sf ncurses/$I.h $RPM_BUILD_ROOT/usr/include/$I.h
done
# remove the linux terminfo entries 
# (broken on sparc, see termfiles_sparc pkg)
%ifarch sparc
rm -f $RPM_BUILD_ROOT/usr/lib/terminfo/l/linux
rm -f $RPM_BUILD_ROOT/usr/lib/terminfo/l/linux-m
%endif

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*.so.*.*} || :

mv $RPM_BUILD_ROOT/usr/lib/libncurses.so.*.* $RPM_BUILD_ROOT/lib
ln -sf ../../lib/libncurses.so.4.2 $RPM_BUILD_ROOT/usr/lib/libncurses.so

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/lib/lib*.so.*.*
%attr(755, root, root) /lib/lib*.so.*.*
/usr/share/terminfo
/usr/share/tabset
%attr(755, root, root) /usr/bin/*
/usr/man/man[157]/*

%files devel
%defattr(644, root, root, 755)
%doc README ANNOUNCE c++ test
/usr/lib/lib*.so
/usr/include/ncurses
/usr/include/*.h
%attr(755, root,  man) /usr/man/man3/*

%files static
%attr(644, root, root) /usr/lib/lib*.a

%changelog
* Wed Nov 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.2-11]
- added more patches from rawhide ncurses,
- use INSTALL_PREFIX instead prefix on "make install" (without this some
  binaries like tset have internal paths padded with Buildroot),
- fixed pl translation.

* Tue Sep  9 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- added pl translation.

* Thu Sep  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.2-10]
- added "rm -rf $RPM_BUILD_ROOT" on start %install,
- shares libncurses moved to /lib.

* Tue Sep  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.2-9]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added striping shared libraries,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Mon Jul 20 1998 Cristian Gafton <gafton@redhat.com>
- added lots of patches. This spec file is starting to look ugly

* Wed Jul 01 1998 Alan Cox <alan@redhat.com>
- Fix setuid trusting. Open termcap/info files as the real user.

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- added terminfo entry for the poor guys using lat1 and/or lat-2 on their
  consoles... Enjoy linux-lat ! Thanks, Erik !

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- new patch to get xterm-color and nxterm terminfo entries
- aliased them to rxvt, as that seems to satisfy everybody

* Sun Apr 12 1998 Cristian Gafton <gafton@redhat.com>
- added %clean section

* Tue Apr 07 1998 Cristian Gafton <gafton@redhat.com>
- removed /usr/lib/terminfo symlink - we shouldn't need that

* Mon Apr 06 1998 Cristian Gafton <gafton@redhat.com>
- updated to 4.2 + patches
- added BuildRoot

* Sat Apr 04 1998 Cristian Gafton <gafton@redhat.com>
- rebuilt with egcs on alpha

* Wed Dec 31 1997 Erik Troan <ewt@redhat.com>
- version 7 didn't rebuild properly on the Alpha somehow -- no real changes
  are in this version

* Tue Dec 09 1997 Erik Troan <ewt@redhat.com>
- TIOCGWINSZ wasn't used properly

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc, linked shared libs against -lc
