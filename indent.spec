Summary:	GNU C indenting program
Summary(cs):	Odsazovací program GNU C
Summary(da):	GNU C indenterings-program
Summary(de):	GNU C-Indenting-Programm
Summary(fi):	GNU:n sisennysohjelma
Summary(fr):	Programme d'indentation C de GNU
Summary(it):	Programma della GNU per l'indentazione dei sorgenti C
Summary(ja):	GNU C¥³¡¼¥ÉÀ°·Á¥×¥í¥°¥é¥à
Summary(pl):	GNU program formatuj±cy ¼ród³a w C
Summary(ru):	ðÒÏÇÒÁÍÍÁ GNU ÄÌÑ ÆÏÒÍÁÔÉÒÏ×ÁÎÉÑ ÉÓÈÏÄÎÙÈ ÔÅËÓÔÏ× ÎÁ C
Summary(tr):	GNU C girintilendirme programý
Summary(uk):	ðÒÏÇÒÁÍÁ GNU ÄÌÑ ÆÏÒÍÁÔÕ×ÁÎÎÑ ×ÉÈ¦ÄÎÉÈ ÔÅËÓÔ¦× ÎÁ C
Name:		indent
Version:	2.2.9
Release:	5
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/indent/%{name}-%{version}.tar.gz
# Source0-md5:	dcdbb163bef928306dee2a0cfc581c89
Patch0:		%{name}-info.patch
Patch1:		%{name}-po-fix.patch
Patch2:		%{name}-pl.po-update.patch
Patch3:		%{name}-zh_TW.patch
Patch4:		%{name}-make-jN.patch
URL:		http://home.hccnet.nl/d.ingamells/beautify.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Indent is a GNU program for beautifying C code, so that it is easier
to read. Indent can also convert from one C writing style to a
different one. Indent understands correct C syntax and tries to handle
incorrect C syntax.

%description -l cs
Toto je odsazovací program GNU. Pou¾ívá se ke zkrá¹lení zdrojových
souborù v programech C.

%description -l da
GNU indenterings-program. Det bruges til at få C kildetekster til at
se pænere (og mere læsbare) ud

%description -l de
Das GNU-Indenting-Programm. Zur Verschönerung Ihrer
C-Programmquelldateienattraktiver aussehen!

%description -l fi
Tämä on GNU:n sisennysohjelma. Sitä käytetään C-ohjelmakoodin
muotoiluun.

%description -l fr
Programme d'indentation de GNU. Utilisé pour embellir les fichiers
source C.

%description -l it
Questo e' un programma per l'indentazione della GNU. E' usato per
abbellire i file sorgenti in C dei programmi.

%description -l ja
Indent ¤Ï C ¤Î¥³¡¼¥É¤Î²ÄÆÉÀ­¤ò¾å¤²¤ë¤¿¤á¡¢Èþ¤·¤¯À°·Á¤¹¤ë¤¿¤á¤Î
GNU¥×¥í¥°¥é¥à¤Ç¤¹¡£ Indent ¤Ï ¤¢¤ë C ¤Îµ­½ÒÊýË¡¤«¤éÊÌ¤Îµ­½ÒÊýË¡¤Ø¤È
ÊÑ´¹¤¹¤ë¤³¤È¤¬¤Ç¤­¤Þ¤¹¡£ Indent ¤Ï¡¢Àµ¤·¤¤ C ¤Î¹½Ê¸¤òÍý²ò¤·¤Þ¤¹¡£
¤½¤·¤Æ¡¢´Ö°ã¤Ã¤¿¹½Ê¸¤â½èÍý¤·¤è¤¦¤È¤·¤Þ¤¹¡£

%description -l pl
GNU program formatuj±cy ¼ród³a w C, które po takiej czynno¶ci ³atwiej
siê czyta. Indent umo¿liwia tak¿e konwersjê miêdzy ró¿nymi stylami
zapisu kodu ¼ród³owego w C. Program ten rozumie poprawna sk³adniê kodu
¼ród³owego C i stara siê tak¿e formatowaæ tak¿e kod który jest
niepoprawny sk³adniowo.

%description -l ru
Indent - ÜÔÏ ÐÒÏÇÒÁÍÍÁ GNU ÄÌÑ ÐÒÉÄÁÎÉÑ ËÒÁÓÉ×ÏÓÔÉ ÉÓÈÏÄÎÙÍ ÔÅËÓÔÁÍ
ÐÒÏÇÒÁÍÍ ÎÁ ÑÚÙËÅ C, ÄÅÌÁÑ ÉÈ ÂÏÌÅÅ ÞÉÔÁÂÅÌØÎÙÍÉ. Indent ÍÏÖÅÔ ÔÁËÖÅ
ËÏÎ×ÅÒÔÉÒÏ×ÁÔØ ÔÅËÓÔÙ ÍÅÖÄÕ ÒÁÚÎÙÍÉ ÓÔÉÌÑÍÉ ÎÁÐÉÓÁÎÉÑ. ïÎ ÐÏÎÉÍÁÅÔ
ËÏÒÒÅËÔÎÙÊ C ÓÉÎÔÁËÓÉÓ É ÓÔÁÒÁÅÔÓÑ ÏÂÒÁÂÁÔÙ×ÁÔØ ÎÅËÏÒÒÅËÔÎÙÊ.

%description -l tr
Bu paket bir C programýnýn kaynak kodunu güzelleþtirmek için
kullanýlýr.

%description -l uk
Indent - ÃÅ ÐÒÏÇÒÁÍÁ GNU ÄÌÑ "ÐÒÉËÒÁÛÅÎÎÑ" ×ÉÈ¦ÄÎÉÈ ÔÅËÓÔ¦× ÐÒÏÇÒÁÍ ÎÁ
ÍÏ×¦ C Ú ÍÅÔÏÀ ÚÒÏÂÉÔÉ §È Â¦ÌØÛ ÞÉÔÁÂÅÌØÎÉÍÉ. Indent ÍÏÖÅ ÔÁËÏÖ
ËÏÎ×ÅÒÔÕ×ÁÔÉ ÔÅËÓÔÉ Í¦Ö Ò¦ÚÎÉÍÉ ÓÔÉÌÑÍÉ ÎÁÐÉÓÁÎÎÑ. ÷¦Î ÒÏÚÕÍ¦¤
ËÏÒÅËÔÎÉÊ C ÓÉÎÔÁËÓÉÓ ¦ ÎÁÍÁÇÁ¤ÔØÓÑ ÏÂÒÏÂÌÑÔÉ ÎÅËÏÒÅËÔÎÉÊ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mv -f po/zh_TW{.Big5,}.po

%build
%{__gettextize}
%{__aclocal} -I aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*.info*
%{_mandir}/man1/*
