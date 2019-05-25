project(
    'rectangle',
    'cpp'
)

shape_dep = dependency('shape', fallback : ['shape', 'shape_dep'])

rectangle_dep = declare_dependency(
    dependencies : [shape_dep]
)
