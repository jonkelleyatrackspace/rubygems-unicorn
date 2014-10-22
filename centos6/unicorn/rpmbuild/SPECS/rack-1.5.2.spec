# Generated from rack-1.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rack
%define _unpackaged_files_terminate_build 0 
%define _missing_doc_files_terminate_build 0 

Name: rubygem-%{gem_name}
Version: 1.5.2
Release: 1%{?dist}
Summary: a modular Ruby webserver interface
Group: Development/Languages
License: Internal
URL: http://rack.github.com/
Source0: %{gem_name}-%{version}.gem
###Requires: ruby(release)
Requires: ruby(abi) = 1.8
Requires: ruby(rubygems) 
###BuildRequires: ruby(release)
BuildRequires: ruby(abi) = 1.8
BuildRequires: rubygems-devel 
BuildRequires: ruby 
# BuildRequires: rubygem(bacon) 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Rack provides a minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.
Also see http://rack.github.com/.


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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{_bindir}/rackup
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/KNOWN-ISSUES

%changelog
* Wed Oct 22 2014 root <root@puppet-n01> - 1.5.2-1
- Initial package

