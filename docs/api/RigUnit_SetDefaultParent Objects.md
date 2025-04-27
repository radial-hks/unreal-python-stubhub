## RigUnit_SetDefaultParent Objects

```python
class RigUnit_SetDefaultParent(RigUnit_DynamicHierarchyBaseMutable)
```

Changes the default parent for an item - this removes all other current parents.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write] * The child to be parented under the new default parent
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``parent`` (RigElementKey):  [Read-Write] * The default parent to be used for the child

<a id="unreal.RigUnit_SetDefaultParent.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             child: RigElementKey = [RigElementType.NONE, "None"],
             parent: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_SetDefaultParent.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The child to be parented under the new default parent

<a id="unreal.RigUnit_SetDefaultParent.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SetDefaultParent.parent"></a>

#### parent

```python
@property
def parent() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The default parent to be used for the child

<a id="unreal.RigUnit_SetDefaultParent.parent"></a>

#### parent

```python
@parent.setter
def parent(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SetChannelHosts"></a>