## RigUnit_BoneHarmonics_BoneTarget Objects

```python
class RigUnit_BoneHarmonics_BoneTarget(StructBase)
```

Rig Unit Bone Harmonics Bone Target

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_BoneHarmonics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The name of the bone to drive
- ``ratio`` (float):  [Read-Only] The ratio of where the bone sits within the harmonics system.
  Valid values reach from 0.0 to 1.0

<a id="unreal.RigUnit_BoneHarmonics_BoneTarget.__init__"></a>

#### __init__

```python
def __init__(bone: Name = "None", ratio: float = 0.000000) -> None
```

<a id="unreal.RigUnit_BoneHarmonics_BoneTarget.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The name of the bone to drive

<a id="unreal.RigUnit_BoneHarmonics_BoneTarget.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_BoneHarmonics_BoneTarget.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Only] The ratio of where the bone sits within the harmonics system.
Valid values reach from 0.0 to 1.0

<a id="unreal.RigUnit_Harmonics_TargetItem"></a>