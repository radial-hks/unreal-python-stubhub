## TypedElementDeletionOptions Objects

```python
class TypedElementDeletionOptions(StructBase)
```

Typed Element Deletion Options

**C++ Source:**

- **Module**: Engine
- **File**: TypedElementWorldInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``verify_deletion_can_happen`` (bool):  [Read-Write]
- ``warn_about_references`` (bool):  [Read-Write]
- ``warn_about_soft_references`` (bool):  [Read-Write]

<a id="unreal.TypedElementDeletionOptions.__init__"></a>

#### __init__

```python
def __init__(verify_deletion_can_happen: bool = False,
             warn_about_references: bool = False,
             warn_about_soft_references: bool = False) -> None
```

<a id="unreal.TypedElementDeletionOptions.verify_deletion_can_happen"></a>

#### verify_deletion_can_happen

```python
@property
def verify_deletion_can_happen() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TypedElementDeletionOptions.verify_deletion_can_happen"></a>

#### verify_deletion_can_happen

```python
@verify_deletion_can_happen.setter
def verify_deletion_can_happen(value: bool) -> None
```

<a id="unreal.TypedElementDeletionOptions.warn_about_references"></a>

#### warn_about_references

```python
@property
def warn_about_references() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TypedElementDeletionOptions.warn_about_references"></a>

#### warn_about_references

```python
@warn_about_references.setter
def warn_about_references(value: bool) -> None
```

<a id="unreal.TypedElementDeletionOptions.warn_about_soft_references"></a>

#### warn_about_soft_references

```python
@property
def warn_about_soft_references() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TypedElementDeletionOptions.warn_about_soft_references"></a>

#### warn_about_soft_references

```python
@warn_about_soft_references.setter
def warn_about_soft_references(value: bool) -> None
```

<a id="unreal.DamageEvent"></a>