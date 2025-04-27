## RigUnit_GetSpaceTransform Objects

```python
class RigUnit_GetSpaceTransform(RigUnit)
```

GetSpaceTransform is used to retrieve a single transform from a hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetSpaceTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``space`` (Name):  [Read-Write] The name of the Space to retrieve the transform for.
- ``space_type`` (RigVMTransformSpace):  [Read-Write] Defines if the Space's transform should be retrieved
  in local or global space.
- ``transform`` (Transform):  [Read-Write] The current transform of the given bone - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetSpaceTransform.__init__"></a>

#### __init__

```python
def __init__(
    space: Name = "None",
    space_type: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_GetSpaceTransform.space"></a>

#### space

```python
@property
def space() -> Name
```

(Name):  [Read-Write] The name of the Space to retrieve the transform for.

<a id="unreal.RigUnit_GetSpaceTransform.space"></a>

#### space

```python
@space.setter
def space(value: Name) -> None
```

<a id="unreal.RigUnit_GetSpaceTransform.space_type"></a>

#### space_type

```python
@property
def space_type() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the Space's transform should be retrieved
in local or global space.

<a id="unreal.RigUnit_GetSpaceTransform.space_type"></a>

#### space_type

```python
@space_type.setter
def space_type(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_GetSpaceTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only] The current transform of the given bone - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetTransform"></a>