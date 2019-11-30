{
    'targets': [
        {
            'target_name': 'pcsclite',
            'sources': [ 'src/addon.cpp', 'src/pcsclite.cpp', 'src/cardreader.cpp' ],
            'cflags': [
                '-Wall',
                '-Wextra',
                '-Wno-unused-parameter',
                '-fPIC',
                '-fno-strict-aliasing',
                '-fno-exceptions',
                '-pedantic'
              ],
            'conditions': [
                ['target_arch=="arm"', {
                    'conditions': [
                        ['OS=="linux"', {
                            'link_settings': {
                                'libraries': [ '--sysroot=$(SYS_ROOT)' ],
                                'library_dirs': [ '$(SYS_ROOT)/usr/lib/$(HOST)' ]
                            }
                        }]
                    ]
                }], 
                ['OS=="linux"', {
                    'include_dirs': [
                        '/usr/include/PCSC',
                        '<!(node -e "require(\'nan\')")'
                    ],
                    'link_settings': {
                        'libraries': [ '-lpcsclite' ],
                        'library_dirs': [ '/usr/lib' ]
                    }
                }],
                ['OS=="mac"', {
                  'libraries': ['-framework', 'PCSC'],
                  "include_dirs" : [ "<!(node -e \"require('nan')\")" ]
                }],
                ['OS=="win"', {
                  'libraries': ['-lWinSCard'],
                  "include_dirs" : [ "<!(node -e \"require('nan')\")" ]
                }]
            ]
        }
    ]
}
