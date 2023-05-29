# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from conan import ConanFile
from conan.tools.files import copy
from conan.tools.layout import basic_layout
import os


required_conan_version = ">=1.50.0"


class CmakeArmEmbeddedConan(ConanFile):
    name = "cmake-arm-embedded"
    version = "1.0.0"
    license = "Apache-2.0"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://libhal.github.io/libhal-armcortex"
    description = ("A collection of CMake scripts for ARM Cortex ")
    topics = ("cmake", "arm", "cortex", "cortex-m", "cortex-m0", "cortex-m0+",
              "cortex-m1", "cortex-m3", "cortex-m4", "cortex-m4f", "cortex-m7",
              "cortex-m23", "cortex-m55", "cortex-m35p", "cortex-m33")
    exports_sources = ("cmake/*", "LICENSE")
    no_copy_source = True
    options = {
        "add_subroutines": [True, False],
        "improve_debugging": [True, False]
    }
    default_options = {
        "add_subroutines": True,
        "improve_debugging": True
    }

    def package_id(self):
        self.info.clear()

    def layout(self):
        basic_layout(self)

    def package(self):
        copy(self, "LICENSE", dst=os.path.join(
            self.package_folder, "licenses"),  src=self.source_folder)
        copy(self, "cmake/*.cmake", src=self.source_folder,
             dst=self.package_folder)

    def package_info(self):
        # Add toolchain.cmake to user_toolchain configuration info to be used
        # by CMakeToolchain generator
        subroutines_path = os.path.join(
            self.package_folder, "cmake/subroutines.cmake")
        improve_debugging_path = os.path.join(
            self.package_folder, "cmake/improve_debugging.cmake")

        if self.options["add_subroutines"]:
            self.conf_info.append(
                "tools.cmake.cmaketoolchain:user_toolchain",
                subroutines_path)

        if self.options["improve_debugging"]:
            self.conf_info.append(
                "tools.cmake.cmaketoolchain:user_toolchain", improve_debugging_path)
