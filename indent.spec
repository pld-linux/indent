Summary:	GNU C indenting program
Summary(cs):	Odsazovac� program GNU C
Summary(da):	GNU C indenterings-program
Summary(de):	GNU C-Indenting-Programm
Summary(fi):	GNU:n sisennysohjelma
Summary(fr):	Programme d'indentation C de GNU
Summary(it):	Programma della GNU per l'indentazione dei sorgenti C
Summary(pl):	GNU program formatuj�cy �r�d�a w C
Summary(tr):	GNU C girintilendirme program�
Name:		indent
Version:	2.2.5
Release:	5
License:	GPL
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	ftp://prep.ai.mit.edu/pub/gnu/indent/%{name}-%{version}.tar.gz
Patch0:		indent-info.patch
URL:		http://www.xs4all.nl/~carlo17/indent/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Indent is a GNU program for beautifying C code, so that it is easier
to read. Indent can also convert from one C writing style to a
different one. Indent understands correct C syntax and tries to handle
incorrect C syntax.

%description -l cs
Toto je odsazovac� program GNU. Pou��v� se ke zkr�len� zdrojov�ch
soubor� v programech C.

%description -l da
GNU indenterings-program. Det bruges til at f� C kildetekster til at
se p�nere (og mere l�sbare) ud

%description -l de
Das GNU-Indenting-Programm. Zur Versch�nerung Ihrer
C-Programmquelldateienattraktiver aussehen!

%description -l fi
T�m� on GNU:n sisennysohjelma. Sit� k�ytet��n C-ohjelmakoodin
muotoiluun.

%description -l fr
Programme d'indentation de GNU. Utilis� pour embellir les fichiers
source C.

%description -l it
Questo e' un programma per l'indentazione della GNU. E' usato per
abbellire i file sorgenti in C dei programmi.

%description -l pl
GNU program formatuj�cy �r�d�a w C, kt�re po takiej czynno�ci �atwiej
si� czyta. Indent umo�liwia tak�e konwersj� mi�dzy r�nymi stylami
zapisu kodu �r�d�owego w C. Program ten rozumie poprawna sk�adni� kodu
�r�d�owego C i stara si� tak�e formatowa� tak�e kod kt�ry jest
niepoprawny sk�adniowo.

%description -l tr
Bu paket bir C program�n�n kaynak kodunu g�zelle�tirmek i�in
kullan�l�r.

%prep
%setup -q
%patch0 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man1/*}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*
%{_mandir}/man1/*
