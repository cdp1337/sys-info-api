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


## Setting up from source (for development)

Linux Mint 22 requires python-venv to be installed: `sudo apt install python3-venv`

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -e .[dev]
```

## Low level Collectors

List of collectors and the platforms tested.
(Not a definitive list of supported platforms, as Debian support for example generally extends to any Debian-based distro
and TrueNAS generally derives from FreeBSD support.)

<!--
![Debian](docs/images/icons/debian.svg)
![Ubuntu](docs/images/icons/ubuntu.svg)
![Fedora](docs/images/icons/fedora.svg)
![Rocky Linux](docs/images/icons/rocky.svg)
![MacOS](docs/images/icons/macos.svg)
![FreeBSD](docs/images/icons/freebsd.svg)
-->

| Type | Executable/Path  | Collector                                                                    | Compability                                                                     |
|------|------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| bin  | apt-get          | [AptInstall](docs/sys_info_api.collectors.bin.apt.md#class-aptinstall)       | ![Debian](docs/images/icons/debian.svg) ![Ubuntu](docs/images/icons/ubuntu.svg) |
| bin  | apt-get          | [AptShow](docs/sys_info_api.collectors.bin.apt.md#class-aptshow)             | ![Debian](docs/images/icons/debian.svg) ![Ubuntu](docs/images/icons/ubuntu.svg) |
| bin  | apt-get          | [AptUpdates](docs/sys_info_api.collectors.bin.apt.md#class-aptupdates)       | ![Debian](docs/images/icons/debian.svg) ![Ubuntu](docs/images/icons/ubuntu.svg) |
| bin  | arp              | [arp](docs/sys_info_api.collectors.bin.arp.md#class-arp)                     |                                                                                 |
| bin  | df               | [df](docs/sys_info_api.collectors.bin.df.md#class-df)                        |                                                                                 |
| bin  | diskutil         |                                                                              |                                                                                 |
| bin  | dmidecode        | [dmidecode](docs/sys_info_api.collectors.bin.dmidecode.md)                   |                                                                                 |
| bin  | dpkg             | dpkg                                                                         |                                                                                 |
| bin  | geom             | geom                                                                         |                                                                                 |
| bin  | hostnamectl      | [hostnamectl](docs/sys_info_api.collectors.bin.hostnamectl.md)               |                                                                                 |
| bin  | iconfig          | [ifconfig](docs/sys_info_api.collectors.bin.ifconfig.md)                     |                                                                                 |
| bin  | ip               | [ip](docs/sys_info_api.collectors.bin.ip.md)                                 |                                                                                 |
| bin  | lldptool         | [lldptool](docs/sys_info_api.collectors.bin.lldptool.md)                     |                                                                                 |
| bin  | lsblk            |                                                                              |                                                                                 |
| bin  | lspci            |                                                                              |                                                                                 |
| bin  | lsusb            |                                                                              |                                                                                 |
| bin  | mii_tool         |                                                                              |                                                                                 |
| bin  | netstat          |                                                                              |                                                                                 |
| bin  | pveversion       |                                                                              |                                                                                 |
| bin  | smartctl         |                                                                              |                                                                                 |
| bin  | systemctl        |                                                                              |                                                                                 |
| bin  | softwareupdate   |                                                                              |                                                                                 |
| bin  | sysctl           |                                                                              |                                                                                 |
| bin  | system_profiler  |                                                                              |                                                                                 |
| bin  | vm_stat          |                                                                              |                                                                                 |
| bin  | zfs              |                                                                              |                                                                                 |
| etc  | /etc/os-release  | [os_release](docs/sys_info_api.collectors.etc.os_release.md#class-osrelease) |                                                                                 |
| etc  | /etc/version     | version                                                                      |                                                                                 |
| proc | /proc/cpuinfo    | cpuinfo                                                                      |                                                                                 |
| proc | /proc/diskstats  | diskstats                                                                    |                                                                                 |
| proc | /proc/meminfo    |                                                                              |                                                                                 |
| proc | /proc/mounts     |                                                                              |                                                                                 |
| proc | /proc/net_dev    |                                                                              |                                                                                 |
| sys  | /sys/bus/pci     |                                                                              |                                                                                 |
| sys  | /sys/bus/usb     |                                                                              |                                                                                 |
| sys  | /sys/class/hwmon |                                                                              |                                                                                 |
| sys  | /sys/class/net   |                                                                              |                                                                                 |

The library is designed to gracefully handle missing collectors, 
but to get the most data, a few additional packages are useful.

Red Hat / Rocky:

```bash
sudo yum install dmidecode net-tools
```