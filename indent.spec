Summary:	GNU C indenting program
Summary(cs):	Odsazovac� program GNU C
Summary(da):	GNU C indenterings-program
Summary(de):	GNU C-Indenting-Programm
Summary(fi):	GNU:n sisennysohjelma
Summary(fr):	Programme d'indentation C de GNU
Summary(it):	Programma della GNU per l'indentazione dei sorgenti C
Summary(ja):	GNU C�����������ץ����
Summary(pl):	GNU program formatuj�cy �r�d�a w C
Summary(tr):	GNU C girintilendirme program�
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

%description -l ja
Indent �� C �Υ����ɤβ�������夲�뤿�ᡢ�������������뤿���
GNU�ץ����Ǥ��� Indent �� ���� C �ε�����ˡ�����̤ε�����ˡ�ؤ�
�Ѵ����뤳�Ȥ��Ǥ��ޤ��� Indent �ϡ������� C �ι�ʸ�����򤷤ޤ���
�����ơ��ְ�ä���ʸ��������褦�Ȥ��ޤ���

���ʤ��� C
�ǥץ���ߥ󥰤����ޤ���ư�ǥ����ɤ������򤷤����ΤǤ����
indent�ѥå������򥤥󥹥ȡ��뤷�Ƥ���������

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
