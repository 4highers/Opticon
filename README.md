# Opticon
An optimum CMS

## Bazel Related

When `requirements.in` is updated, do:

```shell
bazelisk run //:requirements.update
bazelisk run //:gazelle_python_manifest.update
```

To run any target:

```shell
bazelisk run //path/to:target
```

To test any target:

```shell
bazelisk test //path/to:target
```
