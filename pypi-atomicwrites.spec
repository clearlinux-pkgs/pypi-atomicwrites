#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-atomicwrites
Version  : 1.4.0
Release  : 50
URL      : https://files.pythonhosted.org/packages/55/8d/74a75635f2c3c914ab5b3850112fd4b0c8039975ecb320e4449aa363ba54/atomicwrites-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/55/8d/74a75635f2c3c914ab5b3850112fd4b0c8039975ecb320e4449aa363ba54/atomicwrites-1.4.0.tar.gz
Summary  : Atomic file writes.
Group    : Development/Tools
License  : MIT
Requires: pypi-atomicwrites-license = %{version}-%{release}
Requires: pypi-atomicwrites-python = %{version}-%{release}
Requires: pypi-atomicwrites-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
python-atomicwrites
        ===================

%package license
Summary: license components for the pypi-atomicwrites package.
Group: Default

%description license
license components for the pypi-atomicwrites package.


%package python
Summary: python components for the pypi-atomicwrites package.
Group: Default
Requires: pypi-atomicwrites-python3 = %{version}-%{release}

%description python
python components for the pypi-atomicwrites package.


%package python3
Summary: python3 components for the pypi-atomicwrites package.
Group: Default
Requires: python3-core
Provides: pypi(atomicwrites)

%description python3
python3 components for the pypi-atomicwrites package.


%prep
%setup -q -n atomicwrites-1.4.0
cd %{_builddir}/atomicwrites-1.4.0
pushd ..
cp -a atomicwrites-1.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656357970
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-atomicwrites
cp %{_builddir}/atomicwrites-1.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-atomicwrites/a3aac54aa78ad47e5de996080c30f4bf57e39253
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-atomicwrites/a3aac54aa78ad47e5de996080c30f4bf57e39253

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
