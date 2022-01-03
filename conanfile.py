from conans import ConanFile, AutoToolsBuildEnvironment
from conans.tools import get, patch
import os

QSCINTILLA_URL = "https://www.riverbankcomputing.com/static/Downloads/QScintilla/{version}/QScintilla_src-{version}.tar.gz"

SHA256_SUMS = {"2.13.1" : "800e3d2071a96bcccd7581346af0d2fe28fc30cd68530cb8302685d013afd54a"}

class QScintillaConan(ConanFile):
    name = "qscintilla"
    version = "2.13.1"
    requires = ("qt/6.2.2")
    generators = "qmake"
    exports_sources = "add_conan_to_qmake.patch"
    
    def source(self):
        self.output.info("downloading source...")
        shasum = SHA256_SUMS[self.version]
        download_url = QSCINTILLA_URL.format(version=self.version)
        get(download_url, sha256=shasum, strip_root=True)
        self.output.info("patching sources...")
        patch_location = os.path.join(self.source_folder, "add_conan_to_qmake.patch")
        project_location = os.path.join(self.source_folder,"src")
        patch(base_path=project_location, patch_file=patch_location)
        
    def build(self):
        srcpath = os.path.join(self.source_folder, "src")
        self.run("qmake %s" % srcpath, run_environment=True)
        autotools = AutoToolsBuildEnvironment(self)
        autotools.make()
