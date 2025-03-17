# TODO: Fix tests
# TODO: Fix dependencies for Python 3.x version
%bcond_with	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define 	module	xhtml2pdf
Summary:	PDF generator using HTML and CSS
Summary(pl.UTF-8):	Generator PDF używający HTML i CSS
Name:		python-%{module}
Version:	0.1a4
Release:	6
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/x/xhtml2pdf/xhtml2pdf-%{version}.tar.gz
# Source0-md5:	beb2d99bb99376a3a4f584599eacec23
URL:		https://pypi.org/project/xhtml2pdf/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-PyPDF2
BuildRequires:	python-ReportLab >= 2.2
BuildRequires:	python-distribute
BuildRequires:	python-html5lib >= 0.11.1
BuildRequires:	python-modules
BuildRequires:	python-pillow
%endif
BuildRequires:	rpm-pythonprov
%if %{with python3}
BuildRequires:	python3-PyPDF2
BuildRequires:	python3-html5lib >= 0.11.1
BuildRequires:	python3-modules
BuildRequires:	python3-pillow
BuildRequires:	python3-reportlab >= 2.2
%endif
Requires:	python-modules
# /usr/bin/xhtml2pdf needs python-setuptools
Requires:	python-setuptools
Obsoletes:	python-pisa
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
html2pdf converter using the ReportLab Toolkit, the HTML5lib and
pyPdf.

%description -l pl.UTF-8
Konwertor html2pdf używający narzędzi ReportLab, HTML5lib i pyPdf.

%package -n python3-%{module}
Summary:	PDF generator using HTML and CSS
Summary(pl.UTF-8):	Generator PDF używający HTML i CSS
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-pillow
Requires:	python3-setuptools

%description -n python3-%{module}
html2pdf converter using the ReportLab Toolkit, the HTML5lib and
pyPdf.

%description -n python3-%{module} -l pl.UTF-8
Konwertor html2pdf używający narzędzi ReportLab, HTML5lib i pyPdf.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
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
%doc README.rst
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/w3c
%{py_sitescriptdir}/%{module}/w3c/*.py[co]

%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
# TODO: files
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
