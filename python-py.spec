%define module	py

Summary:        Python development support library
Name:           python-%{module}
Version:	1.8.0
Release:	2
License:        MIT
Source0:	https://files.pythonhosted.org/packages/f1/5a/87ca5909f400a2de1561f1648883af74345fe96349f34f737cdfc94eba8c/py-1.8.0.tar.gz
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
