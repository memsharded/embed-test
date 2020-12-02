import json

metadata_h = """\
#if WIN32
__declspec(dllexport) extern char* mydata;
#else
extern char* mydata;
#endif
"""

metadata_c_template = """\
#include "jmetadata.h"

#if WIN32
char* mydata = "<jmetadata>{metadata}</jmetadata>";
#else
char* mydata = "<jmetadata>{metadata}</jmetadata>";
#endif
"""

def load(filepath):
    with open(filepath, "rb") as f:
        content = f.read()
    return content


class JMetadata:
    def __init__(self, deps=None):
        self._deps = deps

    def __str__(self):
        return str(self._deps)

    def __eq__(self, other):
        return self._deps == other._deps

    def __ne__(self, other):
        return self._deps != other._deps

    @staticmethod
    def load_json(filename):
        deps = json.loads(load(filename))
        return JMetadata(deps)

    @staticmethod
    def load_binary(filename):
        content = load(filename)
        metadata_start = content.find(b"<jmetadata>")
        if metadata_start == -1:
            return JMetadata()

        metadata_end = content.find(b"</jmetadata>")
        metadata_start += len("<jmetadata>")
        metadata = content[metadata_start:metadata_end].decode("utf-8")
        deps = metadata.split(",")
        return JMetadata(deps)

    def generate_c(self):
        metadata_c = metadata_c_template.format(metadata=",".join(dep for dep in self._deps))
        open("jmetadata.h", "w").write(metadata_h)
        open("jmetadata.c", "w").write(metadata_c)
