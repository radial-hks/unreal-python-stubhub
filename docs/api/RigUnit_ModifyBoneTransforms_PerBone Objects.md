## RigUnit_ModifyBoneTransforms_PerBone Objects

```python
class RigUnit_ModifyBoneTransforms_PerBone(StructBase)
```

Rig Unit Modify Bone Transforms Per Bone

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ModifyBoneTransforms.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The name of the Bone to set the transform for.
- ``transform`` (Transform):  [Read-Write] The transform value to set for the given Bone.

<a id="unreal.RigUnit_ModifyBoneTransforms_PerBone.__init__"></a>

#### __init__

```python
def __init__(
    bone: Name = "None",
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_ModifyBoneTransforms_PerBone.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The name of the Bone to set the transform for.

<a id="unreal.RigUnit_ModifyBoneTransforms_PerBone.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_ModifyBoneTransforms_PerBone.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] The transform value to set for the given Bone.

<a id="unreal.RigUnit_ModifyBoneTransforms_PerBone.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_ModifyBoneTransforms"></a>