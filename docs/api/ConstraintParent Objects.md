## ConstraintParent Objects

```python
class ConstraintParent(StructBase)
```

Constraint Parent

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Write]
- ``weight`` (float):  [Read-Write]

<a id="unreal.ConstraintParent.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             weight: float = 0.000000) -> None
```

<a id="unreal.ConstraintParent.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.ConstraintParent.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.ConstraintParent.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write]

<a id="unreal.ConstraintParent.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_CCDIK_RotationLimit"></a>