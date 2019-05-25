# meson-dependency-test

Project to test implementation of meson with support for nested subprojects.

```shell
git clone -b nested-subprojects git@github.com:semasquare/meson.git
cd test
rm -rf subprojects/packagecache/ subprojects/square
python3 ../meson/__main__.py build
ninja -C build test
```
