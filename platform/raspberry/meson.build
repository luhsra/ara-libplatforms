lib_platform_targets = []


pi4_clang_flags = [
    '-mcpu=cortex-a72',
    '-mthumb',
    '-mfloat-abi=soft',
    '-std=c++11',
]

qemu_rpi4_32bit = meson.current_source_dir() / 'qemu-system-aarch64'
qemu_rpi4_32bit_cmd = [qemu_rpi4_32bit, '-M', 'raspi4b1g', '-no-reboot', '-nographic', '-serial', 'null', '-serial','mon:stdio', '-kernel']


rpi4_tftp_deploy = files('deploy.py')
