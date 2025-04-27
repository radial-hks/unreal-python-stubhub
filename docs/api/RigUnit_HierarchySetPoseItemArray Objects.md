## RigUnit_HierarchySetPoseItemArray Objects

```python
class RigUnit_HierarchySetPoseItemArray(RigUnit_HierarchyBaseMutable)
```

Sets the hierarchy's pose

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``element_type`` (RigElementType):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``items_to_set`` (Array[RigElementKey]):  [Read-Write] An optional collection to filter against
- ``pose`` (RigPose):  [Read-Write]
- ``space`` (RigVMTransformSpace):  [Read-Write]
- ``weight`` (float):  [Read-Write]

<a id="unreal.RigUnit_HierarchySetPoseItemArray.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             pose: RigPose = [],
             element_type: RigElementType = RigElementType.NONE,
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             items_to_set: Array[RigElementKey] = [],
             weight: float = 0.000000) -> None
```

<a id="unreal.RigUnit_HierarchySetPoseItemArray.pose"></a>

#### pose

```python
@property
def pose() -> RigPose
```

(RigPose):  [Read-Write]

<a id="unreal.RigUnit_HierarchySetPoseItemArray.pose"></a>

#### pose

```python
@pose.setter
def pose(value: RigPose) -> None
```

<a id="unreal.RigUnit_HierarchySetPoseItemArray.element_type"></a>

#### element_type

```python
@property
def element_type() -> RigElementType
```

(RigElementType):  [Read-Write]

<a id="unreal.RigUnit_HierarchySetPoseItemArray.element_type"></a>

#### element_type

```python
@element_type.setter
def element_type(value: RigElementType) -> None
```

<a id="unreal.RigUnit_HierarchySetPoseItemArray.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write]

<a id="unreal.RigUnit_HierarchySetPoseItemArray.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_HierarchySetPoseItemArray.items_to_set"></a>

#### items_to_set

```python
@property
def items_to_set() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write] An optional collection to filter against

<a id="unreal.RigUnit_HierarchySetPoseItemArray.items_to_set"></a>

#### items_to_set

```python
@items_to_set.setter
def items_to_set(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_HierarchySetPoseItemArray.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_HierarchySetPoseItemArray.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_PoseIsEmpty"></a>