# Opticon

Yet another CMS for blogging.

## Quickstart

Run:

```shell
bazelisk run //:Opticon_bin
```

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

## Migrations

Everytime a change is made to the database, do the migration.

1. Go to `alembic/env.py`, import the Model
2. Run `alembic --config alembic/alembic.ini revision --autogenerate -m <some messages>`

TODO(Kiyo5hi): Bazelize this process.
