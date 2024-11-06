#!/usr/bin/env python3

import argparse
import subprocess

from pathlib import Path

def run(cmd):
    print("Executing", " ".join([f'"{x}"' for x in cmd]))
    subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser(description="Deploy image on the remote RPi.")
    parser.add_argument("image", type=Path, help="image file")
    parser.add_argument("--path", required=True, type=Path, help="remote tftp path")
    parser.add_argument("--ssh-host", required=True, help="ssh host")
    parser.add_argument("--scp", required=True, type=Path, help="path to scp")
    parser.add_argument("--ssh", required=True, type=Path, help="path to ssh")
    parser.add_argument("--rpi", required=False, action='store_true', help="whether to update Raspberry config with new kernel")
    parser.add_argument("--beaglev", required=False, action='store_true', help="whether to rename new kernel for beaglev")
    args = parser.parse_args()

    assert args.ssh.is_file()
    assert args.scp.is_file()
    assert args.image.is_file()

    name = args.image.stem

    remote_file = f"{args.ssh_host}:{args.path}/{name}.img"
    run([args.scp, args.image.absolute(), remote_file])

    remote_cmd = f"chmod 777 {args.path}/{name}.img"

    run([args.ssh, args.ssh_host, remote_cmd])
    if args.rpi:
        remote_cmd = f"sed -i -E 's/^kernel=.*/kernel={name}.img/' {args.path}/config.txt"
        run([args.ssh, args.ssh_host, remote_cmd])
    if args.beaglev:
        remote_cmd = f"cp {args.path}/{name}.img {args.path}/autosar.bin"
        run([args.ssh, args.ssh_host, remote_cmd])


if __name__ == '__main__':
    main()
