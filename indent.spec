Summary:	GNU C indenting program
Summary(cs):	Odsazovací program GNU C
Summary(da):	GNU C indenterings-program
Summary(de):	GNU C-Indenting-Programm
Summary(fi):	GNU:n sisennysohjelma
Summary(fr):	Programme d'indentation C de GNU
Summary(it):	Programma della GNU per l'indentazione dei sorgenti C
Summary(ja):	GNU C¥³¡¼¥ÉÀ°·Á¥×¥í¥°¥é¥à
Summary(pl):	GNU program formatuj±cy ¼ród³a w C
Summary(tr):	GNU C girintilendirme programý
Name:		indent
Version:	2.2.7
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	ftp://prep.ai.mit.edu/pub/gnu/indent/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
URL:		http://www.xs4all.nl/~carlo17/indent/
BuildRequires:	autoconf
BuildRequires:	automake
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

¤¢¤Ê¤¿¤¬ C
¤Ç¥×¥í¥°¥é¥ß¥ó¥°¤·¡¢¤Þ¤¿¼«Æ°¤Ç¥³¡¼¥É¤ÎÀ°·Á¤ò¤·¤¿¤¤¤Î¤Ç¤¢¤ì¤Ð
indent¥Ñ¥Ã¥±¡¼¥¸¤ò¥¤¥ó¥¹¥È¡¼¥ë¤·¤Æ¤¯¤À¤µ¤¤¡£

%description -l pl
GNU program formatuj±cy ¼ród³a w C, które po takiej czynno¶ci ³atwiej
siê czyta. Indent umo¿liwia tak¿e konwersjê miêdzy ró¿nymi stylami
zapisu kodu ¼ród³owego w C. Program ten rozumie poprawna sk³adniê kodu
¼ród³owego C i stara siê tak¿e formatowaæ tak¿e kod który jest
niepoprawny sk³adniowo.

%description -l tr
Bu paket bir C programýnýn kaynak kodunu güzelleþtirmek için
kullanýlýr.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal -I aclocal
autoconf
automake -a -c
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
%{_infodir}/*info*
%{_mandir}/man1/*
