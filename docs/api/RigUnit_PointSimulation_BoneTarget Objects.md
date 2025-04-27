## RigUnit_PointSimulation_BoneTarget Objects

```python
class RigUnit_PointSimulation_BoneTarget(StructBase)
```

Rig Unit Point Simulation Bone Target

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_PointSimulation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The name of the bone to map
- ``primary_aim_point`` (int32):  [Read-Only] The index of the point to use for aiming the primary axis.
  Use -1 to indicate that you don't want to aim the bone.
- ``secondary_aim_point`` (int32):  [Read-Only] The index of the point to use for aiming the secondary axis.
  Use -1 to indicate that you don't want to aim the bone.
- ``translation_point`` (int32):  [Read-Only] The index of the point to use for translation

<a id="unreal.RigUnit_PointSimulation_BoneTarget.__init__"></a>

#### __init__

```python
def __init__(bone: Name = "None",
             translation_point: int = 0,
             primary_aim_point: int = 0,
             secondary_aim_point: int = 0) -> None
```

<a id="unreal.RigUnit_PointSimulation_BoneTarget.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The name of the bone to map

<a id="unreal.RigUnit_PointSimulation_BoneTarget.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_PointSimulation_BoneTarget.translation_point"></a>

#### translation_point

```python
@property
def translation_point() -> int
```

(int32):  [Read-Only] The index of the point to use for translation

<a id="unreal.RigUnit_PointSimulation_BoneTarget.primary_aim_point"></a>

#### primary_aim_point

```python
@property
def primary_aim_point() -> int
```

(int32):  [Read-Only] The index of the point to use for aiming the primary axis.
Use -1 to indicate that you don't want to aim the bone.

<a id="unreal.RigUnit_PointSimulation_BoneTarget.secondary_aim_point"></a>

#### secondary_aim_point

```python
@property
def secondary_aim_point() -> int
```

(int32):  [Read-Only] The index of the point to use for aiming the secondary axis.
Use -1 to indicate that you don't want to aim the bone.

<a id="unreal.RigUnit_PointSimulation"></a>