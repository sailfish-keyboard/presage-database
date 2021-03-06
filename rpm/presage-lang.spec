Summary:        Presage language support
License:        MIT
Name:           presage-lang
Version:        21.07.17
Release:        1
Group:          System
URL:            https://github.com/sailfish-keyboard/presage-database
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch

%description
Empty package - do not install


%package de_DE
Summary:        Presage language support for German
License:        GPL-2.0 OR GPL-3.0

%description de_DE
%{summary}.

PackageName: Presage German
Icon: https://raw.githubusercontent.com/sailfish-keyboard/presage/master/resources/presage.png
Categories:
  - Office
  - Dictionary

%package en_US
Summary:        Presage language support for English US
License:        MIT and BSD

%description en_US
%{summary}.

PackageName: Presage English US
Icon: https://raw.githubusercontent.com/sailfish-keyboard/presage/master/resources/presage.png
Categories:
  - Office
  - Dictionary

%package es_ES
Summary:        Presage language support for Spanish (or Castilian)
License:        GPL-3.0 OR LGPL-3.0 OR MPL-1.1

%description es_ES
%{summary}.

PackageName: Presage Spanish
Icon: https://raw.githubusercontent.com/sailfish-keyboard/presage/master/resources/presage.png
Categories:
  - Office
  - Dictionary

%package et_EE
Summary:        Presage language support for Estonian
License:        LGPL-2.1

%description et_EE
%{summary}.

PackageName: Presage Estonian
Icon: https://raw.githubusercontent.com/sailfish-keyboard/presage/master/resources/presage.png
Categories:
  - Office
  - Dictionary

%package fi_FI
Summary:        Presage language support for Finnish
License:        Unknown

%description fi_FI
%{summary}.

PackageName: Presage Finnish
Icon: https://raw.githubusercontent.com/sailfish-keyboard/presage/master/resources/presage.png
Categories:
  - Office
  - Dictionary

%package hu_HU
Summary:        Presage language support for Hungarian
License:        GPL-2.0 OR LGPL-2.1 OR MPL-1.1

%description hu_HU
%{summary}.

PackageName: Presage Hungarian
Icon: https://raw.githubusercontent.com/sailfish-keyboard/presage/master/resources/presage.png
Categories:
  - Office
  - Dictionary

%package ru_RU
Summary:        Presage language support for Russian
License:        LGPL-3.0

%description ru_RU
%{summary}.

PackageName: Presage Russian
Icon: https://raw.githubusercontent.com/sailfish-keyboard/presage/master/resources/presage.png
Categories:
  - Office
  - Dictionary

%package sv_SE
Summary:        Presage language support for Swedish
License:        LGPL-3.0

%description sv_SE
%{summary}.

PackageName: Presage Swedish
Icon: https://raw.githubusercontent.com/sailfish-keyboard/presage/master/resources/presage.png
Categories:
  - Office
  - Dictionary

%prep
%setup -q -n %{name}-%{version}

%install

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/presage

cp -R databases/* $RPM_BUILD_ROOT%{_datadir}/presage

%files
%defattr(-,root,root,-)


%files de_DE
%defattr(-,root,root,-)
%{_datadir}/presage/database_de_DE


%files en_US
%defattr(-,root,root,-)
%{_datadir}/presage/database_en_US


%files es_ES
%defattr(-,root,root,-)
%{_datadir}/presage/database_es_ES


%files et_EE
%defattr(-,root,root,-)
%{_datadir}/presage/database_et_EE


%files fi_FI
%defattr(-,root,root,-)
%{_datadir}/presage/database_fi_FI


%files hu_HU
%defattr(-,root,root,-)
%{_datadir}/presage/database_hu_HU


%files ru_RU
%defattr(-,root,root,-)
%{_datadir}/presage/database_ru_RU


%files sv_SE
%defattr(-,root,root,-)
%{_datadir}/presage/database_sv_SE

