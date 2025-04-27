## RigUnit_AddParent Objects

```python
class RigUnit_AddParent(RigUnit_DynamicHierarchyBaseMutable)
```

Adds a new parent to an element. The weight for the new parent will be 0.0.
You can use the SetParentWeights node to change the parent weights later.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write] * The child to be parented under the new parent
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``parent`` (RigElementKey):  [Read-Write] * The new parent to be added to the child

<a id="unreal.RigUnit_AddParent.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             child: RigElementKey = [RigElementType.NONE, "None"],
             parent: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_AddParent.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The child to be parented under the new parent

<a id="unreal.RigUnit_AddParent.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_AddParent.parent"></a>

#### parent

```python
@property
def parent() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The new parent to be added to the child

<a id="unreal.RigUnit_AddParent.parent"></a>

#### parent

```python
@parent.setter
def parent(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SetDefaultParent"></a>