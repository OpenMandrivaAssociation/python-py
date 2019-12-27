%define module	py

Summary:        Python development support library
Name:           python-%{module}
Version:	1.8.1
Release:	1
License:        MIT
Source0:	https://files.pythonhosted.org/packages/bd/8f/169d08dcac7d6e311333c96b63cbe92e7947778475e1a619b674989ba1ed/py-1.8.1.tar.gz
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
