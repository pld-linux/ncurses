Summary:     curses terminal control library
Summary(de): curses-Terminal-Control-Library
Summary(fr): La bibliothéque de contrôle de terminal curses.
Summary(pl): Biblioteki do kontrolowania terminala
Summary(tr): Terminal kontrol kitaplýðý
Name:        ncurses
Version:     4.2
Release:     13
Copyright:   distributable
Group:       Libraries
Source0:     ftp://ftp.clark.net/pub/dickey/ncurses/%{name}-%{version}.tar.gz
Patch0:      ncurses-4.2-updates-981202.patch.gz
Patch1:      ncurses-4.2-arm.patch
Patch2:      ncurses-4.2-hjl.patch
Patch3:      ncurses-4.2-rh.patch
Patch4:      ncurses-4.2-setuid2.patch
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
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1

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

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.* || :

mv $RPM_BUILD_ROOT/usr/lib/libncurses.so.*.* $RPM_BUILD_ROOT/lib
ln -sf ../../lib/libncurses.so.4.2 $RPM_BUILD_ROOT/usr/lib/libncurses.so

for i in $RPM_BUILD_ROOT/usr/man/man1/*m ; do
	mv $i $RPM_BUILD_ROOT/usr/man/man1/`basename $i m`
done
for i in $RPM_BUILD_ROOT/usr/man/man3/*x ; do
	mv $i $RPM_BUILD_ROOT/usr/man/man3/`basename $i x`
done

gzip -9nf $RPM_BUILD_ROOT/usr/man/man{1,3,5,7}/*

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
%attr(644, root,  man) /usr/man/man[157]/*

%files devel
%defattr(644, root, root, 755)
%doc README ANNOUNCE c++ test
/usr/lib/lib*.so
/usr/include/*
%attr(644, root,  man) /usr/man/man3/*

%files static
%attr(644, root, root) /usr/lib/lib*.a

%changelog
* Fri Dec  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.2-13]
- added gzipping man pages,
- changed man pages permission from 755 to 644,
- --with-debug configure parameter changed to --without-debug and
  --without-profile, --without-cxx, --without-ada,
- added LDFLAGS="-s" to ./configure enviroment,
- splification in devel %files,
- changed sufixes man pages file names to *.1 and *.3.

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
