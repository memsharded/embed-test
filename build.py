import os, shutil, platform

from jmetadata import JMetadata

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("ERROR running {}".format(cmd))


shutil.rmtree("build", ignore_errors=True)
os.makedirs("build", exist_ok=True)
os.chdir("build")
metadata = JMetadata.load_json("../deps.json")
metadata.generate_c()

build_types = "Release", "Debug"

try:
    if platform.system() == "Windows":
        run('cmake .. -G "Visual Studio 15 Win64"')
        for build_type in build_types:
            run('cmake --build . --config {}'.format(build_type))
            # Making sure the app works
            run(".\{}\myapp.exe".format(build_type))
            for f in ["myapp.exe", "mymath.lib", "myphsx.dll"]:
                file_metadata = JMetadata.load_binary("{}/{}".format(build_type, f))
                assert file_metadata == metadata, "{}!={}".format(file_metadata, metadata)
                print("{} metadata OK".format(f), file_metadata)
    else:
        for build_type in build_types:
            run('cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE={}'.format(build_type))
            run('cmake --build .')
            # Making sure the app works
            run("./myapp")
            for f in ["myapp", "libmymath.a", "libmyphsx.so"]:
                file_metadata = JMetadata.load_binary("{}".format(f))
                assert file_metadata == metadata, "{}!={}".format(file_metadata, metadata)
                print("{} metadata OK".format(f), file_metadata)
finally:
    os.chdir("..")