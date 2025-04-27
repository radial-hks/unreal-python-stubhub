## RigUnit_SetBoneRotation Objects

```python
class RigUnit_SetBoneRotation(RigUnitMutable)
```

SetBoneRotation is used to perform a change in the hierarchy by setting a single bone's rotation.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetBoneRotation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The name of the Bone to set the rotation for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``rotation`` (Quat):  [Read-Write] The rotation value to set for the given Bone.
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the bone's rotation should be set
  in local or global space.
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetBoneRotation.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             bone: Name = "None",
             rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             weight: float = 0.000000,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_SetBoneRotation.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The name of the Bone to set the rotation for.

<a id="unreal.RigUnit_SetBoneRotation.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_SetBoneRotation.rotation"></a>

#### rotation

```python
@property
def rotation() -> Quat
```

(Quat):  [Read-Write] The rotation value to set for the given Bone.

<a id="unreal.RigUnit_SetBoneRotation.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Quat) -> None
```

<a id="unreal.RigUnit_SetBoneRotation.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the bone's rotation should be set
in local or global space.

<a id="unreal.RigUnit_SetBoneRotation.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_SetBoneRotation.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetBoneRotation.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetBoneRotation.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_SetBoneTransform"></a>