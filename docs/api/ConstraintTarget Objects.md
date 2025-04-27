## ConstraintTarget Objects

```python
class ConstraintTarget(StructBase)
```

Constraint Target

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter`` (TransformFilter):  [Read-Only]
- ``maintain_offset`` (bool):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``weight`` (float):  [Read-Write]

<a id="unreal.ConstraintTarget.__init__"></a>

#### __init__

```python
def __init__(
    filter: TransformFilter = [[True, True, True], [True, True, True],
                               [True, True, True]]
) -> None
```

<a id="unreal.ConstraintTarget.filter"></a>

#### filter

```python
@property
def filter() -> TransformFilter
```

(TransformFilter):  [Read-Only]

<a id="unreal.RigUnit_TransformConstraint"></a>