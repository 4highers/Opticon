load("@rules_python//python:defs.bzl", "py_library", "py_test")

py_library(
    name = "database",
    srcs = ["handler.py"],
    imports = ["../.."],
    visibility = ["//:__subpackages__"],
    deps = [
        "//opticon/configs",
        "@pip//pypi__sqlalchemy",
    ],
)

py_test(
    name = "handler_test",
    size = "small",
    srcs = ["handler_test.py"],
    deps = [":database"],
)
