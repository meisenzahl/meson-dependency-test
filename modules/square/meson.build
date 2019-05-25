project(
    'square',
    'cpp'
)

rectangle_dep = dependency('rectangle', fallback : ['rectangle', 'rectangle_dep'])

includes = include_directories('include')

square_dep = declare_dependency(
    include_directories : includes,
    dependencies : [rectangle_dep]
)
