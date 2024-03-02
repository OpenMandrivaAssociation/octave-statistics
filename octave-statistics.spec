%global octpkg statistics

Summary:	The Statistics package for GNU Octave
Name:		octave-statistics
Version:	1.6.4
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/statistics/
Url:		https://github.com/gnu-octave/statistics/
Source0:	https://github.com/gnu-octave/statistics/archive/refs/tags/release-%{version}/statistics-%{version}.tar.gz

BuildRequires:  octave-devel >= 6.1.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Additional statistics functions for Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-release-%{version}

%build
%set_build_flags
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

