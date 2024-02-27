project('libplatforms', 'cpp',
    default_options : ['warning_level=3',
                       'cpp_std=c++17',
                       'buildtype=debugoptimized'])

## llvm dependencies
llvm_version = ['>=14', '<16']
llvm_dep = dependency('llvm', method: 'config-tool', version: llvm_version, include_type: 'system')

toolchains = subproject('toolchains')
arm_enabled = toolchains.get_variable('arm_enabled')

llc = toolchains.get_variable('llc')

# this variable is filled in the subdirs
# in contains all paths that needs to be included
libs_includes = []

# common flags for clang
clang_flags = [
  '-ffunction-sections',
  '-fdata-sections',
] + toolchains.get_variable('clang_flags')

llvm_opt_flags = [
  # '-time-passes',
  # '-Og',
  '-O2',
]

llc_flags = ['--function-sections',
             '--data-sections',
            ]
llc_cmd = [llc, '-filetype=obj', '-o', '@OUTPUT@', '@INPUT@', ] + llc_flags


ld_flags = ['-Wl,--gc-sections',
            '-Wl,--warn-common',
            # '-Wl,--warn-section-align',
            '-Wl,--cref',
            '-Wl,-Map,@OUTPUT0@.map'
           ]

ir_flags = toolchains.get_variable('ir_flags')

obj_flags = ['-c']

# standard invocations for clang with c and cpp

clang_c = toolchains.get_variable('clang_c_cmd')
clang_cpp = toolchains.get_variable('clang_cpp_cmd')

ar_args = ['qcs', '@OUTPUT@', '@INPUT@']


if arm_enabled
  arm_triple = toolchains.get_variable('arm_triple')
  arm_clang_flags = [
    '--target=' + arm_triple,
    '-mthumb',
  ]

  lld = toolchains.get_variable('llvm_ld')
  arm_include_path = toolchains.get_variable('arm_include_path')
  arm_link_path = toolchains.get_variable('arm_link_path')
  arm_libgcc_dir = toolchains.get_variable('arm_libgcc_dir')

  arm_ld_flags = [
    '-Wl,-Map,@OUTPUT0@.map',
    '-Wl,--cref',
    '-fuse-ld=' + lld.full_path(),
    '-nostdlib',
    '-nodefaultlibs',
  ]

  arm_ar = toolchains.get_variable('arm_ar')
  ar_cmd = [arm_ar, ar_args]

  subdir('platform')
  subdir('include')

  # declare_dependency does not make sense here, see https://github.com/mesonbuild/meson/issues/12543
  libplatform_link_with = libplatform_target
  libplatform_include_directories = libs_includes
  libplatform_linkerscript = default_linkerscript

  summary({
    'Link library (libplatform_link_with)': libplatform_link_with.full_path(),
    'Includes (libplatform_include_directories)': libplatform_include_directories,
    'Linkerscript (libplatform_linkerscript)': '@0@'.format(libplatform_linkerscript), # replace this with "full_path()" in Meson 1.4.0
  })
endif


