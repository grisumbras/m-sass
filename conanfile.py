from conans import (
    ConanFile,
    python_requires,
    tools,
)


b2 = python_requires("b2-helper/[>=0.7.1]@grisumbras/stable")

@b2.build_with_b2
class MSassConan(ConanFile):
    name = "m-sass"
    license = "BSL-1.0"
    description = "Sass version of m.css"
    homepage = "https://github.com/grisumbras/m-sass"
    url = homepage

    author = "Dmitry Arkhipov <grisumbras@gmail.com>"
    default_user = "grisumbras"
    default_channel = "testing"

    exports_sources = "build.jam", "LICENSE"
    no_copy_source = True

    def set_version(self):
        import re

        content = tools.load("build.jam")
        match = re.search(r"constant\s*VERSION\s*:\s*(\S+)\s*;", content)
        self.version = match.group(1)

    def package_id(self):
        self.info.header_only()
