## RigUnit_CCDIK_RotationLimitPerItem Objects

```python
class RigUnit_CCDIK_RotationLimitPerItem(StructBase)
```

Rig Unit CCDIK Rotation Limit Per Item

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_CCDIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Write] The name of the item to apply the rotation limit to.
- ``limit`` (float):  [Read-Only] The limit of the rotation in degrees.

<a id="unreal.RigUnit_CCDIK_RotationLimitPerItem.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             limit: float = 0.000000) -> None
```

<a id="unreal.RigUnit_CCDIK_RotationLimitPerItem.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The name of the item to apply the rotation limit to.

<a id="unreal.RigUnit_CCDIK_RotationLimitPerItem.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_CCDIK_RotationLimitPerItem.limit"></a>

#### limit

```python
@property
def limit() -> float
```

(float):  [Read-Only] The limit of the rotation in degrees.

<a id="unreal.RigUnit_CCDIK"></a>