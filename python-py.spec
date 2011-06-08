%define module py

Name:           python-%{module}
Version:        0.9.2
Release:        %mkrel 1
License:        MIT
Source:         %{module}-%{version}.tar.gz
Group:          Development/Python
Summary:        Agile development and test support library
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://pypi.python.org/pypi/py
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
The py lib is a development support library featuring these tools and APIs:
    * py.test: cross-project testing tool with many advanced features
    * py.execnet: ad-hoc code distribution to SSH, Socket and local sub processes
    * py.magic.greenlet: micro-threads on standard CPython ("stackless-light") and PyPy
    * py.path: path abstractions over local and subversion files
    * py.code: dynamic code compile and traceback printing support

%prep
%setup -q -n %module-%version

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitearch}

%clean
rm -rf %buildroot

%files 
%defattr(-,root,root)
%doc CHANGELOG LICENSE README.txt
%{_bindir}/py*
%{python_sitearch}/*

