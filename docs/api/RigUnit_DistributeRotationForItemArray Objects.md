## RigUnit_DistributeRotationForItemArray Objects

```python
class RigUnit_DistributeRotationForItemArray(RigUnit_HighlevelBaseMutable)
```

Distributes rotations provided across a array of items.
Each rotation is expressed by a quaternion and a ratio, where the ratio is between 0.0 and 1.0
Note: This node adds rotation in local space of each item!

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DistributeRotation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``items`` (Array[RigElementKey]):  [Read-Write] The items to use to distribute the rotation
- ``rotation_ease_type`` (RigVMAnimEasingType):  [Read-Only] The easing to use between to rotations.
- ``rotations`` (Array[RigUnit_DistributeRotation_Rotation]):  [Read-Write] The list of rotations to be applied
- ``weight`` (float):  [Read-Write] The weight of the solver - how much the rotation should be applied

<a id="unreal.RigUnit_DistributeRotationForItemArray.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        items: Array[RigElementKey] = [],
        rotations: Array[RigUnit_DistributeRotation_Rotation] = [],
        rotation_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR,
        weight: float = 0.000000) -> None
```

<a id="unreal.RigUnit_DistributeRotationForItemArray.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write] The items to use to distribute the rotation

<a id="unreal.RigUnit_DistributeRotationForItemArray.items"></a>

#### items

```python
@items.setter
def items(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_DistributeRotationForItemArray.rotations"></a>

#### rotations

```python
@property
def rotations() -> Array[RigUnit_DistributeRotation_Rotation]
```

(Array[RigUnit_DistributeRotation_Rotation]):  [Read-Write] The list of rotations to be applied

<a id="unreal.RigUnit_DistributeRotationForItemArray.rotations"></a>

#### rotations

```python
@rotations.setter
def rotations(value: Array[RigUnit_DistributeRotation_Rotation]) -> None
```

<a id="unreal.RigUnit_DistributeRotationForItemArray.rotation_ease_type"></a>

#### rotation_ease_type

```python
@property
def rotation_ease_type() -> RigVMAnimEasingType
```

(RigVMAnimEasingType):  [Read-Only] The easing to use between to rotations.

<a id="unreal.RigUnit_DistributeRotationForItemArray.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the solver - how much the rotation should be applied

<a id="unreal.RigUnit_DistributeRotationForItemArray.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_FABRIK"></a>