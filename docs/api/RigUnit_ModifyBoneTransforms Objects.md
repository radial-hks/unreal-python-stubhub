## RigUnit_ModifyBoneTransforms Objects

```python
class RigUnit_ModifyBoneTransforms(RigUnit_HighlevelBaseMutable)
```

ModifyBonetransforms is used to perform a change in the hierarchy by setting one or more bones' transforms.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ModifyBoneTransforms.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_to_modify`` (Array[RigUnit_ModifyBoneTransforms_PerBone]):  [Read-Write] The bones to modify.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``mode`` (ControlRigModifyBoneMode):  [Read-Only] Defines if the bone's transform should be set
  in local or global space, additive or override.
- ``weight`` (float):  [Read-Write] At 1 this sets the transform, between 0 and 1 the transform is blended with previous results.
- ``weight_maximum`` (float):  [Read-Only] The maximum of the weight - defaults to 1.0
- ``weight_minimum`` (float):  [Read-Only] The minimum of the weight - defaults to 0.0

<a id="unreal.RigUnit_ModifyBoneTransforms.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    bone_to_modify: Array[RigUnit_ModifyBoneTransforms_PerBone] = [],
    weight: float = 0.000000,
    weight_minimum: float = 0.000000,
    weight_maximum: float = 0.000000,
    mode: ControlRigModifyBoneMode = ControlRigModifyBoneMode.OVERRIDE_LOCAL
) -> None
```

<a id="unreal.RigUnit_ModifyBoneTransforms.bone_to_modify"></a>

#### bone_to_modify

```python
@property
def bone_to_modify() -> Array[RigUnit_ModifyBoneTransforms_PerBone]
```

(Array[RigUnit_ModifyBoneTransforms_PerBone]):  [Read-Write] The bones to modify.

<a id="unreal.RigUnit_ModifyBoneTransforms.bone_to_modify"></a>

#### bone_to_modify

```python
@bone_to_modify.setter
def bone_to_modify(value: Array[RigUnit_ModifyBoneTransforms_PerBone]) -> None
```

<a id="unreal.RigUnit_ModifyBoneTransforms.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] At 1 this sets the transform, between 0 and 1 the transform is blended with previous results.

<a id="unreal.RigUnit_ModifyBoneTransforms.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_ModifyBoneTransforms.weight_minimum"></a>

#### weight_minimum

```python
@property
def weight_minimum() -> float
```

(float):  [Read-Only] The minimum of the weight - defaults to 0.0

<a id="unreal.RigUnit_ModifyBoneTransforms.weight_maximum"></a>

#### weight_maximum

```python
@property
def weight_maximum() -> float
```

(float):  [Read-Only] The maximum of the weight - defaults to 1.0

<a id="unreal.RigUnit_ModifyBoneTransforms.mode"></a>

#### mode

```python
@property
def mode() -> ControlRigModifyBoneMode
```

(ControlRigModifyBoneMode):  [Read-Only] Defines if the bone's transform should be set
in local or global space, additive or override.

<a id="unreal.RigUnit_ModifyTransforms_PerItem"></a>