Name: python-geotypes
Version: 0.7.0
Release: 8
Summary: Library that implements the OpenGIS 

Source: http://initd.org/svn/psycopg/geotypes/releases/GeoTypes-%{version}.tar.gz 
URL: http://initd.org/tracker/psycopg/wiki
License: GPL
Group:		Development/Python
BuildRequires:  python-devel

%description
GeoTypes is a library that implements the OpenGIS Simple Features Specification
for SQL Geometric Object Model and provides parsers for storing and retrieving
these objects from Postgis. GeoTypes is an external project by RJT.

%prep
%setup -q -n GeoTypes-%{version} 

%install
python setup.py install --root=%{buildroot}

%clean

%files
%{py_puresitedir}/*



