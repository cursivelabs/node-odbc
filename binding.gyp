{
  'targets' : [
    {
      'target_name' : 'odbc_bindings',
      'sources' : [ 
        'src/odbc.cpp',
        'src/odbc_connection.cpp',
        'src/odbc_statement.cpp',
        'src/odbc_result.cpp',
        'src/dynodbc.cpp'
      ],
      'cflags' : ['-Wall', '-Wextra', '-Wno-unused-parameter'],
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'defines' : [
        'dynodbc'
      ],
      'conditions' : [
        [ 'OS == "linux"', {
          'libraries' : [
          ],
          'cflags' : [
            '-g'
          ]
        }],
        [ 'OS == "mac"', {
          'libraries' : [
          ]
        }],
        [ 'OS=="win"', {
          'sources' : [
            'src/strptime.c',
            'src/odbc.cpp'
          ],
          'libraries' : [ 
            '-lodbccp32.lib' 
          ]
        }]
      ]
    }
  ]
}

