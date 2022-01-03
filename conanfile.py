from conans import ConanFile
from conans.tools import get

QSCINTILLA_URL = "https://www.riverbankcomputing.com/static/Downloads/QScintilla/{version}/QScintilla_src-{version}.tar.gz"

SHA256_SUMS = {"2.13.1" : "800e3d2071a96bcccd7581346af0d2fe28fc30cd68530cb8302685d013afd54a"}

class QScintillaConan(ConanFile):
    name = "qscintilla"
    version = "2.13.1"
    requires = ("qt/6.2.2")

    def source(self):
        shasum = SHA256_SUMS[self.version]
        download_url = QSCINTILLA_URL.format(version=self.version,
                                             sha256=shasum)
