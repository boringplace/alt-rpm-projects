Name: hello_c
Version: 1.0.0
Release: alt1

Summary: Hello/C project summary

License: GPL
Group: Education
Url: https://github.com/boringplace/alt-rpm-projects

Source: %name-%version.tar.gz

%description
Hello/C project description

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot%_bindir
install %name %buildroot%_bindir

%files
%_bindir/%name

%changelog
