import platform


def detect_system():
    return {
        "is_arm": platform.machine() == "arm64",
        "is_mac": platform.system() == "Darwin",
        "compiler": "clang" if platform.system() == "Darwin" else "gcc",
    }


def get_openmp_paths():
    system = detect_system()
    if system["is_mac"]:
        base = "/opt/homebrew" if system["is_arm"] else "/usr/local"
        return {
            "include": f"{base}/opt/libomp/include",
            "lib": f"{base}/opt/libomp/lib",
            "flags": ["-Xpreprocessor", "-fopenmp"],
            "link_flags": ["-lomp"],
        }
    return {
        "include": "/usr/include",
        "lib": "/usr/lib",
        "flags": ["-fopenmp"],
        "link_flags": ["-fopenmp"],
    }


def generate_compile_flags():
    paths = get_openmp_paths()
    return f"""
# distutils: extra_compile_args={paths["flags"]}
# distutils: extra_link_args=-L{paths["lib"]} {" ".join(paths["link_flags"])}
# distutils: include_dirs={paths["include"]}
"""


if __name__ == "__main__":
    print(generate_compile_flags())
