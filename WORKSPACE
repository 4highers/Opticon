workspace(name = "opticon")

### Import and setup external deps/rules ###
load("//:external_deps.bzl", "import_rules")

import_rules()

load("//:setup_deps.bzl", "setup_deps")

setup_deps()

### Python ###
load("@python_interpreter//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip",
    python_interpreter_target = interpreter,
    requirements_lock = "//:requirements.txt",
)

load("@pip//:requirements.bzl", "install_deps")

install_deps()

load("@rules_python//gazelle:deps.bzl", _py_gazelle_deps = "gazelle_deps")

_py_gazelle_deps()
