# Raspberry Pi 4

## UART Connection

[Reference](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio-and-the-40-pin-header)

| Pin | Function | Name |
| --- | -------- | ---- |
| 8   | GPIO14   | TX   |
| 10  | GPIO15   | RX   |
| 9   | Ground   | GND  |

Connect TX to RX of the UART to USB converter with 3.3V and vice versa.

```bash
minicom -D /dev/ttyUSB0
```

## SD card boot

* Extract `bootloader.tar.gz` to a fat32 partitioned SD card

## PXE boot

On the Pi4
* Boot Raspberry Pi OS
* Use `raspi-conf / Advanced` to enable network boot on the Pi 4
* Update firmware: `sudo rpi-update && sudo rpi-eeprom-update -d -a`

On the host
* `mkdir /srv/tftp && chmod 777 -R /srv/tftp`
* Extract `bootloader.tar.gz` to `/srv/tftp`
* Setup dnsmasq (DHCP+TFTP)
    ```bash
    # if NetworkManager
    #   /etc/NetworkManager/dnsmasq-shared.d/dnsmasq.conf
    # else
    #   /etc/dnsmasq.conf

    no-hosts
    log-dhcp
    pxe-service=0,"Raspberry Pi Boot"
    enable-tftp
    tftp-root=/srv/tftp
    ```

With Ethernet+UART connected, but SD card removed, the Pi should do a PXE boot.