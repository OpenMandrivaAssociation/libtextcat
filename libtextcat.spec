%define lname textcat
%define major 0
%define libname %mklibname %{lname} %{major}
%define develname %mklibname %{lname} -d

Summary:	Text categorization library
Name:		libtextcat
Version:	2.2
%define subrel 1
Release:	%mkrel 10
Group:		System/Libraries
License:	BSD
Source0:	http://software.wise-guys.nl/download/%{name}-%{version}.tar.bz2
Source1:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/fpdb.conf
Source2:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/chinese_simplified.lm
Source3:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/chinese_traditional.lm
Source4:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/japanese.lm
Source5:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/luxembourgish.lm
Source6:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/mongolian_cyrillic.lm
Source7:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/zulu.lm
URL:		http://software.wise-guys.nl/libtextcat
Patch0:		libtextcat-2.2-exportapi.patch
Patch1:		libtextcat-2.2-OOo.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Libtextcat is a library with functions that implement the classification
technique described in Cavnar & Trenkle, "N-Gram-Based Text Categorization".
It was primarily developed for language guessing, a task on which it is known
to perform with near-perfect accuracy.

%package -n	%{libname}
Summary:	Text categorization library
Group:		System/Libraries

%description -n	%{libname}
Libtextcat is a library with functions that implement the classification
technique described in Cavnar & Trenkle, "N-Gram-Based Text Categorization".
It was primarily developed for language guessing, a task on which it is known
to perform with near-perfect accuracy.

%package -n	%{develname}
Summary:	Development files and headers for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{lname}-devel = %{version}-%{release}

%description -n	%{develname}
Development files and headers for %{name}.

%prep
%setup -q
%patch0 -p1 -b .exportapi.patch~
%patch1 -p1 -b .ooo.patch~

%build
autoreconf -f -i
CFLAGS="%{optflags} -O3" \
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

mkdir -p %{buildroot}%{_datadir}/libtextcat

cp -p %{SOURCE1} %{buildroot}%{_datadir}/libtextcat
cd langclass/LM
cp -p amharic-utf.lm %{buildroot}%{_datadir}/libtextcat/amharic_utf.lm
cp -p yiddish-utf.lm %{buildroot}%{_datadir}/libtextcat/yiddish_utf.lm
cp -p afrikaans.lm %{buildroot}%{_datadir}/libtextcat/afrikaans.lm
cp -p basque.lm %{buildroot}%{_datadir}/libtextcat/basque.lm
cp -p bosnian.lm %{buildroot}%{_datadir}/libtextcat/bosnian.lm
cp -p croatian-ascii.lm %{buildroot}%{_datadir}/libtextcat/croatian.lm
cp -p drents.lm %{buildroot}%{_datadir}/libtextcat/drents.lm
cp -p dutch.lm %{buildroot}%{_datadir}/libtextcat/dutch.lm
cp -p english.lm %{buildroot}%{_datadir}/libtextcat/english.lm
cp -p icelandic.lm %{buildroot}%{_datadir}/libtextcat/icelandic.lm
cp -p indonesian.lm %{buildroot}%{_datadir}/libtextcat/indonesian.lm
cp -p latin.lm %{buildroot}%{_datadir}/libtextcat/latin.lm
cp -p malay.lm %{buildroot}%{_datadir}/libtextcat/malay.lm
cp -p manx.lm %{buildroot}%{_datadir}/libtextcat/manx_gaelic.lm
cp -p marathi.lm %{buildroot}%{_datadir}/libtextcat/marathi.lm
cp -p nepali.lm %{buildroot}%{_datadir}/libtextcat/nepali.lm
cp -p romanian.lm %{buildroot}%{_datadir}/libtextcat/romanian.lm
cp -p sanskrit.lm %{buildroot}%{_datadir}/libtextcat/sanskrit.lm
cp -p scots.lm %{buildroot}%{_datadir}/libtextcat/scots.lm
cp -p serbian-ascii.lm %{buildroot}%{_datadir}/libtextcat/serbian_ascii.lm
cp -p slovak-ascii.lm %{buildroot}%{_datadir}/libtextcat/slovak_ascii.lm
cp -p swahili.lm %{buildroot}%{_datadir}/libtextcat/swahili.lm
cp -p tagalog.lm %{buildroot}%{_datadir}/libtextcat/tagalog.lm
cp -p welsh.lm %{buildroot}%{_datadir}/libtextcat/welsh.lm
iconv -f WINDOWS-1256 -t UTF-8 arabic-windows1256.lm > %{buildroot}%{_datadir}/libtextcat/arabic.lm
iconv -f ISO-8859-1 -t UTF-8 albanian.lm > %{buildroot}%{_datadir}/libtextcat/albanian.lm
iconv -f WINDOWS-1251 -t UTF-8 belarus-windows1251.lm > %{buildroot}%{_datadir}/libtextcat/belarus.lm
iconv -f ISO-8859-1 -t UTF-8 breton.lm > %{buildroot}%{_datadir}/libtextcat/breton.lm
iconv -f ISO-8859-1 -t UTF-8 catalan.lm > %{buildroot}%{_datadir}/libtextcat/catalan.lm
iconv -f ISO-8859-2 -t UTF-8 czech-iso8859_2.lm > %{buildroot}%{_datadir}/libtextcat/czech.lm
iconv -f ISO-8859-1 -t UTF-8 danish.lm > %{buildroot}%{_datadir}/libtextcat/danish.lm
iconv -f ISO-8859-3 -t UTF-8 esperanto.lm > %{buildroot}%{_datadir}/libtextcat/esperanto.lm
iconv -f ISO-8859-15 -t UTF-8 estonian.lm > %{buildroot}%{_datadir}/libtextcat/estonian.lm
iconv -f ISO-8859-1 -t UTF-8 finnish.lm > %{buildroot}%{_datadir}/libtextcat/finnish.lm
iconv -f ISO-8859-1 -t UTF-8 french.lm > %{buildroot}%{_datadir}/libtextcat/french.lm
iconv -f ISO-8859-1 -t UTF-8 frisian.lm > %{buildroot}%{_datadir}/libtextcat/frisian.lm
iconv -f ISO-8859-1 -t UTF-8 georgian.lm > %{buildroot}%{_datadir}/libtextcat/georgian.lm
iconv -f ISO-8859-1 -t UTF-8 german.lm > %{buildroot}%{_datadir}/libtextcat/german.lm
iconv -f ISO-8859-7 -t UTF-8 greek-iso8859-7.lm > %{buildroot}%{_datadir}/libtextcat/greek.lm
iconv -f ISO-8859-8 -t UTF-8 hebrew-iso8859_8.lm > %{buildroot}%{_datadir}/libtextcat/hebrew.lm
iconv -f ISO-8859-2 -t UTF-8 hungarian.lm > %{buildroot}%{_datadir}/libtextcat/hungarian.lm
iconv -f ISO-8859-1 -t UTF-8 irish.lm > %{buildroot}%{_datadir}/libtextcat/irish_gaelic.lm
iconv -f ISO-8859-1 -t UTF-8 italian.lm > %{buildroot}%{_datadir}/libtextcat/italian.lm
iconv -f ISO-8859-13 -t UTF-8 latvian.lm > %{buildroot}%{_datadir}/libtextcat/latvian.lm
iconv -f ISO-8859-13 -t UTF-8 lithuanian.lm > %{buildroot}%{_datadir}/libtextcat/lithuanian.lm
iconv -f ISO-8859-1 -t UTF-8 malay.lm > %{buildroot}%{_datadir}/libtextcat/malay.lm
iconv -f ISO-8859-1 -t UTF-8 middle_frisian.lm > %{buildroot}%{_datadir}/libtextcat/middle_frisian.lm
iconv -f ISO-8859-1 -t UTF-8 mingo.lm > %{buildroot}%{_datadir}/libtextcat/mingo.lm
iconv -f ISO-8859-1 -t UTF-8 norwegian.lm > %{buildroot}%{_datadir}/libtextcat/norwegian.lm
iconv -f ISO-8859-2 -t UTF-8 polish.lm > %{buildroot}%{_datadir}/libtextcat/polish.lm
iconv -f ISO-8859-1 -t UTF-8 portuguese.lm > %{buildroot}%{_datadir}/libtextcat/portuguese.lm
iconv -f ISO-8859-1 -t UTF-8 quechua.lm > %{buildroot}%{_datadir}/libtextcat/quechua.lm
iconv -f ISO-8859-1 -t UTF-8 rumantsch.lm > %{buildroot}%{_datadir}/libtextcat/romansh.lm
iconv -f ISO-8859-5 -t UTF-8 russian-iso8859_5.lm > %{buildroot}%{_datadir}/libtextcat/russian.lm
iconv -f ISO-8859-1 -t UTF-8 scots_gaelic.lm > %{buildroot}%{_datadir}/libtextcat/scots_gaelic.lm
iconv -f ISO-8859-2 -t UTF-8 slovenian-iso8859_2.lm > %{buildroot}%{_datadir}/libtextcat/slovenian.lm
iconv -f ISO-8859-1 -t UTF-8 spanish.lm > %{buildroot}%{_datadir}/libtextcat/spanish.lm
iconv -f ISO-8859-1 -t UTF-8 swedish.lm > %{buildroot}%{_datadir}/libtextcat/swedish.lm
iconv -f ISO-8859-9 -t UTF-8 turkish.lm > %{buildroot}%{_datadir}/libtextcat/turkish.lm
iconv -f KOI8-R -t UTF-8 ukrainian-koi8_r.lm > %{buildroot}%{_datadir}/libtextcat/ukrainian.lm
#these look wrong to me, but that's what upstream OOo has done, raise this upstream
iconv -f ISO-8859-1 -t UTF-8 hindi.lm > %{buildroot}%{_datadir}/libtextcat/hindi.lm
iconv -f ISO-8859-1 -t UTF-8 persian.lm > %{buildroot}%{_datadir}/libtextcat/persian.lm
iconv -f ISO-8859-1 -t UTF-8 korean.lm > %{buildroot}%{_datadir}/libtextcat/korean.lm
iconv -f ISO-8859-1 -t UTF-8 tamil.lm > %{buildroot}%{_datadir}/libtextcat/tamil.lm
iconv -f ISO-8859-1 -t UTF-8 thai.lm > %{buildroot}%{_datadir}/libtextcat/thai.lm
iconv -f ISO-8859-1 -t UTF-8 vietnamese.lm > %{buildroot}%{_datadir}/libtextcat/vietnamese.lm
#and I have no idea how they fixed the encoding of these ones
cp -p %{SOURCE2} %{buildroot}%{_datadir}/libtextcat/chinese_simplified.lm
cp -p %{SOURCE3} %{buildroot}%{_datadir}/libtextcat/chinese_traditional.lm
cp -p %{SOURCE4} %{buildroot}%{_datadir}/libtextcat/japanese.lm
cp -p %{SOURCE5} %{buildroot}%{_datadir}/libtextcat/luxembourgish.lm
cp -p %{SOURCE6} %{buildroot}%{_datadir}/libtextcat/mongolian_cyrillic.lm
cp -p %{SOURCE7} %{buildroot}%{_datadir}/libtextcat/zulu.lm

%clean
rm -r %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog README LICENSE TODO
%dir %{_datadir}/%{name}
%{_libdir}/lib*.so.%{major}*
%{_datadir}/%{name}/*.lm
%{_datadir}/%{name}/fpdb.conf

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_bindir}/createfp
%{_libdir}/*.so
%{_includedir}/%{name}/*


%changelog
* Tue Sep 20 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2-8.1
- built for updates

* Fri Dec 17 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.2-8mdv2011.0
+ Revision: 622665
- update fingerprints
- ditch scriptlets for ancient releases
- don't lower optimization level, use -O3 as per upstream defaults

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2-7mdv2011.0
+ Revision: 609783
- rebuild

* Sat Feb 13 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2-6mdv2010.1
+ Revision: 505580
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jun 22 2008 Funda Wang <fwang@mandriva.org> 2.2-4mdv2009.0
+ Revision: 227919
- rebuild

* Tue Jun 17 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.2-3mdv2009.0
+ Revision: 223440
- fix typo in summary for -devel package

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2-2mdv2008.1
+ Revision: 117639
- correct provides for devel package

* Thu Nov 01 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2-1mdv2008.1
+ Revision: 104679
- fix file list
- import libtextcat


