# Generated from unicorn-4.8.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name unicorn
%define _unpackaged_files_terminate_build 0 
%define _missing_doc_files_terminate_build 0 

Name: rubygem-%{gem_name}
Version: 4.8.3
Release: 1%{?dist}
Summary: Rack HTTP server for fast clients and Unix
Group: Development/Languages
License: Internal
URL: http://unicorn.bogomips.org/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
###Requires: ruby(release)
Requires: ruby(abi) = 1.8
Requires: ruby(rubygems) 
Requires: rubygem(rack) 
Requires: rubygem(kgio) => 2.6
Requires: rubygem(kgio) < 3
Requires: rubygem(raindrops) => 0.7
Requires: rubygem(raindrops) < 1
###BuildRequires: ruby(release)
BuildRequires: ruby(abi) = 1.8
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel 
# BuildRequires: rubygem(isolate) => 3.2
# BuildRequires: rubygem(isolate) < 4
# BuildRequires: rubygem(wrongdoc) => 1.8
# BuildRequires: rubygem(wrongdoc) < 2
Provides: rubygem(%{gem_name}) = %{version}

%description
\Unicorn is an HTTP server for Rack applications designed to only serve
fast clients on low-latency, high-bandwidth connections and take
advantage of features in Unix/Unix-like kernels.  Slow clients should
only be served by placing a reverse proxy capable of fully buffering
both the the request and response in between \Unicorn and slow clients.


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
%{_bindir}/unicorn
%{_bindir}/unicorn_rails
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/FAQ
%doc %{gem_instdir}/README
%doc %{gem_instdir}/TUNING
%doc %{gem_instdir}/PHILOSOPHY
%doc %{gem_instdir}/HACKING
%doc %{gem_instdir}/DESIGN
%doc %{gem_instdir}/CONTRIBUTORS
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/SIGNALS
%doc %{gem_instdir}/KNOWN_ISSUES
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/LATEST
%doc %{gem_instdir}/lib/unicorn.rb
%doc %{gem_instdir}/lib/unicorn/configurator.rb
%doc %{gem_instdir}/lib/unicorn/http_server.rb
%doc %{gem_instdir}/lib/unicorn/preread_input.rb
%doc %{gem_instdir}/lib/unicorn/stream_input.rb
%doc %{gem_instdir}/lib/unicorn/tee_input.rb
%doc %{gem_instdir}/lib/unicorn/util.rb
%doc %{gem_instdir}/lib/unicorn/oob_gc.rb
%doc %{gem_instdir}/lib/unicorn/worker.rb
%doc %{gem_instdir}/ISSUES
%doc %{gem_instdir}/Sandbox
%doc %{gem_instdir}/Links
%doc %{gem_instdir}/Application_Timeouts

%changelog
* Wed Oct 22 2014 root <root@puppet-n01> - 4.8.3-1
- Initial package

