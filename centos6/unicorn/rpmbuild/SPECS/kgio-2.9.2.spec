# Generated from kgio-2.9.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name kgio
%define _unpackaged_files_terminate_build 0 
%define _missing_doc_files_terminate_build 0 

Name: rubygem-%{gem_name}
Version: 2.9.2
Release: 1%{?dist}
Summary: kinder, gentler I/O for Ruby
Group: Development/Languages
License: Internal
URL: http://bogomips.org/kgio/
Source0: %{gem_name}-%{version}.gem
###Requires: ruby(release)
Requires: ruby(abi) = 1.8
Requires: ruby(rubygems) 
###BuildRequires: ruby(release)
BuildRequires: ruby(abi) = 1.8
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel 
Provides: rubygem(%{gem_name}) = %{version}

%description
kgio provides non-blocking I/O methods for Ruby without raising
exceptions on EAGAIN and EINPROGRESS.  It is intended for use with the
Unicorn and Rainbows! Rack servers, but may be used by other
applications (that run on Unix-like platforms).


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}/lib

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/



# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/LATEST
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/ISSUES
%doc %{gem_instdir}/HACKING
%doc %{gem_instdir}/lib/kgio.rb
%doc %{gem_instdir}/ext/kgio/accept.c
%doc %{gem_instdir}/ext/kgio/autopush.c
%doc %{gem_instdir}/ext/kgio/connect.c
%doc %{gem_instdir}/ext/kgio/kgio_ext.c
%doc %{gem_instdir}/ext/kgio/poll.c
%doc %{gem_instdir}/ext/kgio/wait.c
%doc %{gem_instdir}/ext/kgio/tryopen.c

%changelog
* Wed Oct 22 2014 root <root@puppet-n01> - 2.9.2-1
- Initial package

