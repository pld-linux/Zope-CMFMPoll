%define		zope_subname	MPoll
Summary:	Sime cookie-based poll product based on Archetypes
Summary(pl.UTF-8):   Produkt bazujący na Archetypes umożliwiający dodanie pola do głosowań
Name:		Zope-CMF%{zope_subname}
Version:	0.3.1
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	bc8dd0f835e51a16a421e550bb4667f3
URL:		http://sourceforge.net/projects/collective/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMF
Requires:	Zope-archetypes
Conflicts:	CMF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sime cookie-based poll product based on Archetypes.

%description -l pl.UTF-8
Produkt bazujący na Archetypes umożliwiający dodanie pola do głosowań.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,i18n,skins,*.py,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc HISTORY.txt README.txt LICENSE.txt
%{_datadir}/%{name}
