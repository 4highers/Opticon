load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "healthz",
    srcs = ["routers.py"],
    imports = ["../.."],
    visibility = ["//:__subpackages__"],
    deps = ["@pip//pypi__fastapi"],
)
