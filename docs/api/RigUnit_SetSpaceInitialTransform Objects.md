## RigUnit_SetSpaceInitialTransform Objects

```python
class RigUnit_SetSpaceInitialTransform(RigUnitMutable)
```

SetSpaceInitialTransform is used to perform a change in the hierarchy by setting a single space's initial transform.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetSpaceInitialTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``result`` (Transform):  [Read-Write] The transform value result (after weighting)
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
  in local or global space.
- ``space_name`` (Name):  [Read-Write] The name of the Space to set the transform for.
- ``transform`` (Transform):  [Read-Write] The transform value to set for the given space.

<a id="unreal.RigUnit_SetSpaceInitialTransform.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        space_name: Name = "None",
        transform: Transform = [[0.000000, 0.000000, 0.000000],
                                [-0.000000, 0.000000, 0.000000],
                                [1.000000, 1.000000, 1.000000]],
        result: Transform = [[0.000000, 0.000000, 0.000000],
                             [-0.000000, 0.000000, 0.000000],
                             [1.000000, 1.000000, 1.000000]],
        space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE) -> None
```

<a id="unreal.RigUnit_SetSpaceInitialTransform.space_name"></a>

#### space_name

```python
@property
def space_name() -> Name
```

(Name):  [Read-Write] The name of the Space to set the transform for.

<a id="unreal.RigUnit_SetSpaceInitialTransform.space_name"></a>

#### space_name

```python
@space_name.setter
def space_name(value: Name) -> None
```

<a id="unreal.RigUnit_SetSpaceInitialTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] The transform value to set for the given space.

<a id="unreal.RigUnit_SetSpaceInitialTransform.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_SetSpaceInitialTransform.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only] The transform value result (after weighting)

<a id="unreal.RigUnit_SetSpaceInitialTransform.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
in local or global space.

<a id="unreal.RigUnit_SetSpaceInitialTransform.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_SetSpaceTransform"></a>