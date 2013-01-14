%define	debug_package	%nil
Summary:	PostScript utilities
Name:		psutils
Version:	p17
Release:	21

URL:		http://www.tardis.ed.ac.uk/~ajcd/psutils/index.html
Source0:	ftp://ftp.knackered.org/pub/psutils/%{name}-%{version}.tar.bz2
Patch0:		psutils-make.patch
Patch1:		psutils-maketext.patch

License:	BSD-like
Group:		Publishing
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
mkdir -p %{buildroot}/usr/{bin,man,share/psutils}
make -f Makefile.unix install BUILDROOT="$RPM_BUILD_ROOT"
strip %{buildroot}/%{_bindir}/{epsffit,psbook,psnup,psresize,pstops,psselect}
#move the man page
mv %{buildroot}/usr/man %{buildroot}/%{_datadir}

%files
%defattr(-,root,root,0755)
%doc LICENSE README
%attr(755,root,root) %_bindir/*
%dir %_datadir/%{name}
%_mandir/man1/*
%_datadir/%{name}/*




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> p17-18mdv2011.0
+ Revision: 667896
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> p17-17mdv2011.0
+ Revision: 607230
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> p17-16mdv2010.1
+ Revision: 520205
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> p17-15mdv2010.0
+ Revision: 426787
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> p17-14mdv2009.1
+ Revision: 351592
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> p17-13mdv2009.0
+ Revision: 225110
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> p17-12mdv2008.1
+ Revision: 179366
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Adam Williamson <awilliamson@mandriva.org> p17-11mdv2008.0
+ Revision: 73311
- correct license (#32876)


* Sun Jan 28 2007 Olivier Thauvin <nanardon@mandriva.org> p17-10mdv2007.0
+ Revision: 114737
- mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> p17-9mdk
- Rebuild

