%global octpkg statistics

Summary:	Additional statistics functions for Octave
Name:		octave-%{octpkg}
Version:	1.4.3
Release:	2
Url:		https://packages.octave.org/%{octpkg}/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+ and Public Domain
Group:		Sciences/Mathematics
BuildArch:	noarch

BuildRequires:	octave-devel >= 4.0.0
BuildRequires:	octave-io >= 1.0.18

Requires:	octave(api) = %{octave_api}

Requires:	octave-io >= 1.0.18
Requires(post): octave
Requires(postun): octave

%description
Additional statistics functions for Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

