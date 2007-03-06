Summary:	GNU C indenting program
Summary(cs.UTF-8):	Odsazovací program GNU C
Summary(da.UTF-8):	GNU C indenterings-program
Summary(de.UTF-8):	GNU C-Indenting-Programm
Summary(fi.UTF-8):	GNU:n sisennysohjelma
Summary(fr.UTF-8):	Programme d'indentation C de GNU
Summary(it.UTF-8):	Programma della GNU per l'indentazione dei sorgenti C
Summary(ja.UTF-8):	GNU Cコード整形プログラム
Summary(pl.UTF-8):	GNU program formatujący źródła w C
Summary(ru.UTF-8):	Программа GNU для форматирования исходных текстов на C
Summary(tr.UTF-8):	GNU C girintilendirme programı
Summary(uk.UTF-8):	Програма GNU для форматування вихідних текстів на C
Name:		indent
Version:	2.2.9
Release:	8
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/indent/%{name}-%{version}.tar.gz
# Source0-md5:	dcdbb163bef928306dee2a0cfc581c89
Patch0:		%{name}-info.patch
Patch1:		%{name}-po-fix.patch
Patch2:		%{name}-pl.po-update.patch
Patch3:		%{name}-zh_TW.patch
Patch4:		%{name}-make-jN.patch
Patch5:		%{name}-overflow.patch
Patch6:		%{name}-gcc4.patch
URL:		http://mysite.freeserve.com/indent/beautify.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	tetex
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Indent is a GNU program for beautifying C code, so that it is easier
to read. Indent can also convert from one C writing style to a
different one. Indent understands correct C syntax and tries to handle
incorrect C syntax.

%description -l cs.UTF-8
Toto je odsazovací program GNU. Používá se ke zkrášlení zdrojových
souborů v programech C.

%description -l da.UTF-8
GNU indenterings-program. Det bruges til at få C kildetekster til at
se pænere (og mere læsbare) ud

%description -l de.UTF-8
Das GNU-Indenting-Programm. Zur Verschönerung Ihrer
C-Programmquelldateienattraktiver aussehen!

%description -l fi.UTF-8
Tämä on GNU:n sisennysohjelma. Sitä käytetään C-ohjelmakoodin
muotoiluun.

%description -l fr.UTF-8
Programme d'indentation de GNU. Utilisé pour embellir les fichiers
source C.

%description -l it.UTF-8
Questo e' un programma per l'indentazione della GNU. E' usato per
abbellire i file sorgenti in C dei programmi.

%description -l ja.UTF-8
Indent は C のコードの可読性を上げるため、美しく整形するための
GNUプログラムです。 Indent は ある C の記述方法から別の記述方法へと
変換することができます。 Indent は、正しい C の構文を理解します。
そして、間違った構文も処理しようとします。

%description -l pl.UTF-8
GNU program formatujący źródła w C, które po takiej czynności łatwiej
się czyta. Indent umożliwia także konwersję między różnymi stylami
zapisu kodu źródłowego w C. Program ten rozumie poprawna składnię kodu
źródłowego C i stara się także formatować także kod który jest
niepoprawny składniowo.

%description -l ru.UTF-8
Indent - это программа GNU для придания красивости исходным текстам
программ на языке C, делая их более читабельными. Indent может также
конвертировать тексты между разными стилями написания. Он понимает
корректный C синтаксис и старается обрабатывать некорректный.

%description -l tr.UTF-8
Bu paket bir C programının kaynak kodunu güzelleştirmek için
kullanılır.

%description -l uk.UTF-8
Indent - це програма GNU для "прикрашення" вихідних текстів програм на
мові C з метою зробити їх більш читабельними. Indent може також
конвертувати тексти між різними стилями написання. Він розуміє
коректний C синтаксис і намагається обробляти некоректний.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
