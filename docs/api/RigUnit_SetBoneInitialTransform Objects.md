## RigUnit_SetBoneInitialTransform Objects

```python
class RigUnit_SetBoneInitialTransform(RigUnitMutable)
```

SetBoneInitialTransform is used to perform a change in the hierarchy by setting a single bone's transform.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetBoneInitialTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The name of the Bone to set the transform for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``result`` (Transform):  [Read-Write] The transform value result (after weighting)
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
  in local or global space.
- ``transform`` (Transform):  [Read-Write] The transform value to set for the given Bone.

<a id="unreal.RigUnit_SetBoneInitialTransform.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             bone: Name = "None",
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             result: Transform = [[0.000000, 0.000000, 0.000000],
                                  [-0.000000, 0.000000, 0.000000],
                                  [1.000000, 1.000000, 1.000000]],
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_SetBoneInitialTransform.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The name of the Bone to set the transform for.

<a id="unreal.RigUnit_SetBoneInitialTransform.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_SetBoneInitialTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] The transform value to set for the given Bone.

<a id="unreal.RigUnit_SetBoneInitialTransform.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_SetBoneInitialTransform.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only] The transform value result (after weighting)

<a id="unreal.RigUnit_SetBoneInitialTransform.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
in local or global space.

<a id="unreal.RigUnit_SetBoneInitialTransform.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_SetBoneInitialTransform.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_SetBoneRotation"></a>