# cmake-arm-embedded

CMake toolchain and helper scripts for ARM embedded software development.

## Using with Conan

Add the following line to your `conanfile.txt` to your `[tool_requires]`:

```
[tool_requires]
cmake-arm-embedded/0.1.0
```

In order to get access to the `toolchain.cmake` file, the `CMakeToolchain`
generator must be used. All together you'll need:

```
[tool_requires]
cmake-arm-embedded/0.1.0

[generator]
CMakeToolchain
```

To use the toolchain in cmake use either:

```
cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake
```

or add it to the `CMakeLists.txt` file directly:

```cmake
cmake_minimum_required(VERSION 3.15)

set(CMAKE_TOOLCHAIN_FILE conan_toolchain.cmake)

project(project_name LANGUAGES CXX)
```

> It is crucial to set the value of `CMAKE_TOOLCHAIN_FILE` before `project()` is
> invoked, because `project()` triggers toolchain detection and verification.
