# BeagleV Fire

By default, the U-Boot is compiled for Supervisor mode.
To enable Machine mode, which is required by our RTOS implementation, following changes are required to the bootloader.

## Bootloader compilation

[Follow these steps](https://openbeagle.org/beaglev-fire/BeagleV-Fire-ubuntu).

At the end a complete SD card image with Ubuntu is generated.
Use this to test the device functionality.

## Patch U-Boot

### Configuration

use the provided uboot.defconfig or menuconfig to configure `BeagleV-Fire-ubuntu/uboot` with following config.
```
# U-Boot in machine mode:
CONFIG_RISCV_MMODE=y

# load image from TFTP server
CONFIG_BOOTCOMMAND="dhcp; setenv bootfile research/beaglev/autosar.bin; setenv loadaddr 0x80000000; tftp; go 0x80000000"

# for static IPs (faster)
CONFIG_BOOTCOMMAND="setenv ipaddr 10.33.23.213; setenv serverip 10.33.23.253; setenv bootfile research/beaglev/autosar.bin; setenv loadaddr 0x80000000; tftp; go 0x80000000"
```

### Multicore startup

* there are two options
  * the bootm command can be used, but images must be formatted accordingly
  * the go command (as used in the new BOOTCOMMAND) must be extended for multicore, apply the [patch file](uboot.patch)

## Configure HSS

By default, the HSS will switch to S-Mode when loading U-Boot and enable OpenSBI interface. To change this behavior:
copy `hss_config.yaml` to `BeagleV-Fire-ubuntu/deploy/config.yaml`.

## TFTP Boot

The bootloader will now load `research/beaglev/autosar.bin` from the DHCP-provided TFTP server and execute it automatically on boot.