%define version_oct6114_032 1.07.01
%define version_oct6114_064 1.05.01
%define version_oct6114_128 1.05.01
%define version_oct6114_256 1.05.01
%define version_tc400m MR6.12
%define version_vpmoct032 1.12.0
%define version_vpmadt032 1.07
%define version_hx8 2.06
%define version_te820 1.76
%define version_oct6126_128 01.07.04
%define version_a4a a0017
%define version_a4b d001e
%define version_a8a 1d0017
%define version_a8b 1f001e
%define version_te133 7a001e
%define version_te134 780017
%define version_te435 13001e
%define version_te436 10017

Summary: Firmware files for DAHDI
Name: dahdi-firmware
Version: 3.0.0
Release: 1%{dist}
License: GPL
Group: Utilities/System
#Source: %{name}-sources-%{aversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
URL: http://www.asterisk.org
Vendor: Digium.com
BuildRequires: wget
Obsoletes: dahdi-firmware-oct6114-032
Obsoletes: dahdi-firmware-oct6114-064
Obsoletes: dahdi-firmware-oct6114-128
Obsoletes: dahdi-firmware-oct6114-256
Obsoletes: dahdi-firmware-tc400m
Obsoletes: dahdi-firmware-vpmoct032
Obsoletes: dahdi-firmware-vpmadt032
Obsoletes: dahdi-firmware-hx8
Obsoletes: dahdi-firmware-te820
Obsoletes: dahdi-firmware-oct6126-128
Obsoletes: dahdi-firmware-a4a
Obsoletes: dahdi-firmware-a4b
Obsoletes: dahdi-firmware-a8a
Obsoletes: dahdi-firmware-a8b
Obsoletes: dahdi-firmware-te133
Obsoletes: dahdi-firmware-te134
Obsoletes: dahdi-firmware-te435
Obsoletes: dahdi-firmware-te436

%description
This is a collection of all firmware used in the open source DAHDI project.

%prep
wget -c http://downloads.openvox.cn/pub/firmwares/opvx-dahdi-fw-oct6114-032-%{version_oct6114_032}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-oct6114-064-%{version_oct6114_064}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-oct6114-128-%{version_oct6114_128}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-oct6114-256-%{version_oct6114_256}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-tc400m-%{version_tc400m}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-vpmoct032-%{version_vpmoct032}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-vpmadt032-%{version_vpmadt032}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-hx8-%{version_hx8}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-te820-%{version_te820}.tar.gz
wget -c http://www.allo.com/firmware/pri-card/OCT6-LEC-128.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-a4a-%{version_a4a}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-a4b-%{version_a4b}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-a8a-%{version_a8a}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-a8b-%{version_a8b}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-te133-%{version_te133}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-te134-%{version_te134}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-te435-%{version_te435}.tar.gz
wget -c http://downloads.digium.com/pub/telephony/firmware/releases/dahdi-fw-te436-%{version_te436}.tar.gz


%build

%install
mkdir -p $RPM_BUILD_ROOT/lib/firmware/

tar xof OCT6-LEC-128.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
rm -rf $RPM_BUILD_ROOT/lib/firmware/dahdi-fw-oct6114-128.bin
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-oct6126-128-%{version_oct6126_128}

tar xof opvx-dahdi-fw-oct6114-032-%{version_oct6114_032}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-oct6114-032-%{version_oct6114_032}

tar xof dahdi-fw-oct6114-064-%{version_oct6114_064}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-oct6114-064-%{version_oct6114_064}

tar xof dahdi-fw-oct6114-128-%{version_oct6114_128}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-oct6114-128-%{version_oct6114_128}

tar xof dahdi-fw-oct6114-256-%{version_oct6114_256}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-oct6114-256-%{version_oct6114_256}

tar xof dahdi-fw-tc400m-%{version_tc400m}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-tc400m-%{version_tc400m}

tar xof dahdi-fw-vpmoct032-%{version_vpmoct032}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-vpmoct032-%{version_vpmoct032}

tar xof dahdi-fw-vpmadt032-%{version_vpmadt032}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-vpmadt032-%{version_vpmadt032}

tar xof dahdi-fw-hx8-%{version_hx8}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-hx8-%{version_hx8}

tar xof dahdi-fw-te820-%{version_te820}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-te820-%{version_te820}

tar xof dahdi-fw-a4a-%{version_a4a}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-a4a-%{version_a4a}

tar xof dahdi-fw-a4b-%{version_a4b}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-a4b-%{version_a4b}

tar xof dahdi-fw-a8a-%{version_a8a}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-a8a-%{version_a8a}

tar xof dahdi-fw-a8b-%{version_a8b}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-a8b-%{version_a8b}

tar xof dahdi-fw-te133-%{version_te133}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-te133-%{version_te133}

tar xof dahdi-fw-te134-%{version_te134}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-te134-%{version_te134}

tar xof dahdi-fw-te435-%{version_te435}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-te435-%{version_te435}

tar xof dahdi-fw-te436-%{version_te436}.tar.gz -C $RPM_BUILD_ROOT/lib/firmware/
touch $RPM_BUILD_ROOT/lib/firmware/.dahdi-fw-te436-%{version_te436}

%clean
cd $RPM_BUILD_DIR
%{__rm} -rf %{name}-%{version}
%{__rm} -rf /var/log/%{name}-sources-%{version}-%{release}.make.err
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/lib/firmware/*
/lib/firmware/.dahdi*
