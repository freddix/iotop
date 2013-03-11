Summary:	Top like utility for I/O
Name:		iotop
Version:	0.5
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.bz2
# Source0-md5:	b0846ad976f41bca2813f7f8a73fef31
URL:		http://guichaz.free.fr/iotop/
%pyrequires_eq	python-modules
BuildRequires:	python-devel
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux has always been able to show how much I/O was going on (the bi
and bo columns of the vmstat 1 command). iotop is a Python program
with a top like UI used to show of behalf of which process is the I/O
going on.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__python} setup.py install			\
        --optimize 2				\
        --root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS THANKS
%attr(755,root,root) %{_bindir}/iotop
%{py_sitescriptdir}/iotop
%{py_sitescriptdir}/*.egg-info
%{_mandir}/man8/iotop.8*

