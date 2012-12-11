Name: python-geotypes
Version: 0.7.0
Release: %mkrel 8
Summary: Library that implements the OpenGIS 
Source: http://initd.org/svn/psycopg/geotypes/releases/GeoTypes-%{version}.tar.gz 
URL: http://initd.org/tracker/psycopg/wiki
License: GPL
Group:		Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%py_requires -d

%description
GeoTypes is a library that implements the OpenGIS Simple Features Specification
for SQL Geometric Object Model and provides parsers for storing and retrieving
these objects from Postgis. GeoTypes is an external project by RJT.

%prep
%setup -q -n GeoTypes-%{version} 

%install
rm -rf %buildroot
python setup.py install --root=%buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%py_puresitedir/*



%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 0.7.0-8mdv2011.0
+ Revision: 593931
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.7.0-7mdv2010.0
+ Revision: 442126
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.7.0-6mdv2009.1
+ Revision: 323714
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.7.0-5mdv2009.0
+ Revision: 259617
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.7.0-4mdv2009.0
+ Revision: 247422
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.7.0-2mdv2008.1
+ Revision: 171059
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix no-buildroot-tag
- fix description-line-too-long

* Tue Dec 18 2007 Helio Chissini de Castro <helio@mandriva.com> 0.7.0-1mdv2008.1
+ Revision: 132671
- import python-geotypes


