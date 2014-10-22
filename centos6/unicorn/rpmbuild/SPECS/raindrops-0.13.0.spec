# Generated from raindrops-0.13.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name raindrops
%define _unpackaged_files_terminate_build 0 
%define _missing_doc_files_terminate_build 0 

Name: rubygem-%{gem_name}
Version: 0.13.0
Release: 1%{?dist}
Summary: real-time stats for preforking Rack servers
Group: Development/Languages
License: Internal
URL: http://raindrops.bogomips.org/
Source0: %{gem_name}-%{version}.gem
###Requires: ruby(release)
Requires: ruby(abi) = 1.8
Requires: ruby(rubygems) 
###BuildRequires: ruby(release)
BuildRequires: ruby(abi) = 1.8
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel 
# BuildRequires: rubygem(aggregate) => 0.2
# BuildRequires: rubygem(aggregate) < 1
# BuildRequires: rubygem(io-extra) => 1.2
# BuildRequires: rubygem(io-extra) < 2
# BuildRequires: rubygem(io-extra) >= 1.2.3
# BuildRequires: rubygem(posix_mq) => 2.0
# BuildRequires: rubygem(posix_mq) < 3
# BuildRequires: rubygem(rack) => 1.2
# BuildRequires: rubygem(rack) < 2
# BuildRequires: rubygem(unicorn) >= 0.98
# BuildRequires: rubygem(wrongdoc) => 1.6.2
# BuildRequires: rubygem(wrongdoc) < 1.7
# BuildRequires: rubygem(wrongdoc) >= 1.6.2
Provides: rubygem(%{gem_name}) = %{version}

%description
Raindrops is a real-time stats toolkit to show statistics for Rack HTTP
servers.  It is designed for preforking servers such as Rainbows! and
Unicorn, but should support any Rack HTTP server under Ruby 2.0, 1.9,
1.8 and Rubinius on platforms supporting POSIX shared memory.  It may
also be used as a generic scoreboard for sharing atomic counters across
multiple processes.


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
%doc %{gem_instdir}/README
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/lib/raindrops.rb
%doc %{gem_instdir}/lib/raindrops/aggregate.rb
%doc %{gem_instdir}/lib/raindrops/aggregate/last_data_recv.rb
%doc %{gem_instdir}/lib/raindrops/aggregate/pmq.rb
%doc %{gem_instdir}/lib/raindrops/last_data_recv.rb
%doc %{gem_instdir}/lib/raindrops/linux.rb
%doc %{gem_instdir}/lib/raindrops/middleware.rb
%doc %{gem_instdir}/lib/raindrops/middleware/proxy.rb
%doc %{gem_instdir}/lib/raindrops/struct.rb
%doc %{gem_instdir}/lib/raindrops/watcher.rb
%doc %{gem_instdir}/ext/raindrops/raindrops.c
%doc %{gem_instdir}/ext/raindrops/linux_inet_diag.c
%doc %{gem_instdir}/ext/raindrops/linux_tcp_info.c

%changelog
* Wed Oct 22 2014 root <root@puppet-n01> - 0.13.0-1
- Initial package

