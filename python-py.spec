%define module	py

Summary:        Python development support library
Name:           python-%{module}
Version:	1.11.0
Release:	4
License:        MIT
Source0:	https://files.pythonhosted.org/packages/98/ff/fec109ceb715d2a6b4c4a85a61af3b40c723a961e8828319fbcb15b868dc/py-1.11.0.tar.gz
Group:          Development/Python
Url:            https://pylib.org
BuildArch:		noarch
BuildRequires:  python3dist(babel)
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
#pushd doc
#PYTHONPATH=../build/lib make html
#popd

%files
%doc LICENSE README.rst
%{py_puresitedir}/py*
