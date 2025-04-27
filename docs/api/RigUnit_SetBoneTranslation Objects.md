## RigUnit_SetBoneTranslation Objects

```python
class RigUnit_SetBoneTranslation(RigUnitMutable)
```

SetBoneTranslation is used to perform a change in the hierarchy by setting a single bone's Translation.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetBoneTranslation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The name of the Bone to set the Translation for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the bone's Translation should be set
  in local or global space.
- ``translation`` (Vector):  [Read-Write] The Translation value to set for the given Bone.
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetBoneTranslation.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             bone: Name = "None",
             translation: Vector = [0.000000, 0.000000, 0.000000],
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             weight: float = 0.000000,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_SetBoneTranslation.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The name of the Bone to set the Translation for.

<a id="unreal.RigUnit_SetBoneTranslation.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_SetBoneTranslation.translation"></a>

#### translation

```python
@property
def translation() -> Vector
```

(Vector):  [Read-Write] The Translation value to set for the given Bone.

<a id="unreal.RigUnit_SetBoneTranslation.translation"></a>

#### translation

```python
@translation.setter
def translation(value: Vector) -> None
```

<a id="unreal.RigUnit_SetBoneTranslation.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the bone's Translation should be set
in local or global space.

<a id="unreal.RigUnit_SetBoneTranslation.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_SetBoneTranslation.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetBoneTranslation.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetBoneTranslation.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_GetControlColor"></a>