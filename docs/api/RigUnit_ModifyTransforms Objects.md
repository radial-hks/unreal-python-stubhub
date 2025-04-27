## RigUnit_ModifyTransforms Objects

```python
class RigUnit_ModifyTransforms(RigUnit_HighlevelBaseMutable)
```

Modify Transforms is used to perform a change in the hierarchy by setting one or more bones' transforms

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ModifyTransforms.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item_to_modify`` (Array[RigUnit_ModifyTransforms_PerItem]):  [Read-Write] The items to modify.
- ``mode`` (ControlRigModifyBoneMode):  [Read-Only] Defines if the bone's transform should be set
  in local or global space, additive or override.
- ``weight`` (float):  [Read-Write] At 1 this sets the transform, between 0 and 1 the transform is blended with previous results.
- ``weight_maximum`` (float):  [Read-Only] The maximum of the weight - defaults to 1.0
- ``weight_minimum`` (float):  [Read-Only] The minimum of the weight - defaults to 0.0

<a id="unreal.RigUnit_ModifyTransforms.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    item_to_modify: Array[RigUnit_ModifyTransforms_PerItem] = [],
    weight: float = 0.000000,
    weight_minimum: float = 0.000000,
    weight_maximum: float = 0.000000,
    mode: ControlRigModifyBoneMode = ControlRigModifyBoneMode.OVERRIDE_LOCAL
) -> None
```

<a id="unreal.RigUnit_ModifyTransforms.item_to_modify"></a>

#### item_to_modify

```python
@property
def item_to_modify() -> Array[RigUnit_ModifyTransforms_PerItem]
```

(Array[RigUnit_ModifyTransforms_PerItem]):  [Read-Write] The items to modify.

<a id="unreal.RigUnit_ModifyTransforms.item_to_modify"></a>

#### item_to_modify

```python
@item_to_modify.setter
def item_to_modify(value: Array[RigUnit_ModifyTransforms_PerItem]) -> None
```

<a id="unreal.RigUnit_ModifyTransforms.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] At 1 this sets the transform, between 0 and 1 the transform is blended with previous results.

<a id="unreal.RigUnit_ModifyTransforms.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_ModifyTransforms.weight_minimum"></a>

#### weight_minimum

```python
@property
def weight_minimum() -> float
```

(float):  [Read-Only] The minimum of the weight - defaults to 0.0

<a id="unreal.RigUnit_ModifyTransforms.weight_maximum"></a>

#### weight_maximum

```python
@property
def weight_maximum() -> float
```

(float):  [Read-Only] The maximum of the weight - defaults to 1.0

<a id="unreal.RigUnit_ModifyTransforms.mode"></a>

#### mode

```python
@property
def mode() -> ControlRigModifyBoneMode
```

(ControlRigModifyBoneMode):  [Read-Only] Defines if the bone's transform should be set
in local or global space, additive or override.

<a id="unreal.RigUnit_MultiFABRIK_EndEffector"></a>