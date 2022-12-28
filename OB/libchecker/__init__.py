#coding = utf-8
import os.path
def _install_libraries(deps: list[str]):
    bruh = ["install"]
    for dep in deps:
        bruh.append(dep)
    _call_pip(bruh)
def _call_pip(args: list[str]):
    pip_internal = __import__("importlib").import_module(
        "pip._internal.cli.main"
    )
    pip_internal.main(args)
def is_import_available(name: str) -> bool:
    try:
        __import__(name)
        return True
    except ModuleNotFoundError:
        return False
def _get_uninstalled_libraries(libraries: list[tuple[str, str]]) -> list[tuple[str, str]]:
    uninstalled_libs = []
    for lib_to_check in libraries:
        if not is_import_available(lib_to_check[0]):
            uninstalled_libs.append(lib_to_check)
    return uninstalled_libs
def check_if_libraries_exist(libraries: list[tuple[str, str]], install_if_missing: bool = True) -> bool:
    uninstalled = _get_uninstalled_libraries(libraries)
    if len(uninstalled) == 0:
        return True
    if not install_if_missing:
        return False
    _install_libraries([x[1] for x in uninstalled])
    return True
def install_all_from_requirements_txt(requirements_txt_path: str = "requirements.txt"):
    if not os.path.exists(requirements_txt_path):
        raise FileNotFoundError("File "+requirements_txt_path+" not found")
    _call_pip(["install", "-r", requirements_txt_path])
