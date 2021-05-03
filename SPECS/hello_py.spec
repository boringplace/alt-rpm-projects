Name: hello_py
Version: 1.0.0
Release: alt1

Summary: Hello/Python project summary

License: GPLv3+
Group: Education
Url: https://github.com/boringplace/alt-rpm-projects

BuildArch: noarch

Source: %name.py

%description
Hello/Python project description

%install
mkdir -p %buildroot%_bindir
install %SOURCE0 %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
