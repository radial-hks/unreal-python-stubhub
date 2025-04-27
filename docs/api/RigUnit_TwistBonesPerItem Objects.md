## RigUnit_TwistBonesPerItem Objects

```python
class RigUnit_TwistBonesPerItem(RigUnit_HighlevelBaseMutable)
```

Creates a gradient of twist rotation along a collection of items.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TwistBones.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``items`` (RigElementKeyCollection):  [Read-Write] The items to twist
- ``pole_axis`` (Vector):  [Read-Only] The axis to use for the pole vector for each bone
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``twist_axis`` (Vector):  [Read-Only] The axis to twist the bones around
- ``twist_ease_type`` (RigVMAnimEasingType):  [Read-Only] The easing to use between two twists.
- ``weight`` (float):  [Read-Write] The weight of the solver - how much the rotation should be applied

<a id="unreal.RigUnit_TwistBonesPerItem.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             items: RigElementKeyCollection = [[]],
             twist_axis: Vector = [0.000000, 0.000000, 0.000000],
             pole_axis: Vector = [0.000000, 0.000000, 0.000000],
             twist_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR,
             weight: float = 0.000000,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_TwistBonesPerItem.items"></a>

#### items

```python
@property
def items() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write] The items to twist

<a id="unreal.RigUnit_TwistBonesPerItem.items"></a>

#### items

```python
@items.setter
def items(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_TwistBonesPerItem.twist_axis"></a>

#### twist_axis

```python
@property
def twist_axis() -> Vector
```

(Vector):  [Read-Only] The axis to twist the bones around

<a id="unreal.RigUnit_TwistBonesPerItem.pole_axis"></a>

#### pole_axis

```python
@property
def pole_axis() -> Vector
```

(Vector):  [Read-Only] The axis to use for the pole vector for each bone

<a id="unreal.RigUnit_TwistBonesPerItem.twist_ease_type"></a>

#### twist_ease_type

```python
@property
def twist_ease_type() -> RigVMAnimEasingType
```

(RigVMAnimEasingType):  [Read-Only] The easing to use between two twists.

<a id="unreal.RigUnit_TwistBonesPerItem.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the solver - how much the rotation should be applied

<a id="unreal.RigUnit_TwistBonesPerItem.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_TwistBonesPerItem.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_TwoBoneIKSimple_DebugSettings"></a>