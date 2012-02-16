Name:		epsxe
Version:	1.6.0
Release:	%mkrel 69.3
Summary:	Sony PlayStation emulator
License:	Freeware
Group:		Emulators
URL:		http://www.epsxe.com
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
%setup

%install
%__rm -rf %{buildroot}
%__install -D -m 0755 epsxe-start %{buildroot}%{_bindir}/epsxe-start
%__install -D -m 0644 epsxe.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%__install -D -m 0644 epsxe.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -D -m 0755 epsxe %{buildroot}%{_libdir}/epsxe/epsxe
%__install -D -m 0644 keycodes.lst %{buildroot}%{_libdir}/epsxe/keycodes.lst
%__cp -r cfg %{buildroot}%{_libdir}/%{name}/
%__cp -r docs %{buildroot}%{_libdir}/%{name}/
%__cp -r extra %{buildroot}%{_libdir}/%{name}/
%__cp -r plugins %{buildroot}%{_libdir}/%{name}/
%__cp -r shaders %{buildroot}%{_libdir}/%{name}/

%__rm -f %{buildroot}%{_libdir}/%{name}/plugins/libgpuPeopsSDL.so.1.0.16

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}-start
%{_libdir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

