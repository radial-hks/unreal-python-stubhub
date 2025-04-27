## RigUnit_CCDIK_RotationLimit Objects

```python
class RigUnit_CCDIK_RotationLimit(StructBase)
```

Rig Unit CCDIK Rotation Limit

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_CCDIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The name of the bone to apply the rotation limit to.
- ``limit`` (float):  [Read-Only] The limit of the rotation in degrees.

<a id="unreal.RigUnit_CCDIK_RotationLimit.__init__"></a>

#### __init__

```python
def __init__(bone: Name = "None", limit: float = 0.000000) -> None
```

<a id="unreal.RigUnit_CCDIK_RotationLimit.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The name of the bone to apply the rotation limit to.

<a id="unreal.RigUnit_CCDIK_RotationLimit.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_CCDIK_RotationLimit.limit"></a>

#### limit

```python
@property
def limit() -> float
```

(float):  [Read-Only] The limit of the rotation in degrees.

<a id="unreal.RigUnit_CCDIK_RotationLimitPerItem"></a>