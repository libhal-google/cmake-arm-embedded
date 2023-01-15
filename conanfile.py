from conan import ConanFile
from conan.tools.files import copy
from conan.tools.layout import basic_layout
import os


required_conan_version = ">=1.50.0"


class CmakeArmEmbeddedConan(ConanFile):
    name = "cmake-arm-embedded"
    version = "0.1.0"
    license = "Apache-2.0"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://libhal.github.io/libhal-armcortex"
    description = ("A collection of CMake scripts for ARM Cortex ")
    topics = ("cmake", "ARM", "cortex", "cortex-m", "cortex-m0", "cortex-m0+",
              "cortex-m1", "cortex-m3", "cortex-m4", "cortex-m4f", "cortex-m7",
              "cortex-m23", "cortex-m55", "cortex-m35p", "cortex-m33")
    exports_sources = ("cmake/*", "LICENSE")
    no_copy_source = True

    def package_id(self):
        self.info.clear()

    def layout(self):
        basic_layout(self)

    def package(self):
        self.copy("LICENSE", dst=os.path.join(
            self.package_folder, "licenses"),  src=self.source_folder)
        self.copy("cmake/toolchain.cmake", src=self.source_folder,
                  dst=self.package_folder)

    def package_info(self):
        # Add toolchain.cmake to user_toolchain configuration info to be used
        # by CMakeToolchain generator
        f = os.path.join(self.package_folder, "cmake/toolchain.cmake")
        self.conf_info.append("tools.cmake.cmaketoolchain:user_toolchain", f)
