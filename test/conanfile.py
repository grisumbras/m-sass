from conans import (
    ConanFile,
    python_requires,
)


b2 = python_requires("b2-helper/[>=0.7.1]@grisumbras/stable")

@b2.build_with_b2
class MSassTestConan(ConanFile):
    def test(self):
        pass
