Name:		texlive-fitbox
Version:	50088
Release:	1
Summary:	Fit graphics on a page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fitbox
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fitbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fitbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fitbox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows a box (usually an \includegraphics box) to
fit on the page. It scales the box to the maximal allowed size
within the user-set limits. If there is not enough space on the
page, the box is moved to the next one.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fitbox
%{_texmfdistdir}/tex/latex/fitbox
%doc %{_texmfdistdir}/doc/latex/fitbox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
