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


| Type | Executable/Path  | Collector                                                                                          | Notes                                          |
|------|------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------|
| bin  | apt-get          | [AptInstall](docs/sys_info_api.collectors.bin.apt.md#class-aptinstall)                             | Install a package or packages with apt         |
| bin  | apt-get          | [AptShow](docs/sys_info_api.collectors.bin.apt.md#class-aptshow)                                   | Show details of a package                      |
| bin  | apt-get          | [AptUpdates](docs/sys_info_api.collectors.bin.apt.md#class-aptupdates)                             | List and install updates available             |
| bin  | arp              | [Arp](docs/sys_info_api.collectors.bin.arp.md#class-arp)                                           | List neighbors on network interfaces           |
| bin  | df               | [Df](docs/sys_info_api.collectors.bin.df.md#class-df)                                              | List filesystem usage stats                    |
| bin  | diskutil         |                                                                                                    |                                                |
| bin  | dmidecode        | [DmiBaseboard](docs/sys_info_api.collectors.bin.dmidecode.md#class-dmibaseboard)                   | Retrieve baseboard information from DMI        |
| bin  | dmidecode        | [DmiBios](docs/sys_info_api.collectors.bin.dmidecode.md#class-dmibios)                             | Retrieve BIOS information from DMI             |
| bin  | dmidecode        | [DmiCache](docs/sys_info_api.collectors.bin.dmidecode.md#class-dmicache)                           | Retrieve L1, L2, and L3 memory info from DMI   |
| bin  | dmidecode        | [DmiChassis](docs/sys_info_api.collectors.bin.dmidecode.md#class-dmichassis)                       | Retrieve chassis hardware information from DMI |
| bin  | dmidecode        | [DmiMemory](docs/sys_info_api.collectors.bin.dmidecode.md#class-dmimemory)                         | Retrieve system memory information from DMI    |
| bin  | dmidecode        | [DmiProcessor](docs/sys_info_api.collectors.bin.dmidecode.md#class-dmiprocessor)                   | Retrieve CPU information from DMI              |
| bin  | dmidecode        | [DmiSystem](docs/sys_info_api.collectors.bin.dmidecode.md#class-dmisystem)                         | Retrieve hardware vendor information from DMI  |
| bin  | dpkg             | [DpkgListInstalled](docs/sys_info_api.collectors.bin.dpkg.md#class-dpkglistinstalled)              | List installed packages with dpkg              |
| bin  | dpkg             | [DpkgInstall](docs/sys_info_api.collectors.bin.dpkg.md#class-dpkginstall)                          | Install a local package file with dpkg         |
| bin  | geom             |                                                                                                    |                                                |
| bin  | hostnamectl      | [HostnameCtl](docs/sys_info_api.collectors.bin.hostnamectl.md#class-hostnamectl)                   | Retrieve hostname and chassis information      |
| bin  | iconfig          | [Ifconfig](docs/sys_info_api.collectors.bin.ifconfig.md#class-ifconfig)                            |                                                |
| bin  | ip               | [IPLink](docs/sys_info_api.collectors.bin.ip.md#class-iplink)                                      |                                                |
| bin  | iwconfig         | [Iwconfig](docs/sys_info_api.collectors.bin.iwconfig.md#class-iwconfig)                            |                                                |
| bin  | lldptool         | [LldpNeighborScan](docs/sys_info_api.collectors.bin.lldptool.md#class-lldpneighborscan)            |                                                |
| bin  | lldptool         | [LldpStatus](docs/sys_info_api.collectors.bin.lldptool.md#class-lldpstatus)                        |                                                |
| bin  | lsblk            | [Lsblk](docs/sys_info_api.collectors.bin.lsblk.md#class-lsblk)                                     |                                                |
| bin  | lspci            | [Lspci](docs/sys_info_api.collectors.bin.lspci.md#class-lspci)                                     |                                                |
| bin  | lsusb            | [Lsusb](docs/sys_info_api.collectors.bin.lsusb.md#class-lsusb)                                     |                                                |
| bin  | mii_tool         |                                                                                                    |                                                |
| bin  | netstat          |                                                                                                    |                                                |
| bin  | pkg              | [PkgListInstalled](docs/sys_info_api.collectors.bin.pkg.md#class-pkglistinstalled)                 |                                                |
| bin  | pveversion       | [PveVersion](docs/sys_info_api.collectors.bin.pveversion.md#class-pveversion)                      |                                                |
| bin  | rpm              | [RpmInstall](docs/sys_info_api.collectors.bin.rpm.md#class-rpminstall)                             |                                                |
| bin  | smartctl         |                                                                                                    |                                                |
| bin  | sysctl           | [SysctlKernBoottime](docs/sys_info_api.collectors.bin.sysctl.md#class-sysctlkernboottime)          |                                                |
| bin  | systemctl        | [SystemCtlListServices](docs/sys_info_api.collectors.bin.systemctl.md#class-systemctllistservices) |                                                |
| bin  | softwareupdate   |                                                                                                    |                                                |
| bin  | sysctl           |                                                                                                    |                                                |
| bin  | system_profiler  |                                                                                                    |                                                |
| bin  | uname            | [UnameMachine](docs/sys_info_api.collectors.bin.uname.md#class-unamemachine)                       |                                                |
| bin  | uname            | [UnameVersion](docs/sys_info_api.collectors.bin.uname.md#class-unameversion)                       |                                                |
| bin  | uptime           | [Uptime](docs/sys_info_api.collectors.bin.uptime.md#class-uptime)                                  |                                                |
| bin  | who              | [WhoBootTime](docs/sys_info_api.collectors.bin.who.md#class-whoboottime)                           |                                                |
| bin  | yum              | [YumListInstalled](docs/sys_info_api.collectors.bin.yum.md#class-yumlistinstalled)                 |                                                |
| bin  | yum              | [YumInstall](docs/sys_info_api.collectors.bin.yum.md#class-yuminstall)                             |                                                |
| bin  | yum              | [YumUpdates](docs/sys_info_api.collectors.bin.yum.md#class-yumupdates)                             |                                                |
| bin  | vm_stat          |                                                                                                    |                                                |
| bin  | zfs              |                                                                                                    |                                                |
| etc  | /etc/os-release  | [os_release](docs/sys_info_api.collectors.etc.os_release.md#class-osrelease)                       |                                                |
| etc  | /etc/version     | version                                                                                            |                                                |
| proc | /proc/cpuinfo    | cpuinfo                                                                                            |                                                |
| proc | /proc/diskstats  | diskstats                                                                                          |                                                |
| proc | /proc/meminfo    |                                                                                                    |                                                |
| proc | /proc/mounts     |                                                                                                    |                                                |
| proc | /proc/net_dev    |                                                                                                    |                                                |
| sys  | /sys/bus/pci     |                                                                                                    |                                                |
| sys  | /sys/bus/usb     |                                                                                                    |                                                |
| sys  | /sys/class/hwmon |                                                                                                    |                                                |
| sys  | /sys/class/net   |                                                                                                    |                                                |


Test data for most collectors can be generated automatically via the `generate_test_data` script.
[List of what collectors have been tested in which operating systems](docs/os_coverage.md) 


The library is designed to gracefully handle missing collectors, 
but to get the most data, a few additional packages are useful.

Red Hat / Rocky:

```bash
sudo yum install dmidecode net-tools
```