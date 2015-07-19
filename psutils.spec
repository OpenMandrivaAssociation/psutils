%define	debug_package	%nil

Summary:	PostScript utilities
Name:		psutils
Version:	p17
Release:	29
License:	BSD-like
Group:		Publishing
Url:		http://www.tardis.ed.ac.uk/~ajcd/psutils/index.html
Source0:	ftp://ftp.knackered.org/pub/psutils/%{name}-%{version}.tar.bz2
Patch0:		psutils-make.patch
Patch1:		psutils-maketext.patch
Requires:	perl

%description
psutils contains some utilities for manipulating PostScript documents.
Page selections and rearrangement are supported, including arrengement
into signatures for booklet printing, and page merging for n-up printing.

%prep
%setup -qn psutils
%apply_patches

%build
make -f Makefile.unix RPM_OPT_FLAGS="%{optflags}" CC=%{__cc} \
	BUILDROOT="%{buildroot}" PERL=%{_bindir}/perl

%install
mkdir -p %{buildroot}/usr/{bin,man,share/psutils}
make -f Makefile.unix install BUILDROOT="%{buildroot}"
strip %{buildroot}/%{_bindir}/{epsffit,psbook,psnup,psresize,pstops,psselect}
#move the man page
mv %{buildroot}/usr/man %{buildroot}/%{_datadir}

%files
%doc LICENSE README
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*
