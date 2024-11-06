# BeagleV Fire

By default, the U-Boot is compiled for Supervisor mode.
To enable Machine mode, which is required by our RTOS implementation, following changes are required to the bootloader.

## Bootloader compilation

[Follow these steps](https://openbeagle.org/beaglev-fire/BeagleV-Fire-ubuntu).

At the end a complete SD card image with Ubuntu is generated.
Use this to test the device functionality.

## Patch U-Boot

use the provided uboot.defconfig or menuconfig to configure `BeagleV-Fire-ubuntu/uboot` with following config.
```
CONFIG_RISCV_SMODE=y
CONFIG_BOOTCOMMAND="dhcp; setenv bootfile research/beaglev/autosar.bin; setenv loadaddr 0x80000000; tftp; go 0x80000000"
```

## Configure HSS

By default, the HSS will switch to S-Mode when loading U-Boot. To change this behavior:
copy `hss_config.yaml` to `BeagleV-Fire-ubuntu/deploy/config.yaml`.

## TFTP Boot

The bootloader will now load `research/beaglev/autosar.bin` from the DHCP-provided TFTP server and execute it automatically on boot.