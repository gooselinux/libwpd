Name: libwpd
Summary: Library for reading and converting WordPerfect(tm) documents
Version: 0.8.14
Release: 4.1%{?dist}
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Group: System Environment/Libraries
URL: http://libwpd.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildRequires: glib2-devel >= 2.0.0, libgsf-devel >= 1.6.0

%description
Library that handles Word Perfect documents.

%package tools
Summary: Tools to transform WordPerfect Documents into other formats
Group: Applications/Publishing

%description tools
Tools to transform WordPerfect Documents into other formats.
Currently supported: html, raw, text.

%package devel
Requires: libwpd = %{version}-%{release}
Requires: glib2-devel >= 2.0.0, libgsf-devel >= 1.6.0, pkgconfig
Summary: Files for developing with libwpd
Group: Development/Libraries

%description devel
Includes and definitions for developing with libwpd.

%prep
%setup -q

%build
%configure --without-docs --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc CHANGES COPYING CREDITS README
%{_libdir}/*.so.*

%files tools
%defattr(-,root,root,-)
%{_bindir}/wpd2*

%files devel
%defattr(-,root,root,-)
%doc HACKING TODO
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%dir %{_includedir}/libwpd-0.8
%{_includedir}/libwpd-0.8/libwpd/

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.8.14-4.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.8.14-2
- Rebuild for provides

* Wed Feb 13 2008 Caolan McNamara <caolanm@redhat.com> - 0.8.14-1
- next version

* Mon Dec 17 2007 Caolan McNamara <caolanm@redhat.com> - 0.8.13-2
- strangely 0.8.13-1 never appeared in rawhide

* Thu Dec 13 2007 Caolan McNamara <caolanm@redhat.com> - 0.8.13-1
- next version

* Sat Oct 13 2007 Caolan McNamara <caolanm@redhat.com> - 0.8.12-1
- next version

* Fri Aug 24 2007 Caolan McNamara <caolanm@redhat.com> - 0.8.11-1
- next version

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 0.8.10-2
- clarify license

* Fri Jun 15 2007 Caolan McNamara <caolanm@redhat.com> - 0.8.10-1
- next version

* Sun Mar 27 2007 Caolan McNamara <caolanm@redhat.com> - 0.8.9-2
- Resolves: rhbz#233876: add unowned directory fix from Michael Schwendt 

* Fri Mar 16 2007 Caolan McNamara <caolanm@redhat.com> - 0.8.9-1
- next version

* Fri Feb 09 2007 Caolan McNamara <caolanm@redhat.com> - 0.8.8-2
- spec cleanups

* Thu Jan 11 2007 Caolan McNamara <caolanm@redhat.com> - 0.8.8-1
- next version

* Mon Oct 09 2006 Caolan McNamara <caolanm@redhat.com> - 0.8.7-1
- next version

* Mon Jul 17 2006 Caolan McNamara <caolanm@redhat.com> - 0.8.6-1
- next version

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.8.5-3.1
- rebuild

* Sun Jun 11 2006  Caolan McNamara <caolanm@redhat.com> 0.8.5-3
- add wp5nofontlistcrash

* Fri Jun 02 2006  Caolan McNamara <caolanm@redhat.com> 0.8.5-2
- build through brew

* Thu Jun 01 2006  Caolan McNamara <caolanm@redhat.com> 0.8.5-1
- next version

* Tue Mar 21 2006  Caolan McNamara <caolanm@redhat.com> 0.8.4-2
- rebuild for libgsf

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.8.4-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.8.4-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> 0.8.4-1.1
- rebuilt

* Fri Dec 02 2005 Caolan McNamara <caolanm@redhat.com> 0.8.4-1
- next version

* Fri Dec 02 2005 Caolan McNamara <caolanm@redhat.com> 0.8.3-2
- rebuild because of libgsf

* Tue Jun 28 2005 Caolan McNamara <caolanm@redhat.com> 0.8.3-1
- update to latest libwpd

* Tue Jun 28 2005 Caolan McNamara <caolanm@redhat.com> 0.8.2-2.fc5
- export to other formats twiddle

* Wed Jun 22 2005 Caolan McNamara <caolanm@redhat.com> 0.8.2-1
- bump to latest version

* Fri Apr 29 2005 Caolan McNamara <caolanm@redhat.com> 0.8.1-1
- bump to latest version kudos Fridrich Strba
- drop integrated patch

* Wed Apr  6 2005 Caolan McNamara <caolanm@redhat.com> 0.8.0-4
- add libwpd devel provided patch for endless loops on some wpd documents

* Wed Mar 30 2005 Caolan McNamara <caolanm@redhat.com> 0.8.0-3
- rh#152503# add some Requires for -devel package

* Wed Mar  2 2005 Caolan McNamara <caolanm@redhat.com> 0.8.0-2
- rebuild with gcc4

* Fri Feb 11 2005 Caolan McNamara <caolanm@redhat.com> 0.8.0-1
- new version

* Wed Feb 9 2005 Caolan McNamara <caolanm@redhat.com> 0.7.2-2
- rebuild

* Fri Jul 23 2004 Caolan McNamara <caolanm@redhat.com> 0.7.2-1
- bump to 0.7.2

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 19 2004 Jeremy Katz <katzj@redhat.com> - 0.7.1-1
- update to 0.7.1

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Dec 16 2003 Jeremy Katz <katzj@redhat.com> 0.6.6-1
- 0.6.6

* Tue Nov  4 2003 Jeremy Katz <katzj@redhat.com> 0.6.5-1
- 0.6.5

* Mon Sep 15 2003 Jeremy Katz <katzj@redhat.com> 0.6.2-1
- 0.6.2

* Sun Jul  6 2003 Jeremy Katz <katzj@redhat.com> 0.5.0-1
- initial build for Red Hat Linux, tweak accordingly

* Sat Apr 26 2003 Rui M. Seabra <rms@1407.org>
- Create rpm spec
