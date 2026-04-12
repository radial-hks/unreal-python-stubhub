## RigUnit\_HierarchyGetPose Objects

```python
class RigUnit_HierarchyGetPose(RigUnit_HierarchyBase)
```

Returns the hierarchy's pose

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``element_type`` (RigElementType):  [Read-Write]
- ``initial`` (bool):  [Read-Write]
- ``items_to_get`` (RigElementKeyCollection):  [Read-Write] An optional collection to filter against
- ``pose`` (RigPose):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetPose.__init__"></a>

#### \_\_init\_\_

```python
def __init__(initial: bool = False,
             element_type: RigElementType = RigElementType.NONE,
             items_to_get: RigElementKeyCollection = [[]],
             pose: RigPose = []) -> None
```

<a id="unreal.RigUnit_HierarchyGetPose.initial"></a>

#### initial

```python
@property
def initial() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetPose.initial"></a>

#### initial

```python
@initial.setter
def initial(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetPose.element_type"></a>

#### element\_type

```python
@property
def element_type() -> RigElementType
```

(RigElementType):  [Read-Write]

<a id="unreal.RigUnit_HierarchyGetPose.element_type"></a>

#### element\_type

```python
@element_type.setter
def element_type(value: RigElementType) -> None
```

<a id="unreal.RigUnit_HierarchyGetPose.items_to_get"></a>

#### items\_to\_get

```python
@property
def items_to_get() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write] An optional collection to filter against

<a id="unreal.RigUnit_HierarchyGetPose.items_to_get"></a>

#### items\_to\_get

```python
@items_to_get.setter
def items_to_get(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_HierarchyGetPose.pose"></a>

#### pose

```python
@property
def pose() -> RigPose
```

(RigPose):  [Read-Only]

<a id="unreal.RigUnit_HierarchyGetPoseItemArray"></a>