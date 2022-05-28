"""Import external rules/deps."""

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

def import_rules():
    http_archive(
        name = "io_bazel_rules_go",
        sha256 = "69de5c704a05ff37862f7e0f5534d4f479418afc21806c887db544a316f3cb6b",
        urls = [
            "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.27.0/rules_go-v0.27.0.tar.gz",
            "https://github.com/bazelbuild/rules_go/releases/download/v0.27.0/rules_go-v0.27.0.tar.gz",
        ],
    )

    http_archive(
        name = "bazel_gazelle",
        sha256 = "fd8d852ebcb770b41c1c933fc3085b4a23e1426a1af4e791d39b67bb8d894eb7",
        strip_prefix = "bazel-gazelle-41b542f9b0fefe916a95ca5460458abf916f5fe5",
        urls = [
            # No release since March, and we need subsequent fixes
            "https://github.com/bazelbuild/bazel-gazelle/archive/41b542f9b0fefe916a95ca5460458abf916f5fe5.zip",
        ],
    )

    http_archive(
        name = "rules_python",
        sha256 = "cdf6b84084aad8f10bf20b46b77cb48d83c319ebe6458a18e9d2cebf57807cdd",
        strip_prefix = "rules_python-0.8.1",
        url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.8.1.tar.gz",
    )
