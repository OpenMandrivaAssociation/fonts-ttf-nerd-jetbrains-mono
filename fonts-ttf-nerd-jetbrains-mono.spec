Name:           fonts-ttf-nerd-jetbrains-mono
Version:        3.3.0
Release:        1
Summary:        A mono-space font family containing coding ligatures
License:        OFL-1-1
Group:		    System/Fonts/True type
URL:            https://github.com/ryanoasis/nerd-fonts
Source:         https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/JetBrainsMono.tar.xz
BuildRequires:  fontpackages-devel
BuildArch:      noarch

%description
The JetBrains Mono project publishes developer-oriented font families.

Their forms are simple and free from unnecessary details. Rendered in small
sizes, the text looks crisper. The easier the forms, the faster the eye
perceives them and the less effort the brain needs to process them.

The shape of ovals approaches that of rectangular symbols. This makes the whole
pattern of the text more clear-Ñut. The outer sides of ovals ensure there are
no additional obstacles for your eyes as they scan the text vertically.

Characters remain standard in width, but the height of the lowercase is
maximized. This approach keeps code lines to the length that developers expect,
and it helps improve rendering since each letter occupies more pixels.

They use a 9Â° italic angle; this maintains the optimal contrast to minimize
distraction and eye strain. The usual angle is about 11Â°â€“12Â°.}

%prep
%autosetup -c

%build

%install
install -d %{buildroot}%{_datadir}/fonts %{buildroot}%{_docdir}/%{name} %{buildroot}%{_licensedir}/%{name}
install -m644 *.ttf %{buildroot}%{_datadir}/fonts
install -m644 README.md %{buildroot}%{_docdir}/%{name}
install -m644 OFL.txt %{buildroot}%{_licensedir}/%{name}

%files
%doc README.md
%{_datadir}/fonts/*
%{_datadir}/licenses/*
