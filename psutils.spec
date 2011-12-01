Summary:	PostScript utilities
Name:		psutils
Version:	p17
Release:	%mkrel 18

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
	BUILDROOT="%{buildroot}" PERL=%{_bindir}/perl

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/{bin,man,share/psutils}
make -f Makefile.unix install BUILDROOT="%{buildroot}"
strip %{buildroot}/%_bindir/{epsffit,psbook,psnup,psresize,pstops,psselect}
#move the man page
mv %{buildroot}/usr/man %{buildroot}/%_datadir

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc LICENSE README
%attr(755,root,root) %_bindir/*
%dir %_datadir/%{name}
%_mandir/man1/*
%_datadir/%{name}/*


