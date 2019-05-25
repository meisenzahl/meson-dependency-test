project(
    'rectangle',
    'cpp'
)

shape_dep = dependency('shape', fallback : ['shape', 'shape_dep'])

includes = include_directories('include')

rectangle_dep = declare_dependency(
    include_directories : includes,
    dependencies : [shape_dep]
)
