#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jsondiff
Version  : 1.3.0
Release  : 27
URL      : https://files.pythonhosted.org/packages/37/53/df2401ddcdc20289e715d3ab30080a0f286a897b6c9c6511bad869ee1ea1/jsondiff-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/37/53/df2401ddcdc20289e715d3ab30080a0f286a897b6c9c6511bad869ee1ea1/jsondiff-1.3.0.tar.gz
Summary  : Diff JSON and JSON-like structures in Python
Group    : Development/Tools
License  : MIT
Requires: pypi-jsondiff-bin = %{version}-%{release}
Requires: pypi-jsondiff-license = %{version}-%{release}
Requires: pypi-jsondiff-python = %{version}-%{release}
Requires: pypi-jsondiff-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: jsondiff
Provides: jsondiff-python
Provides: jsondiff-python3

%description
jsondiff
========
Diff JSON and JSON-like structures in Python.
Installation
------------

%package bin
Summary: bin components for the pypi-jsondiff package.
Group: Binaries
Requires: pypi-jsondiff-license = %{version}-%{release}

%description bin
bin components for the pypi-jsondiff package.


%package license
Summary: license components for the pypi-jsondiff package.
Group: Default

%description license
license components for the pypi-jsondiff package.


%package python
Summary: python components for the pypi-jsondiff package.
Group: Default
Requires: pypi-jsondiff-python3 = %{version}-%{release}

%description python
python components for the pypi-jsondiff package.


%package python3
Summary: python3 components for the pypi-jsondiff package.
Group: Default
Requires: python3-core
Provides: pypi(jsondiff)

%description python3
python3 components for the pypi-jsondiff package.


%prep
%setup -q -n jsondiff-1.3.0
cd %{_builddir}/jsondiff-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641449180
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jsondiff
cp %{_builddir}/jsondiff-1.3.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jsondiff/0439ac90b9812d0e46a14b9bc0d1a4fcbee071f6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jdiff
/usr/bin/jsondiff

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jsondiff/0439ac90b9812d0e46a14b9bc0d1a4fcbee071f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
