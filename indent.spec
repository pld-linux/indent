Summary:	GNU C indenting program
Summary(de):	GNU C-Indenting-Programm  
Summary(fr):	Programme d'indentation C de GNU
Summary(pl):	GNU program formatuj±cy ¼ród³a w C
Summary(tr):	GNU C girintilendirme programý
Name:		indent
Version:	1.10.0
Release:	2
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source:		ftp://prep.ai.mit.edu/pub/gnu/indent/%{name}-%{version}.tar.gz
Patch0:		indent-info.patch
patch1:		indent-glibc21.patch
Prereq:		/sbin/install-info
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is the GNU indenting program. It is used to beautify C program source
files.

%description -l de
Das GNU-Indenting-Programm. Zur Verschönerung Ihrer
C-Programmquelldateienattraktiver aussehen!

%description -l fr
Programme d'indentation de GNU. Utilisé pour embellir les fichiers source C.

%description -l pl
GNU program formatuj±cy ¼ród³a w C. Wyrównuje wciêcia itp., tak ¿eby
kod ¼ród³owy ³adniej wygl±da³.

%description -l tr
Bu paket bir C programýnýn kaynak kodunu güzelleþtirmek için kullanýlýr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man1/*}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/indent.info.gz /etc/info-dir

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/indent.info.gz /etc/info-dir
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*
%{_mandir}/man1/*

%changelog
* Wed Jun 30 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10-2]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation  Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>.
