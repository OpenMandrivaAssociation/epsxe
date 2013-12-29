%define __noautoprov '(.*)\\.so(.*)'
%define __noautoreq 'libstdc\\+\\+-libc6\\.2-2\\.so\\.3'

Summary:	Sony PlayStation emulator
Name:		epsxe
Version:	1.6.0
Release:	69.7
License:	Freeware
Group:		Emulators
Url:		http://www.epsxe.com
# Custom repack with plugins etc
Source:		%{name}-%{version}.tar.bz2
Suggests:	galaxy-gtk12
ExclusiveArch:	%{ix86}

%description
Great Sony PlayStation emulator. Requires a BIOS image. Includes
the best plugins:

GPU P.E.Op.S. MesaGL 1.78
GPU P.E.Op.S. SoftX 1.18
GPU Pete's XGL2 2.9

SPU Eternal 1.41
SPU P.E.Op.S. ALSA 1.9
SPU P.E.Op.S. OSS 1.9
SPU Pete's Null 1.1

JoyPad Lamer0's JoyPadXwin 1.1
JoyPad ammoQ's PadJoy 0.8
JoyPad Linuzappz X Windows Pad Driver 1.6

%prep
%setup -q

%install
install -D -m 0755 epsxe-start %{buildroot}%{_bindir}/epsxe-start
install -D -m 0644 epsxe.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -m 0644 epsxe.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 0755 epsxe %{buildroot}%{_libdir}/epsxe/epsxe
install -D -m 0644 keycodes.lst %{buildroot}%{_libdir}/epsxe/keycodes.lst
cp -r cfg %{buildroot}%{_libdir}/%{name}/
cp -r docs %{buildroot}%{_libdir}/%{name}/
cp -r extra %{buildroot}%{_libdir}/%{name}/
cp -r plugins %{buildroot}%{_libdir}/%{name}/
cp -r runtime %{buildroot}%{_libdir}/%{name}/
cp -r shaders %{buildroot}%{_libdir}/%{name}/

rm -f %{buildroot}%{_libdir}/%{name}/plugins/libgpuPeopsSDL.so.1.0.16

%files
%{_bindir}/%{name}-start
%{_libdir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

