## RigUnit_SetSpaceTransform Objects

```python
class RigUnit_SetSpaceTransform(RigUnitMutable)
```

SetSpaceTransform is used to perform a change in the hierarchy by setting a single space's transform.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetSpaceTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``space`` (Name):  [Read-Write] The name of the Space to set the transform for.
- ``space_type`` (RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
  in local or global space.
- ``transform`` (Transform):  [Read-Write] The transform value to set for the given Space.
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetSpaceTransform.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        space: Name = "None",
        weight: float = 0.000000,
        transform: Transform = [[0.000000, 0.000000, 0.000000],
                                [-0.000000, 0.000000, 0.000000],
                                [1.000000, 1.000000, 1.000000]],
        space_type: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE
) -> None
```

<a id="unreal.RigUnit_SetSpaceTransform.space"></a>

#### space

```python
@property
def space() -> Name
```

(Name):  [Read-Write] The name of the Space to set the transform for.

<a id="unreal.RigUnit_SetSpaceTransform.space"></a>

#### space

```python
@space.setter
def space(value: Name) -> None
```

<a id="unreal.RigUnit_SetSpaceTransform.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetSpaceTransform.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetSpaceTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] The transform value to set for the given Space.

<a id="unreal.RigUnit_SetSpaceTransform.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_SetSpaceTransform.space_type"></a>

#### space_type

```python
@property
def space_type() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
in local or global space.

<a id="unreal.RigUnit_SetSpaceTransform.space_type"></a>

#### space_type

```python
@space_type.setter
def space_type(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_SetTransform"></a>