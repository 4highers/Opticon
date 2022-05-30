load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@bazel_gazelle//:def.bzl", "gazelle")
load("@rules_python//gazelle:def.bzl", "GAZELLE_PYTHON_RUNTIME_DEPS")
load("@pip//:requirements.bzl", "all_whl_requirements")
load("@rules_python//gazelle/manifest:defs.bzl", "gazelle_python_manifest")
load("@rules_python//gazelle/modules_mapping:def.bzl", "modules_mapping")

# bazelisk run //:requirements.update
# bazelisk test //:requirements_test
compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
)

modules_mapping(
    name = "modules_map",
    wheels = all_whl_requirements,
)

# bazelisk run //:gazelle_python_manifest.update
# bazelisk test //:gazelle_python_manifest.test
gazelle_python_manifest(
    name = "gazelle_python_manifest",
    modules_mapping = ":modules_map",
    pip_repository_name = "pip",
    requirements = "//:requirements.txt",
)

# bazelisk run //:gazelle
# rules_python has problem parsing py_test target
# Ref: https://github.com/bazelbuild/rules_python/issues/714
# gazelle:exclude **/*_test.py
gazelle(
    name = "gazelle",
    data = GAZELLE_PYTHON_RUNTIME_DEPS,
    gazelle = "@rules_python//gazelle:gazelle_python_binary",
)
