# tests
tests = [
    'square.test'
]

gtest_dep = dependency('gtest', fallback: ['gtest', 'gtest_dep'])

foreach test_name : tests
    test_exe = executable(
        '_'.join(test_name.split('/')),
        [test_name + '.cpp'],
        include_directories : [],
        dependencies : [gtest_dep, square_dep]
    )
    test(
        '_'.join(test_name.split('/')),
        test_exe
    )
endforeach
