.\" {PTM/LK/0.2/28-09-1998/"konwersja termcap do terminfo"}
.\" T³umaczenie: 28-09-1998 £ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
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
.\" IN NO EVENT SHALL THE ABOVE PRAWA AUTORSKIE HOLDERS BE LIABLE FOR ANY CLAIM,   *
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
'\" t
.TH captoinfo 1M ""
.ds n 5
.ds d /usr/share/terminfo
.SH NAZWA
captoinfo \- konwersja opisu terminali w formacie termcap do formatu terminfo
.SH SK£ADNIA
\fBcaptoinfo\fR [\fB-v\fIn\fR \fIszeroko¶æ\fR]  [\fB-V\fR] [\fB-1\fR]
[\fB-w\fR \fIszeroko¶æ\fR] \fIplik\fR ...
.SH OPIS
.B captoinfo
szuka w \fIpliku\fR opisu terminali w formacie \fBtermcap\fR. Dla ka¿dego
znalezionego opisu na standardowe wyj¶cie jest wypisywany odpowiednik tego
opisu w formacie \fBterminfo\fR. Parametry \fBtc\fR w formacie \fBtermcap\fR
s± przekszta³cane bezpo¶rednio na parametry \fBuse\fR formatu \fBterminfo\fR.

Je¿eli nazwa pliku nie zostanie podana w linii poleceñ, jest ona pobierana
ze zmiennej ¶rodowiskowej \fBTERMCAP\fR. Je¿eli w zmiennej \fBTERMCAP\fR
znajduje siê pe³na ¶cie¿ka do pliku, pobierane s± z niego jedynie dane
terminala opisywanego zmienn± ¶rodowiskow± \fBTERM\fR. Je¿eli zmienna
\fBTERMCAP\fR nie istnieje, czytany jest plik \fB\*d\fR.

.TP 5
\fB-v\fR
wypisz informacje na temat dzia³ania programu na standardowe wyj¶cie b³êdu.
.\" print out tracing information on standard error as the program runs.
.TP 5
\fB-V\fR
wypisz numer wersji programu na standardowe wyj¶cie b³êdu i zakoñcz dzia³anie.
.TP 5
\fB-1\fR
wypisuj po jednym polu w ka¿dej linii. W przeciwnym wypadku w ka¿dej linii
znajdzie siê kilka pól tak, aby nie przekroczyæ 60 znaków w linii.
.TP 5
\fB-w\fR
ustaw d³ugo¶æ linii na \fIszeroko¶æ\fR znaków.
.SH PLIKI
.TP 20
\*d
skompilowana baza danych o terminalach.
.SH KONWERSJA NIESTANDARDOWYCH OPISÓW MO¿LIWO¶CI TERMINALI
.PP
Czê¶æ przestarza³ych niestandardowych mo¿liwo¶ci zostanie przez
\fBcaptoinfo\fR automatycznie
przekszta³cona do standardowej postaci w formacie terminfo (SVr4/XSI Curses).
Po ka¿dej konwersji tego rodzaju program wypisze informacjê na standardowe
wyj¶cie b³êdów umo¿liwiaj±c u¿ytkownikowi sprawdzenie, czy nie dosz³o do
przypadkowej translacji przypadkowej warto¶ci lub b³êdu syntaktycznego.
.PP
.TS H
c c c c
c c c c
l l l l.
.\"Nonstd	Std	From	Terminfo
.\"name	name		capability
Niestand	Stand	Pochodzenie	Opis
nazwa	nazwa		terminfo
_
BO	mr	AT&T	enter_reverse_mode
CI	vi	AT&T	cursor_invisible
CV	ve	AT&T	cursor_normal
DS	mh	AT&T	enter_dim_mode
EE	me	AT&T	exit_attribute_mode	
FE	LF	AT&T	label_on
FL	LO	AT&T	label_off
XS	mk	AT&T	enter_secure_mode
EN	@7	XENIX	key_end
GE	ae	XENIX	exit_alt_charset_mode
GS	as	XENIX	enter_alt_charset_mode
HM	kh	XENIX	key_home
LD	kL	XENIX	key_dl
PD	kN	XENIX	key_npage
PN	po	XENIX	prtr_off
PS	pf	XENIX	prtr_on
PU	kP	XENIX	key_ppage
RT	@8	XENIX	kent
UP	ku	XENIX	kcuu1
KA	k;	Tek	key_f10
KB	F1	Tek	key_f11
KC	F2	Tek	key_f12
KD	F3	Tek	key_f13
KE	F4	Tek	key_f14
KF	F5	Tek	key_f15
BC	Sb	Tek	set_background
FC	Sf	Tek	set_foreground
HS	mh	Iris	enter_dim_mode
.TE
.PP
Plik termcap w sytemie XENIX zawiera³ opis zestawu rozszerzonych mo¿liwo¶ci
takich, jak rysowanie formularzy, korzystaj±cych ze znaków z górnej po³owy
zestawu ASCII na komputerach IBM PC. Oto one:
.PP
.TS H
c c
l l.
Cap	Graphic
_
G2	upper left 
G3	lower left 
G1	upper right 
G4	lower right 
GR	pointing right 
GL	pointing left 
GU	pointing up
GD	pointing down 
GH	horizontal line
GV	vertical line
GC	intersection
G6	upper left 
G7	lower left
G5	upper right
G8	lower right
Gr	tee pointing right
Gr	tee pointing left
Gu	tee pointing up
Gd	tee pointing down
Gh	horizontal line
Gv	vertical line
Gc	intersection
GG	acs magic cookie count
.TE
.PP
Je¿eli w opisie terminala pojawi siê jednoliniowy opis mo¿liwo¶ci, jest on
przekszta³cany do postaci ci±gu \fBacsc\fR. Opisy dwuliniowe oraz opisy
\fBGG\fR s± pomijane, za¶ program wypisuje komunikat ostrzegawczy.
.PP
System AIX firmy IBM posiada bazê terminfo opart± na terminfo systemu SVr1
niekompatybiln± z formatem SVr4. Nastêpuj±ce rozszerzenia systemu AIX s±
przekszta³cane automatycznie.
.PP
.TS
c c
l l.
IBM	XSI
_
ksel	kslt
kbtab	kcbt
font0	s0ds
font1	s1ds
font2	s2ds
font3	s3ds
.TE
.PP
Dodatkowo opis mo¿liwo¶ci \fBbox\fR charakterystyczny dla systemu AIX jest
automatycznie przekszta³cany do postaci ci±gu \fBacsc\fR.
.PP
Biblioteka terminfo Hewlett-Packarda obs³uguje dwie niestandardowe
mo¿liwo¶ci terminfo: \fBmeml\fR (blokada pamiêci) oraz \fBmemu\fR
(odblokowanie pamiêci). S± one pomijane i wysy³any jest komunikat
ostrzegawczy.
.SH UWAGI
Ten program jest w rzeczywisto¶ci dowi±zaniem do programu \fItic\fR(1M)
pracuj±cego w trybie \fI-I\fR.

Opcja \fI\-v\fP dzia³a nieco odmiennie ni¿ w SVr4. W systemie SVr4 aby
okre¶liæ poziom generowania informacji nale¿y tê opcjê powtórzyæ odpowiedni±
ilo¶æ razy.

.SH ZOBACZ TAK¯E
\fBcurses\fR(3X), \fBinfocmp\fR(1M), \fBterminfo\fR(\*n)
.SH AUTOR
Eric S. Raymond <esr@snark.thyrsus.com>
.\"#
.\"# The following sets edit modes for GNU EMACS
.\"# Local Variables:
.\"# mode:nroff
.\"# fill-column:79
.\"# End:
