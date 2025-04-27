## RigUnit_HierarchyAddControlElement Objects

```python
class RigUnit_HierarchyAddControlElement(RigUnit_HierarchyAddElement)
```

Adds a new control to the hierarchy

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] * The resulting item
- ``name`` (Name):  [Read-Write] * The name of the new element to add
- ``offset_space`` (RigVMTransformSpace):  [Read-Write] * The space the offset is in
- ``offset_transform`` (Transform):  [Read-Write] * The offset transform of the new control
- ``parent`` (RigElementKey):  [Read-Write] * The parent of the new element to add

<a id="unreal.RigUnit_HierarchyAddControlElement.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    parent: RigElementKey = [RigElementType.NONE, "None"],
    name: Name = "None",
    item: RigElementKey = [RigElementType.NONE, "None"],
    offset_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                   [-0.000000, 0.000000, 0.000000],
                                   [1.000000, 1.000000, 1.000000]],
    offset_space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE
) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlElement.offset_transform"></a>

#### offset_transform

```python
@property
def offset_transform() -> Transform
```

(Transform):  [Read-Write] * The offset transform of the new control

<a id="unreal.RigUnit_HierarchyAddControlElement.offset_transform"></a>

#### offset_transform

```python
@offset_transform.setter
def offset_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlElement.offset_space"></a>

#### offset_space

```python
@property
def offset_space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] * The space the offset is in

<a id="unreal.RigUnit_HierarchyAddControlElement.offset_space"></a>

#### offset_space

```python
@offset_space.setter
def offset_space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlFloat"></a>