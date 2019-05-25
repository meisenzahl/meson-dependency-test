project(
    'square',
    'cpp'
)

rectangle_dep = dependency('rectangle', fallback : ['rectangle', 'rectangle_dep'])

square_dep = declare_dependency(
    dependencies : [rectangle_dep]
)
