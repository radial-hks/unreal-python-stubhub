## RigUnit_GetInitialBoneTransform Objects

```python
class RigUnit_GetInitialBoneTransform(RigUnit)
```

GetInitialBoneTransform is used to retrieve a single transform from a hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetInitialBoneTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The name of the Bone to retrieve the transform for.
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be retrieved
  in local or global space.
- ``transform`` (Transform):  [Read-Write] The current transform of the given bone - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetInitialBoneTransform.__init__"></a>

#### __init__

```python
def __init__(
    bone: Name = "None",
    space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_GetInitialBoneTransform.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The name of the Bone to retrieve the transform for.

<a id="unreal.RigUnit_GetInitialBoneTransform.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_GetInitialBoneTransform.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be retrieved
in local or global space.

<a id="unreal.RigUnit_GetInitialBoneTransform.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_GetInitialBoneTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only] The current transform of the given bone - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetRelativeBoneTransform"></a>