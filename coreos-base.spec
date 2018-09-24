Name:           coreos-base
Version:        0.1
Release:        1%{?dist}
Summary:        Base scripts, systemd units, rules for Fedora CoreOS

License:
URL:            https://example.com/%{name}
Source0:        https://example.com/%{name}/release/%{name}-%{version}.tar.gz

BuildRequires:
Requires:       bash
Requires:       systemd

%description
%{summary}.

%package motdgen
Summary:        Message of the day generator files for Fedora CoreOS
Requires:       coreos-base
Requires:       bash
Requires:       systemd
Requires:       pam >= 1.3.1

%description motdgen
%{summary}.

%package issuegen
Summary:        Issue generator files for Fedora CoreOS
Requires:       coreos-base
Requires:       bash
Requires        systemd
Requires:       agetty

%description issuegen
%{summary}.

%package profile
Summary:        Profile script for Fedora CoreOS
Requires:       bash
Requires:       systemd

%description profile
%{summary}.

%prep
%setup -q

%build

%install

# Vendor-scoped directories
mkdir -p %{buildroot}%{_prefix}/lib/%{name}/issue.d
mkdir -p %{buildroot}%{_prefix}/lib/%{name}/motd.d
mkdir -p %{buildroot}/run/%{name}/issue.d
mkdir -p %{buildroot}/run/%{name}/motd.d
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/issue.d
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/motd.d
mkdir -p %{buildroot}%{_prefix}/share/%{name}

# External directories
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_tmpfilesdir}
mkdir -p %{buildroot}%{_prefix}/lib/udev/rules.d

# TODO: move files in current repo to better organized dirs
# TODO: once moved to new dirs, use * for things like base.issue
install -DpZm 0644 issuegen.path %{buildroot}%{_unitdir}/issuegen.path
install -DpZm 0644 issuegen.service %{buildroot}%{_unitdir}/issuegen.service
install -DpZm 0644 issuegen.conf %{buildroot}%{_tmpfilesdir}/issuegen.conf
install -DpZm 0644 motdgen.path %{buildroot}%{_unitdir}/motdgen.path
install -DpZm 0644 motdgen.service %{buildroot}%{_unitdir}/motdgen.service
install -DpZm 0644 motdgen.conf %{buildroot}%{_tmpfilesdir}/motdgen.conf
install -DpZm 0644 91-issuegen.rules %{buildroot}%{_prefix}/lib/udev/rules.d/91-issuegen.rules
install -DpZm 0644 coreos-profile.conf %{buildroot}%{_tmpfilesdir}/coreos-profile.conf

install -DpZm 0755 issuegen %{buildroot}%{_prefix}/lib/%{name}/issuegen
install -DpZm 0755 motdgen %{buildroot}%{_prefix}/lib/%{name}/motdgen
install -DpZm 0755 coreos-profile.sh %{buildroot}%{_prefix}/share/%{name}/coreos-profile.sh
install -DpZm 0644 base.issue %{buildroot}%{_prefix}/lib/%{name}/issue.d/base.issue

%files
%doc README.md
%license LICENSE
%dir %{_prefix}/lib/%{name}
%dir /run/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_prefix}/share/%{name}

%files issuegen
%{_unitdir}/issuegen.path
%{_unitdir}/issuegen.service
%{_tmpfilesdir}/issuegen.conf
%{_prefix}/lib/udev/rules.d/91-issuegen.rules
%{_prefix}/lib/%{name}/issuegen
%dir %{_prefix}/lib/%{name}/issue.d
%{_prefix}/lib/%{name}/issue.d/base.issue
%dir /run/%{name}/issue.d
%dir %{_sysconfdir}/%{name}/issue.d

%files motdgen
%{_unitdir}/motdgen.path
%{_unitdir}/motdgen.service
%{_tmpfilesdir}/motdgen.conf
%{_prefix}/lib/%{name}/motdgen
%dir %{_prefix}/lib/%{name}/motd.d
%dir /run/%{name}/motd.d
%dir %{_sysconfdir}/%{name}/motd.d

%files profile
%{_tmpfilesdir}/coreos-profile.conf
%{_prefix}/share/%{name}/coreos-profile.sh

%changelog
* Fri Sept 21 2018 Robert Fairley <rfairley@redhat.com> - 0.1
- Initial Package