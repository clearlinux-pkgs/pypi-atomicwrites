#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : atomicwrites
Version  : 1.1.5
Release  : 16
URL      : http://pypi.debian.net/atomicwrites/atomicwrites-1.1.5.tar.gz
Source0  : http://pypi.debian.net/atomicwrites/atomicwrites-1.1.5.tar.gz
Summary  : Atomic file writes.
Group    : Development/Tools
License  : MIT
Requires: atomicwrites-python3
Requires: atomicwrites-license
Requires: atomicwrites-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
python-atomicwrites
        ===================

%package license
Summary: license components for the atomicwrites package.
Group: Default

%description license
license components for the atomicwrites package.


%package python
Summary: python components for the atomicwrites package.
Group: Default
Requires: atomicwrites-python3

%description python
python components for the atomicwrites package.


%package python3
Summary: python3 components for the atomicwrites package.
Group: Default
Requires: python3-core

%description python3
python3 components for the atomicwrites package.


%prep
%setup -q -n atomicwrites-1.1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529091292
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/atomicwrites
cp LICENSE %{buildroot}/usr/share/doc/atomicwrites/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/atomicwrites/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
