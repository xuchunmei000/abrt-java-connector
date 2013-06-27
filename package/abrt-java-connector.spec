%global commit 239a2a669df420a40968f8c6f3290e9b4994251f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		abrt-java-connector
Version:	1.0.0
Release:	1%{?dist}
Summary:	JNI Agent library converting Java exceptions to ABRT problems

Group:		System Environment/Libraries
License:	GPLv2+
URL:		https://github.com/jfilak/abrt-java-connector
Source0:	https://github.com/jfilak/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:	cmake
BuildRequires:	libreport-devel
BuildRequires:	java-1.7.0-openjdk-devel

Requires:	abrt

%description
JNI library providing an agent capable to process both caught and uncaught
exceptions and transform them to ABRT problems


%prep
%setup -qn %{name}-%{commit}


%build
%cmake -DCMAKE_BUILD_TYPE=Release
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc LICENSE README AUTHORS
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format_java.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_formatdup_java.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/java_event.conf

# install only unversioned shared object because the package is a Java plugin
# and not a system library but unfortunately the library must be placed in ld
# library paths
%{_libdir}/lib%{name}.so


%check
make test


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig



%changelog
* Thu Jun 27 2013 Jakub Filak <jfilak@redhat.com> - 1.0.0-1
- Publicly releasable version

* Mon Jun 03 2013 Jakub Filak <jfilak@redhat.com> - 0.1.2-1
- Start versioning library
- Drop build dependency on abrt-devel

* Mon Jun 03 2013 Jakub Filak <jfilak@redhat.com> - 0.1.1-2
- Provide ABRT configuration

* Mon Jun 03 2013 Jakub Filak <jfilak@redhat.com> - 0.1.1-1
- New release

* Fri May 31 2013 Jakub Filak <jfilak@redhat.com> - 0.1.0-3
- Build with the library name same as the package name

* Fri May 31 2013 Jakub Filak <jfilak@redhat.com> - 0.1.0-2
- Build with ABRT enabled

* Fri May 31 2013 Jakub Filak <jfilak@redhat.com> - 0.1.0-1
- Initial version
