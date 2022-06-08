load("@rules_python//python:defs.bzl", "py_library")

filegroup(
    name = "configs",
    srcs = glob(
        ["**/*"],
        exclude = glob([
            "**/*.py",
            "**/*.pyc",
        ]),
    ),
    visibility = ["//:__subpackages__"],
)

py_library(
    name = "alembic",
    srcs = ["env.py"],
    imports = [".."],
    visibility = ["//:__subpackages__"],
    deps = [
        "//opticon/database",
        "@pip//pypi__alembic",
        "@pip//pypi__sqlalchemy",
    ],
)
