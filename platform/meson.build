lib_platform_src_files = []
libplatform_includes = []


subdir('raspberry')
subdir('beaglev')
subdir('stm32')
libplatform_target = custom_target('libplatform.a',
                                   input: lib_platform_targets,
                                   output: 'libplatform.a',
                                   command: ar_cmd,
                                   build_by_default: true)
