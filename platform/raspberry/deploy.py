#!/usr/bin/env python3

import argparse
import subprocess

from pathlib import Path

REMOTE_TFTP_FOLDER = "/proj/tftp/research/rpi4"


def run(cmd):
    print("Executing", " ".join([f'"{x}"' for x in cmd]))
    subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser(description="Deploy image on the remote RPi.")
    parser.add_argument("image", type=Path, help="image file")
    parser.add_argument("--ssh-host", required=True, help="ssh host")
    parser.add_argument("--scp", required=True, type=Path, help="path to scp")
    parser.add_argument("--ssh", required=True, type=Path, help="path to ssh")
    args = parser.parse_args()

    assert args.ssh.is_file()
    assert args.scp.is_file()
    assert args.image.is_file()

    name = args.image.stem

    remote_file = f"{args.ssh_host}:{REMOTE_TFTP_FOLDER}/{name}.img"
    run([args.scp, args.image.absolute(), remote_file])
    remote_cmd = f"sed -i -E 's/^kernel=.*/kernel={name}.img/' {REMOTE_TFTP_FOLDER}/config.txt"
    run([args.ssh, args.ssh_host, remote_cmd])


if __name__ == '__main__':
    main()
