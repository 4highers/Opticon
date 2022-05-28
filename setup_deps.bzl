"""Setup rules/deps accordingly."""

load("@rules_python//python:repositories.bzl", "python_register_toolchains")
load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")
load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")

def _setup_gazelle():
    go_rules_dependencies()
    go_register_toolchains(version = "1.18")
    gazelle_dependencies()

def _setup_rules_python():
    python_register_toolchains(
        name = "python_interpreter",
        python_version = "3.10",
    )

def setup_rules():
    _setup_gazelle()
    _setup_rules_python()

def setup_deps():
    setup_rules()
