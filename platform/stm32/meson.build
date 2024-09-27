lib_platform_targets = []

stm32_clang_flags = [
    '-fno-builtin',
    '-fno-threadsafe-statics',
    '-fshort-enums',
    '--rtlib=libgcc',
    '-fomit-frame-pointer',
    '-mcpu=cortex-m3',
    '-march=armv7-m',
    '-mabi=aapcs',
    '-mfloat-abi=soft',
    '-DF_CPU=72000000L',
    '-DMCU_STM32F103RB',
    '-DSTM32F1',
    '-DSTM32F103RB',
    '-DSTM32F103xB',
]

stm32_arm_mode = 'thumb' / 'v7-m' / 'nofp'

stm32_ld_flags = [
    '-lc_nano',
    '-lm',
    '-lgcc',  # for floating point stuff
    '-lnosys',
    f'-I@arm_include_path@',
    f'-Wl,-L,@arm_link_path@' / stm32_arm_mode,
    f'-Wl,-L,@arm_libgcc_dir@' / stm32_arm_mode
]

subdir('Drivers/CMSIS/')
subdir('Drivers/STM32F1xx_HAL_Driver/')

src_files = [
  'init'
]

includes = []
foreach include : libs_includes
  includes += ['-I', include]
endforeach
foreach src : src_files
  obj_target = custom_target(src,
                             input: src+'.cc',
                             output: src+'.cc.o',
                             depfile: src+'.cc.dep',
                             command: clang_cpp +
                                      arm_clang_flags +
                                      stm32_clang_flags +
                                      includes +
                                      arm_ld_flags +
                                      stm32_ld_flags +
                                      ld_flags +
                                      obj_flags +
                                      clang_flags)
  lib_platform_targets += obj_target

endforeach



default_linkerscript = files('linkerscript.ld')[0]

run_target('cat_serial', command:[join_paths(meson.current_source_dir(), 'cat_serial.sh')])
