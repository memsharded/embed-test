import os, shutil

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("ERROR running {}".format(cmd))

def load(filepath):
    with open(filepath, "rb") as f:
        content = f.read()
    return content

#shutil.rmtree("build", ignore_errors=True)
os.makedirs("build", exist_ok=True)
os.chdir("build")
try:
    #run('cmake .. -G "Visual Studio 15 Win64"')
    run('cmake --build . --config Debug')
    run(".\Debug\myapp.exe")
    for f in ("myapp.exe", "mymath.lib", "myphsx.dll"):
        app = load("Release\{}".format(f))
        metadata = app.find(b"CARABOLO")
        print("{} METADATA {}".format(f, metadata))
finally:
    os.chdir("..")