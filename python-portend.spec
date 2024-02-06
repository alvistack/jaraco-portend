# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-portend
Epoch: 100
Version: 3.1.0
Release: 1%{?dist}
BuildArch: noarch
Summary: TCP port monitoring and discovery
License: MIT
URL: https://github.com/jaraco/portend/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
por·tend pôrˈtend/ be a sign or warning that (something, especially
something momentous or calamitous) is likely to happen.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-portend
Summary: TCP port monitoring and discovery
Requires: python3
Requires: python3-tempora >= 1.8
Provides: python3-portend = %{epoch}:%{version}-%{release}
Provides: python3dist(portend) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-portend = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(portend) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-portend = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(portend) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-portend
por·tend pôrˈtend/ be a sign or warning that (something, especially
something momentous or calamitous) is likely to happen.

%files -n python%{python3_version_nodots}-portend
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-portend
Summary: TCP port monitoring and discovery
Requires: python3
Requires: python3-tempora >= 1.8
Provides: python3-portend = %{epoch}:%{version}-%{release}
Provides: python3dist(portend) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-portend = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(portend) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-portend = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(portend) = %{epoch}:%{version}-%{release}

%description -n python3-portend
por·tend pôrˈtend/ be a sign or warning that (something, especially
something momentous or calamitous) is likely to happen.

%files -n python3-portend
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
