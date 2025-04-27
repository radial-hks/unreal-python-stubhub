## RigUnit_PoseGetItems Objects

```python
class RigUnit_PoseGetItems(RigUnit_HierarchyBase)
```

Returns the items in the hierarchy pose

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``element_type`` (RigElementType):  [Read-Write]
- ``items`` (RigElementKeyCollection):  [Read-Write]
- ``pose`` (RigPose):  [Read-Write]

<a id="unreal.RigUnit_PoseGetItems.__init__"></a>

#### __init__

```python
def __init__(pose: RigPose = [],
             element_type: RigElementType = RigElementType.NONE,
             items: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_PoseGetItems.pose"></a>

#### pose

```python
@property
def pose() -> RigPose
```

(RigPose):  [Read-Write]

<a id="unreal.RigUnit_PoseGetItems.pose"></a>

#### pose

```python
@pose.setter
def pose(value: RigPose) -> None
```

<a id="unreal.RigUnit_PoseGetItems.element_type"></a>

#### element_type

```python
@property
def element_type() -> RigElementType
```

(RigElementType):  [Read-Write]

<a id="unreal.RigUnit_PoseGetItems.element_type"></a>

#### element_type

```python
@element_type.setter
def element_type(value: RigElementType) -> None
```

<a id="unreal.RigUnit_PoseGetItems.items"></a>

#### items

```python
@property
def items() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_PoseGetItemsItemArray"></a>