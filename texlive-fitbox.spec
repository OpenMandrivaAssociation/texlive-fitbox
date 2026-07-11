%global tl_name fitbox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	Fit graphics on a page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fitbox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fitbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fitbox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fitbox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows a box (usually an \includegraphics box) to fit on the
page. It scales the box to the maximal allowed size within the user-set
limits. If there is not enough space on the page, the box is moved to
the next one.

