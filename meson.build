project('libplatforms', 'cpp',
    default_options : ['warning_level=3',
                       'cpp_std=c++17',
                       'buildtype=debugoptimized'])

## llvm dependencies
llvm_version = ['>=14', '<16']
llvm_dep = dependency('llvm', method: 'config-tool', version: llvm_version, include_type: 'system')

toolchains = subproject('toolchains')
arm_enabled = toolchains.get_variable('arm_enabled')

# this variable is filled in the subdirs
# in contains all paths that needs to be included
libs_includes = []

# common flags for clang
clang_flags = ['-g',  # generate debug information
               '-O0',
               '-Xclang', '-disable-O0-optnone',  # don't set the noopt attribute (prevent optimization needed by ARA)
               '-ffunction-sections',
               '-fdata-sections',
               '-fno-rtti',
               '-Wno-everything',
               '-fno-discard-value-names',  # use the C/C++ variable names for the pendent in the LLVM IR when possible
               '-fno-exceptions']

llvm_opt_flags = [
  # '-time-passes',
  # '-Og',
  '-O2',
]

llc_flags = ['--function-sections',
             '--data-sections',
            ]
ld_flags = ['-Wl,--gc-sections',
            '-Wl,--warn-common',
            '-Wl,--warn-section-align',
            '-Wl,--cref',
            '-Wl,-Map,@OUTPUT0@.map'
           ]

# compiler flags to generate IR
ir_flags = ['-S', '-emit-llvm',]

obj_flags = ['-c']

# standard invocations for clang with c and cpp
c_std = '-std=c11'
cxx_std = '-std=c++11'

clang = toolchains.get_variable('clang')
clang_base = [
           '-o', '@OUTPUT0@',
           '@INPUT@',
           '-MD', '-MF', '@DEPFILE@',
]
clang_c = [clang, clang_base, c_std]
clang_cpp = [clang, clang_base, cxx_std]

ar_args = ['qcs', '@OUTPUT@', '@INPUT@']


if arm_enabled
  arm_triple = toolchains.get_variable('arm_triple')
  arm_clang_flags = [
    '--target=' + arm_triple,
    '-mthumb',
    '-mcpu=cortex-m3',
    '-march=armv7-m',
    '-mabi=aapcs',
    '-mfloat-abi=soft',
    '-DF_CPU=72000000L',
    '-DMCU_STM32F103RB',
    '-DSTM32F1',
    '-DSTM32F103RB',
    '-DSTM32F103xB',
    '-fomit-frame-pointer',
    '-fno-builtin',
    '-fno-threadsafe-statics',
    '-fshort-enums',
    '--rtlib=libgcc',
  ]
  arm_mode = 'thumb' / 'v7-m' / 'nofp'

  lld = toolchains.get_variable('llvm_ld')
  arm_include_path = toolchains.get_variable('arm_include_path')
  arm_link_path = toolchains.get_variable('arm_link_path')
  libgcc_dir = toolchains.get_variable('libgcc_dir')

  arm_ld_flags = [
    '-Wl,-Map,@OUTPUT0@.map',
    '-Wl,--cref',
    '-fuse-ld=' + lld.full_path(),
    '-nostdlib',
    '-nodefaultlibs',
    '-lc',
    f'-I@arm_include_path@',
    f'-Wl,-L,@arm_link_path@' / arm_mode,
    f'-Wl,-L,@libgcc_dir@' / arm_mode,
  ]

  # llc_flags += ['--frame-pointer=none']

  arm_ar = toolchains.get_variable('arm_ar')
  ar_cmd = [arm_ar, ar_args]

  subdir('platform')
  subdir('include')

  # declare_dependency does not make sense here, see https://github.com/mesonbuild/meson/issues/12543
  libplatform_link_with = libplatform_target
  libplatform_include_directories = libs_includes
  libplatform_linkerscript = default_linkerscript
endif


