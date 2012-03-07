#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	xhtml2pdf
Summary:	PDF generator using HTML and CSS
Name:		python-%{module}
Version:	0.0.3
Release:	0.1
License:	Apache License 2.0
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/x/xhtml2pdf/%{module}-%{version}.tar.gz
# Source0-md5:	13b0d6059b72c994473fddfa7a528451
URL:		http://pypi.python.org/pypi/xhtml2pdf/
BuildRequires:	python-ReportLab >= 2.2
BuildRequires:	python-distribute
BuildRequires:	python-html5lib >= 0.11.1
BuildRequires:	python-pyPdf >= 1.11
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML/CSS to PDF converter based on Python.

%prep
%setup -q -n %{module}-%{version}


%build
%{__python} setup.py build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/w3c
%{py_sitescriptdir}/%{module}/w3c/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
