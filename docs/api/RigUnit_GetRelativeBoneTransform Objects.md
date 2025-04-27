## RigUnit_GetRelativeBoneTransform Objects

```python
class RigUnit_GetRelativeBoneTransform(RigUnit)
```

GetBoneTransform is used to retrieve a single transform from a hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetRelativeBoneTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The name of the Bone to retrieve the transform for.
- ``space`` (Name):  [Read-Write] The name of the Bone to retrieve the transform relative within.
- ``transform`` (Transform):  [Read-Write] The current transform of the given bone - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetRelativeBoneTransform.__init__"></a>

#### __init__

```python
def __init__(
    bone: Name = "None",
    space: Name = "None",
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_GetRelativeBoneTransform.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The name of the Bone to retrieve the transform for.

<a id="unreal.RigUnit_GetRelativeBoneTransform.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_GetRelativeBoneTransform.space"></a>

#### space

```python
@property
def space() -> Name
```

(Name):  [Read-Write] The name of the Bone to retrieve the transform relative within.

<a id="unreal.RigUnit_GetRelativeBoneTransform.space"></a>

#### space

```python
@space.setter
def space(value: Name) -> None
```

<a id="unreal.RigUnit_GetRelativeBoneTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only] The current transform of the given bone - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetRelativeTransformForItem"></a>