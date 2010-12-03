Summary:	PostScript utilities
Name:		psutils
Version:	p17
Release:	%mkrel 17

URL:		http://www.tardis.ed.ac.uk/~ajcd/psutils/index.html
Source0:	ftp://ftp.knackered.org/pub/psutils/%{name}-%{version}.tar.bz2
Patch0:		psutils-make.patch
Patch1:		psutils-maketext.patch

License:	BSD-like
Group:		Publishing
BuildRoot:	%_tmppath/%name-%version-%release-root
Requires:	perl

%description
psutils contains some utilities for manipulating PostScript documents.
Page selections and rearrangement are supported, including arrengement
into signatures for booklet printing, and page merging for n-up printing.

%prep

%setup -q -n psutils
%patch0 -p1
%patch1 -p1

%build
make -f Makefile.unix RPM_OPT_FLAGS="$RPM_OPT_FLAGS" \
	BUILDROOT="$RPM_BUILD_ROOT" PERL=%{_bindir}/perl

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man,share/psutils}
make -f Makefile.unix install BUILDROOT="$RPM_BUILD_ROOT"
strip $RPM_BUILD_ROOT/%_bindir/{epsffit,psbook,psnup,psresize,pstops,psselect}
#move the man page
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/%_datadir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc LICENSE README
%attr(755,root,root) %_bindir/*
%dir %_datadir/%{name}
%_mandir/man1/*
%_datadir/%{name}/*


