#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-diffusionMap
Version  : 1.1.0
Release  : 3
URL      : https://cran.r-project.org/src/contrib/diffusionMap_1.1-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/diffusionMap_1.1-0.tar.gz
Summary  : Diffusion map
Group    : Development/Tools
License  : GPL-2.0
Requires: R-igraph
Requires: R-scatterplot3d
BuildRequires : R-igraph
BuildRequires : R-scatterplot3d
BuildRequires : clr-R-helpers

%description
parametrization, including creation and visualization of
          diffusion map, clustering with diffusion K-means and
	  regression using adaptive regression model.

%prep
%setup -q -c -n diffusionMap

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523301660

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523301660
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diffusionMap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diffusionMap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diffusionMap
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library diffusionMap|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/diffusionMap/DESCRIPTION
/usr/lib64/R/library/diffusionMap/INDEX
/usr/lib64/R/library/diffusionMap/Meta/Rd.rds
/usr/lib64/R/library/diffusionMap/Meta/data.rds
/usr/lib64/R/library/diffusionMap/Meta/features.rds
/usr/lib64/R/library/diffusionMap/Meta/hsearch.rds
/usr/lib64/R/library/diffusionMap/Meta/links.rds
/usr/lib64/R/library/diffusionMap/Meta/nsInfo.rds
/usr/lib64/R/library/diffusionMap/Meta/package.rds
/usr/lib64/R/library/diffusionMap/NAMESPACE
/usr/lib64/R/library/diffusionMap/R/diffusionMap
/usr/lib64/R/library/diffusionMap/R/diffusionMap.rdb
/usr/lib64/R/library/diffusionMap/R/diffusionMap.rdx
/usr/lib64/R/library/diffusionMap/data/Chainlink.txt.gz
/usr/lib64/R/library/diffusionMap/data/annulus.txt.gz
/usr/lib64/R/library/diffusionMap/help/AnIndex
/usr/lib64/R/library/diffusionMap/help/aliases.rds
/usr/lib64/R/library/diffusionMap/help/diffusionMap.rdb
/usr/lib64/R/library/diffusionMap/help/diffusionMap.rdx
/usr/lib64/R/library/diffusionMap/help/paths.rds
/usr/lib64/R/library/diffusionMap/html/00Index.html
/usr/lib64/R/library/diffusionMap/html/R.css
