%define module	py

Summary:        Python development support library
Name:           python-%{module}
Version:	1.9.0
Release:	2
License:        MIT
Source0:	https://files.pythonhosted.org/packages/97/a6/ab9183fe08f69a53d06ac0ee8432bc0ffbb3989c575cc69b73a0229a9a99/py-%{version}.tar.gz
Group:          Development/Python
Url:            http://pylib.org
BuildArch:		noarch
BuildRequires:  python-setuptools
BuildRequires:  python-setuptools_scm
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
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}
pushd doc
PYTHONPATH=../build/lib make html
popd

%files
%doc CHANGELOG LICENSE README.rst doc/_build/html
%{py_puresitedir}/py*
