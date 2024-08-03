# System Information API for Linux, BSD, and MacOS

Alpha-phase development, not ready for production use yet!

Documentation and such to come once the platform is more complete.

## Application Architecture

This library is composed of two layers, collectors and device.

The collectors are the low-level and generally platform-specific parsers for native binaries and files.
They are responsible for executing binaries and reading raw files to extract system information.

Device layer runs those collectors and provides a unified API for the developer to interact with.

For example, the operating system name is provided by the `operating_system` device object, 
which in turn queries /etc/version, pveversion, /etc/os-release, and system_profiler to determine the operating system.


## Low level Collectors

| Type | Collector | ![Debian](docs/images/icons/debian.svg) Debian | Ubuntu | Fedora | Rocky | MacOS | FreeBSD | Proxmox | TrueNAS |
|------|-----------|------------------------------------------------|--------|--------|-------|-------|---------|---------|---------|
| bin  | arp       | 12                                             |        |        |       |       |         |         |         |