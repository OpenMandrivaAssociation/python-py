%define module	py
%define name	python-%{module}
%define version	1.4.10
%define	rel		1
%if %mdkversion < 201100
%define	release	%mkrel %rel
%else
%define	release	%rel
%endif

Summary:        Python development support library
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        MIT
Source:			http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.zip
Group:          Development/Python
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://pylib.org
BuildArch:		noarch
BuildRequires:  python-setuptools
BuildRequires:	python-sphinx

%description
The py lib is a development support library featuring these tools and
APIs:

* py.path: uniform local and svn path objects
* py.apipkg: explicit API control and lazy-importing
* py.iniconfig: easy parsing of .ini files
* py.code: dynamic code generation and introspection
* py.path: uniform local and svn path objects

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot}
pushd doc
PYTHONPATH=../build/lib make html
popd

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG LICENSE README.txt doc/_build/html
%py_sitedir/py*



%changelog
* Fri Oct 19 2012 Lev Givon <lev@mandriva.org> 1.4.10-1
+ Revision: 819088
- Update to 1.4.10.

* Fri Aug 31 2012 Lev Givon <lev@mandriva.org> 1.4.9-1
+ Revision: 816118
- Update to 1.4.9.

* Sun Jun 10 2012 Lev Givon <lev@mandriva.org> 1.4.8-1
+ Revision: 804316
- Update to 1.4.8.

* Thu Jan 12 2012 Lev Givon <lev@mandriva.org> 1.4.6-1
+ Revision: 760504
- Update to 1.4.6.

* Sun Aug 21 2011 Lev Givon <lev@mandriva.org> 1.4.5-1
+ Revision: 695926
- Update to 1.4.5.

* Thu Jul 21 2011 Lev Givon <lev@mandriva.org> 1.4.4-1
+ Revision: 690853
- Update to 1.4.4.

* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 0.9.2-1
+ Revision: 683264
- import python-py


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 0.9.2
- first release for Mandriva 

