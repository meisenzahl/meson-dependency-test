# Support for nested subprojects

See https://github.com/mesonbuild/meson/pull/5453

[xclaesse](https://github.com/xclaesse) suggested the following:

1. Check if the .wrap exists in master project. If it does, then just use that one.
2. If master project does not have a .wrap, then check if one and only one subproject has it, recursively. If only one is found, then use it.
3. If more than one subproject (or sub-sub-...-project) has that .wrap, then make an error and tell user that he has to promote one to master project to solve the conflict.
