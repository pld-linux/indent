Summary:     GNU C indenting program
Summary(de): GNU C-Indenting-Programm  
Summary(fr): Programme d'indentation C de GNU
Summary(pl): GNU program formatuj±cy ¼ród³a w C
Summary(tr): GNU C girintilendirme programý
Name:        indent
Version:     1.9.1
Release:     10
Copyright:   GPL
Group:       Development/Tools
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Prereq:      /sbin/install-info
BuildRoot:   /tmp/%{name}-%{root}-root

%description
This is the GNU indenting program.  It is used to beautify
C program source files.

%description -l de
Das GNU-Indenting-Programm. Zur Verschönerung Ihrer  
C-Programmquelldateienattraktiver aussehen! 

%description -l fr
Programme d'indentation de GNU. Utilisé pour embellir les
fichiers source C.

%description -l pl
Ten GNU program formatuje ¼ród³a w C, wyrównuje wciêcia itp., tak ¿eby
¼ród³o ³adniej wygl±da³o.

%description -l tr
Bu paket bir C programýnýn kaynak kodunu güzelleþtirmek için kullanýlýr.

%prep
%setup -q

%build
./configure --prefix=/usr
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,info,man/man1}

make prefix=$RPM_BUILD_ROOT/usr install
gzip -9nf $RPM_BUILD_ROOT/usr/info/*
install indent.1 $RPM_BUILD_ROOT/usr/man/man1

strip $RPM_BUILD_ROOT/usr/bin/indent

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/indent.info.gz /usr/info/dir \
	--entry="* indent: (indent).            Program to format source code."

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/info/indent.info.gz /usr/info/dir \
		--entry="* indent: (indent).            Program to format source code."
fi

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/*
/usr/info/*info*
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Sat Sep 26 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
  [1.9.1-10]
- use %{name} and %{version} macros,
- added full %attr description in %files,
- added pl translation,
- `mkdir -p' replaced with more standard `install -d',
- don't use TABs in info/dir entry.

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- use install-info

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
