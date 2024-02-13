lib_platform_targets = []


pi4_clang_flags = [
    # actually pi4 is cortex-a72, but this makes it compatible with qemu
    '-mcpu=cortex-a7',
    '-mthumb',
    '-mfloat-abi=soft',
    '-std=c++11',
]

qemu_rpi4_32bit = meson.current_source_dir() / 'qemu-system-aarch64'
qemu_rpi4_32bit_cmd = [qemu_rpi4_32bit, '-M', 'raspi4b1g', '-no-reboot', '-nographic', '-serial', 'null', '-serial','mon:stdio', '-kernel']