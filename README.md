# cmake-arm-embedded

CMake toolchain and helper scripts for ARM embedded software development.

## Using with Conan

Add the following line to your `conanfile.txt` to your `[tool_requires]`:

```
[tool_requires]
cmake-arm-embedded/0.1.1
```

In order to get access to the `toolchain.cmake` file, the `CMakeToolchain`
generator must be used. All together you'll need:

```
[tool_requires]
cmake-arm-embedded/0.1.1

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

## Available Architecture Flags

- `CORTEX_M4F_FLAGS`: Flags for a cortex M4 processor with a hardware floating
  point unit.
- `CORTEX_M4_FLAGS`: Flags for a cortex M4 processor without a floating point
  unit.

Using these in your `CMakeLists.txt`:

```cmake
target_compile_options(${PROJECT_NAME} PRIVATE ${CORTEX_M4F_FLAGS})
```

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for details.

## License

Apache 2.0; see [`LICENSE`](LICENSE) for details.

## Disclaimer

This project is not an official Google project. It is not supported by
Google and Google specifically disclaims all warranties as to its quality,
merchantability, or fitness for a particular purpose.

