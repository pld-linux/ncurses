.\"***************************************************************************
.\" Copyright (c) 1998 Free Software Foundation, Inc.                        *
.\"                                                                          *
.\" Permission is hereby granted, free of charge, to any person obtaining a  *
.\" copy of this software and associated documentation files (the            *
.\" "Software"), to deal in the Software without restriction, including      *
.\" without limitation the rights to use, copy, modify, merge, publish,      *
.\" distribute, distribute with modifications, sublicense, and/or sell       *
.\" copies of the Software, and to permit persons to whom the Software is    *
.\" furnished to do so, subject to the following conditions:                 *
.\"                                                                          *
.\" The above copyright notice and this permission notice shall be included  *
.\" in all copies or substantial portions of the Software.                   *
.\"                                                                          *
.\" THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS  *
.\" OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF               *
.\" MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.   *
.\" IN NO EVENT SHALL THE ABOVE COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,   *
.\" DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR    *
.\" OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR    *
.\" THE USE OR OTHER DEALINGS IN THE SOFTWARE.                               *
.\"                                                                          *
.\" Except as contained in this notice, the name(s) of the above copyright   *
.\" holders shall not be used in advertising or otherwise to promote the     *
.\" sale, use or other dealings in this Software without prior written       *
.\" authorization.                                                           *
.\"***************************************************************************
.\"
.\" $Id$
.\" Translation (c) 1998 Marcin Mazurek <mazek@capella.ae.poznan.pl>
.\" {PTM/MM/0.1/08-10-1998/"term.7 - zasady nazywania typów terminali"}
.TH TERM 7
.ds n 5
.ds d /usr/share/terminfo
.SH NAZWA
term \- zasady nazywania typów terminali
.SH OPIS
.PP
Zmienna ¶rodowiskowa \fBTERM\fR powinna standardowo zawieraæ nazwê typu  
terminala, konsoli lub urz±dzenia wy¶wietlaj±cego, którego u¿ywasz. 
Informacja ta jest niezbêdna dla wszystkich programów wy¶wietlaj±cych wyniki
na ekranie, w³±czaj±c w to Twój edytor czy program pocztowy.
.PP
Standardowa warto¶æ zmiennej \fBTERM\fR bêdzie ustawiona poprzez
inicjalizacjê lini poprzez plik \fB/etc/inittab\fR (Linux i
System-V-podobne UNIXy)
lub plik \fB/etc/ttys\fR (BSD UNIXy). To prawie zawsze wystarczy dla stacji
roboczych czy konsoli mikrokomputerów.
.PP
Je¶li u¿ywasz lini telefonicznej, typ urz±dzenia do³±czonego do niej mo¿e byæ
ró¿ny. Starsze systemy UNIXowe ustawiaj± pocz±tkowo bardzo prosty typ
terminala np. `dumb' lub `dialup'.  Nowsze mog± u¿ywaæ
terminala `vt100', odzwierciedlaj±c rozpowszechnienie terminali DECa
VT100-kompatybilnych i emulatorów z komputerów osobistych.
.PP
Nowoczesne telnet'y przekazuj± Twoj± zmienn± ¶rodowiskow± \fBTERM\fR z
lokalnego systemu do odleg³ego. Mog± wyst±piæ problemy je¿eli terminfo lub  
termcap na odleg³ym systemie nie zawiera definicji terminala kompatybilnej z
Twoj±, ale ta sytuacja jest rzadka i mo¿e byæ prawie zawsze unikniêta przez
ustawienie typu terminala na `vt100' (zak³adaj±c, ¿e rzeczywi¶cie u¿ywasz 
VT100-podobnej konsoli, terminala, lub emulatora terminala.)
.PP
W ka¿dym razie, mo¿esz dowolnie zmieniaæ zmienn± \fBTERM\fR ustawion± przez
Twój system na dowoln± warto¶æ w profilu Twojej pow³oki. Program \fBtset\fR(1) 
mo¿e byæ w tym pomocny; mo¿esz mu podaæ zbiór regu³ aby wydedukowa³ lub
za¿±da³ podania typu terminala bazuj±c na urz±dzeniu tty i prêdko¶ci
przesy³u danych (baud rate).
.PP
Ustawienie zmiennej \fBTERM\fR w³asn± warto¶ci± mo¿e byæ tak¿e u¿yteczne
je¶li stworzy³e¶ w³asn± definicjê terminala w³±czaj±c opcje (takie jak 
widzialny dzwonek (czyli b³y¶niêcie ekranu) lub pod¶wietlenie) które maj±
zamieniæ standardowe ustawienia systemu.
.PP
Opisy typów terminali s± przechowywane jako pliki zawieraj±ce dane opisuj±ce
ich mo¿liwo¶ci w katalogu \*d. Aby przejrzeæ listê wszystkich nazw terminali 
rozpoznawanych przez system, wykonaj 

	toe | more

z promptu pow³oki. Pliki te, opisuj±ce mo¿liwo¶ci terminali s± przechowywane
w formacie binarnym aby zapewniæ optymaln± prêdko¶æ dostêpu do nich
(odwrotnie ni¿ w przypadku starego bazuj±cego na tek¶cie pliku \fBtermcap\fR, 
który zastêpuj±); aby sprawdziæ jedn± z pozycji musisz u¿yæ komendy \fBinfocmp\fR(1).
Wywo³aj j± nastêpuj±co:

	infocmp \fInazwa\fR

gdzie \fInazwa\fR jest nazw± typu terminala, który chcesz sprawdziæ
(i zarazem nazw± pliku w podkatalogu \*d nazwanym od pierwszej litery typu
terminala). Komenda ta wy¶wietla plik z opisem terminala w formacie tekstowym
opisanym przez \fBterminfo\fR(\*n).  
.PP
Pierwsza linia \fBterminfo\fR(\*n) opisuje nazwy, pod którymi terminfo
rozpoznaje terminal, nazwy przedzielone s± znakami `|', a ostatnia 
zakoñczona jest przecinkiem.  Pierwsza nazwa jest podstawow± nazw±
terminala \fI(primary name)\fR, i powinna byæ u¿ywana przy ustawianiu
zmiennej \fBTERM\fR.  Ostatnia nazwa jest w
rzeczywisto¶ci opisem typu terminala (mo¿e zawieraæ spacje; inne musz± byæ
pojedynczymi s³owami). Nazwy pomiêdzy pierwsz±, a ostatni± (o ile istniej±)
s± aliasami nazwy terminala i zazwyczaj przechowywane s± tam dawne nazwy
terminala dla kompatybilno¶ci.
.PP
Istniej± pewne konwencje jak dobieraæ podstawowe nazwy terminala, które
pozwalaj± aby by³y unikalne, a zarazem nios³y w sobie pewn± informacjê.
Poni¿ej zamieszczony jest przewodnik, który krok po kroku wyja¶nia jak
nazywaæ a tak¿e jak je rozumieæ:
.PP
Najpierw wybierz g³ówn± nazwê.  Powinna siê ona sk³adaæ z ma³ej litery
i nastêpuj±cych po niej do siedmiu ma³ych liter b±d¼ cyfr. Powiniene¶
unikaæ u¿ywania znaków przestankowych w g³ównych nazwach, poniewa¿ s± one
u¿ywane i interpretowane jako nazwy plików i meta-znaków pow³oki
(np. takie jak !, $, *, ? etc.), umieszczone w nich mog± spowodowaæ dziwne
i k³opotliwe zachowanie.
Uko¶nik (/), czy jakikolwiek inny znak, który mo¿e zostaæ zinterpretowany
przez czyj¶ system plików (\e, $, [, ]), jest szczególnie niebezpieczne 
(terminfo jest niezale¿ne od platformy, wiêc wybór nazwy zawieraj±cej znaki
specjalne mo¿e którego¶ dnia spowodowaæ pewne problemy dla przysz³ych
u¿ytkowników). Znak kropki (.) jest wzglêdnie bezpieczny o ile wystêpuje co
najwy¿ej jedna w nazwie g³ównej; niektóre starsze nazwy terminfo
wykorzystuj± j±.
.PP
Nazwa g³ówna terminala lub typu konsoli stacji roboczej powinna prawie zawsze
zaczynaæ siê od przedrostka sprzedawcy (np. \fBhp\fR dla Hewlett-Packard, \fBwy\fR
dla Wyse, czy \fBatt\fR dla terminali AT&T), lub popularn± nazw± lini
terminala (\fBvt\fR dla terminali typu  VT od DECa, czy \fBsun\fR dla
konsoli stacji roboczych Suna czy \fBregent\fR dla modeli ADDS Regent).
Mo¿esz wylistowaæ drzewo terminfo aby zobaczyæ jakie przedrostki s± ju¿ w
powszechnym u¿yciu.
Po nazwie g³ównej powinien znajdowaæ siê, je¶li to potrzebne, numer modelu;
a wiêc \fBvt100\fR, \fBhp2621\fR, \fBwy50\fR.
.PP
Nazw± g³ówn± dla konsoli typu PC-Unix powinna byæ nazwa systemu
operacyjnego np. \fBlinux\fR, \fBbsdos\fR, \fBfreebsd\fB, \fBnetbsd\fR.
\fINie\fR powinna to byæ nazwa typu \fBconsole\fR czy jakakolwiek inna
ogólna nazwa która mo¿e spowodowaæ zamieszanie w ¶rodowisku o wielu
platformach. Je¶li pó¼niej nastêpuje numer modelu, powinien wskazywaæ albo
numer wersji systemu operacyjnego lub numer wersji sterownika konsoli.
.PP
Nazw± g³ówna dla emulatora terminala (zak³adaj±c ¿e nie pasuje do którego¶
ze standardu ANSI lub typu vt100) powinna byæ nazwa programu lub z ³atwo¶ci±
rozpoznawalny skrót (np. \fBversaterm\fR, \fBctrm\fR).
.PP
Po nazwie g³ównej, mo¿esz dodaæ dowoln± lecz rozs±dn± ilo¶æ rozdzielonych
³±cznikiem przyrostków okre¶laj±cych specjalne w³a¶ciwo¶ci.
.TP 5
2p
Ma dwie strony pamiêci.  Podobnie 4p, 8p, itd.
.TP 5
mc
Magic-cookie.  Niektóre terminale (szczególnie starsze Wyse) mog± wspieraæ
jedynie jeden atrybut bez utraty magic-cookie. Ich definicja w terminfo
zazwyczaj jest sparowana z inn± (która posiada ten przyrostek) aby wspieraæ
du¿± ilo¶æ atrybutów.
.TP 5
-am
W³±cza auto-margines (prawostronne zawijanie)
.TP 5
-m
Tryb mono - wy³±czenie wsparcia dla kolorów
.TP 5
-na
Bez strza³ek - termcap ignoruje strza³ki które w rzeczywisto¶ci s± na
terminalu, wiêc u¿ytkownik mo¿e u¿ywaæ ich lokalnie.
.TP 5
-nam
Bez auto-marginesu - Wy³±cz opcjê am
.TP 5
-nl
Bez etykiet - wy³±cz miêkkie etykiety
.TP 5
-nsl
Bez lini statusu - zlikwiduj liniê statusu
.TP 5
-pp
Ma port drukarki który jest u¿ywany
.TP 5
-rv
Terminal w odwróconym trybie video (czarny na bia³ym)
.TP 5
-s
U¿yj lini statusu.
.TP 5
-vb
U¿yj widzialnego dzwonka (b³ysk) a nie krótkiego dzwiêku.
.TP 5
-w
Szeroki; terminal jest w 132 kolumnowym trybie.
.PP
Standardowo, je¶li typ Twojego terminala jest jednym z wariantów, który ma za zadanie
okre¶liæ liczbê lini, przyrostek powinien znale¼æ siê tam pierwszy. Dla
hipotetycznego terminala FuBarCo model 2317 w 30-liniowym trybie z odwrotnym
wy¶wietlaniem (reverse video), lepsz± nazw± by³aby \fBfubar-30-rv\fR
(ni¿ np. `fubar-rv-30').
.PP
Typy terminali, które nie s± opisane jako samodzielne sekcje, a raczej jako
sk³adniki do do³±czenia do innych sekcji poprzez \fBuse\fR,
s± rozró¿niane poprzez u¿ycie znaków plus (+) a nie minus (-).
.PP
Komendy, które u¿ywaj± typu terminala aby kontrolowaæ wy¶wietlanie czêsto
akceptuj± opcjê -T, która pozwala podaæ typ terminala jako argument.
Takie programy powinny skorzystaæ ze zmiennej ¶rodowiskowej \fBTERM\fR
kiedy opcja -T jest nie podana.
.SH PRZENO¦NO¦Æ
Dla maksymalnej kompatybilno¶ci ze starymi systemami UNIXowymi V, nazwy i
aliasy powinny byæ unikalne w pierwszych 14 znakach.
.SH PLIKI
.TP 5
\*d/?/*
sk±pilowane pliki zawieraj±ce opisy terminali
.TP 5
/etc/inittab
inicjalizacja lini tyy (AT&T-podobne UNIXy).
.TP 5
/etc/ttys
inicjalizacja lini tty (BSD-podobne UNIXy).
.SH "ZOBACZ TAK¯E"
\fBcurses\fR(3X), \fBterminfo\fR(\*n), \fBterm\fR(\*d).
.\"#
.\"# The following sets edit modes for GNU EMACS
.\"# Local Variables:
.\"# mode:nroff
.\"# fill-column:79
.\"# End:
