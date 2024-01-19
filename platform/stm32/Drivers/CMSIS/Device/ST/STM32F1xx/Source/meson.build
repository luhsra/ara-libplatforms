
src_files = ['system_stm32f1xx.c']

obj_targets = []
includes = []
foreach include : libs_includes
  includes += ['-I', include]
endforeach
foreach src : src_files
  lib_platform_src_files += files(src)
  obj_target = custom_target(src,
                             input: src,
                             output: src+'.o',
                             depfile: src+'.dep',
                             command: clang_c+
                                      arm_clang_flags +
                                      includes +
                                      stm32_clang_flags +
                                      arm_ld_flags +
                                      ld_flags +
                                      obj_flags +
                                      clang_flags)
  lib_platform_targets += obj_target
  obj_targets += obj_target
endforeach

libstm_hal_target = custom_target('cmsis.ar',
                          input: obj_targets,
                          output: 'libcmsis.a',
                          command: ar_cmd,
                          build_by_default: true)


# ld_flags += ['-Wl,-L' + meson.current_build_dir()]
