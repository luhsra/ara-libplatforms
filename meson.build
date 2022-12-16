project('libplatforms', 'cpp',
    default_options : ['warning_level=3',
                       'cpp_std=c++17',
                       'buildtype=debugoptimized'])

fs = import('fs')

# Python
py3_mod = import('python')
py3_inst = py3_mod.find_installation('python3', modules: [])
if py3_inst.language_version().version_compare('<3.9')
    error('At least Python 3.9 is required.')
endif

## llvm dependencies
llvm_version = ['>=14', '<16']
llvm_dep = dependency('llvm', method: 'config-tool', version: llvm_version, include_type: 'system')

llvm_bindir = llvm_dep.get_variable(configtool: 'bindir')
clang = find_program(llvm_bindir / 'clang', version: llvm_version)
llvm_link = find_program(llvm_bindir / 'llvm-link', version: llvm_version)

## arch specific build tools
if get_option('arch') == 'i386'
    target_triple='x86_64-linux-gnu'
elif get_option('arch') == 'arm'
    target_triple = 'arm-none-eabi'
else
    error('unknown arch ' + get_option('arch'))
endif

arch_error = 'Do you have an @0@ toolchain? Otherwise consider to switch to another architecture. See the "arch" config option for that.'

foreach prog_name : ['ar', 'ld']
    full_prog_name = target_triple + '-' + prog_name
    prog = find_program(full_prog_name, required: false)
    if not prog.found()
        error(arch_error.format(get_option('arch').to_upper()))
    endif
    set_variable(prog_name, prog)
endforeach

# this variables are filled in the subdirs
libs_includes = []
libs_include_dirs = []

subdir('tools')
subdir('settings')
subdir('platform')
subdir('include')

libplatforms_dep = declare_dependency(link_with : libplatform_target,
                                       include_directories : libs_include_dirs)
