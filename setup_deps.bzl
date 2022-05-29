"""Setup rules/deps accordingly."""

load("@rules_python//python:repositories.bzl", "python_register_toolchains")
load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")
load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")
load("@rules_proto//proto:repositories.bzl", "rules_proto_dependencies", "rules_proto_toolchains")
load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")
load("@rules_python//gazelle:deps.bzl", _py_gazelle_deps = "gazelle_deps")

def _setup_gazelle():
    go_rules_dependencies()
    go_register_toolchains(version = "1.18")
    gazelle_dependencies()
    _py_gazelle_deps()

def _setup_rules_python():
    python_register_toolchains(
        name = "python_interpreter",
        python_version = "3.10",
    )

def _setup_protobuf():
    rules_proto_dependencies()
    rules_proto_toolchains()
    grpc_deps()

def setup_rules():
    _setup_gazelle()
    _setup_rules_python()
    _setup_protobuf()

def setup_deps():
    setup_rules()
