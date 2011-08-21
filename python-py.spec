%define module	py
%define name	python-%{module}
%define version	1.4.5
%define	release	%mkrel 1

Summary:        Python development support library
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        MIT
Source:         %{module}-%{version}.zip
Group:          Development/Python
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://pylib.org
BuildArch:	noarch
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
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST
pushd doc
PYTHONPATH=../build/lib make html
popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc CHANGELOG LICENSE README.txt doc/_build/html


