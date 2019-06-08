project(
    'circle',
    'cpp'
)

shape_dep = dependency('shape', fallback : ['shape', 'shape_dep'])

includes = include_directories('include')

circle_dep = declare_dependency(
    include_directories : includes,
    dependencies : [shape_dep]
)
