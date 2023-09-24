#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Use Database URLs in your Django Application
Summary(pl.UTF-8):	Korzystanie z URL-i do baz danych w aplikacji Django
Name:		python-dj_database_url
# keep 0.x here for python2 / django1..2 support
Version:	0.5.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/dj-database-url/
Source0:	https://files.pythonhosted.org/packages/source/d/dj-database-url/dj-database-url-%{version}.tar.gz
# Source0-md5:	eb9b3997e3a0ddfc38a25beef28f3b21
URL:		https://pypi.org/project/dj-database-url/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows to utilize the 12factor inspired DATABASE_URL
environment variable to configure Django application.

%description -l pl.UTF-8
Ten moduł pozwala na konfigurowanie aplikacji Django przy użyciu
zmiennej środowiskowej DATABASE_URL, zainspirowanej przez 12factor.

%package -n python3-dj_database_url
Summary:	Use Database URLs in your Django Application
Summary(pl.UTF-8):	Korzystanie z URL-i do baz danych w aplikacji Django
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-dj_database_url
This module allows to utilize the 12factor inspired DATABASE_URL
environment variable to configure Django application.

%description -n python3-dj_database_url -l pl.UTF-8
Ten moduł pozwala na konfigurowanie aplikacji Django przy użyciu
zmiennej środowiskowej DATABASE_URL, zainspirowanej przez 12factor.

%prep
%setup -q -n dj-database-url-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/dj_database_url.py[co]
%{py_sitescriptdir}/dj_database_url-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-dj_database_url
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/dj_database_url.py
%{py3_sitescriptdir}/__pycache__/dj_database_url.cpython-*.py[co]
%{py3_sitescriptdir}/dj_database_url-%{version}-py*.egg-info
%endif
