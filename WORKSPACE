workspace(name = "opticon")

### Import and setup external deps/rules ###
load("//:external_deps.bzl", "import_rules")

import_rules()

load("//:setup_deps.bzl", "setup_deps")

setup_deps()

### Python ###
load("@python_interpreter//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "pip",
    python_interpreter_target = interpreter,
    requirements = "//:requirements.txt",
)
