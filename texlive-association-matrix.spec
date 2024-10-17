Name:		texlive-association-matrix
Version:	64845
Release:	2
Summary:	LaTeX support for creating association matrices
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/association-matrix
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/association-matrix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/association-matrix.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows the creation of association matrices in an
clear and concise fashion, without having to deal with manually
generating and modifying the tables while working. All you have
to do is define the rows and the columns by their unique
identifier, and then specify which cells should be marked as
associated. Then, the \amxgenerate command generates a table
that shows in the cells with a blip (*) where the association
was added. The package depends on etoolbox, forloop, ifthen,
textcomp, and xparse.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/association-matrix
%doc %{_texmfdistdir}/doc/latex/association-matrix

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
