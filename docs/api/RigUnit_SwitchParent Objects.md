## RigUnit_SwitchParent Objects

```python
class RigUnit_SwitchParent(RigUnit_DynamicHierarchyBaseMutable)
```

Switches an element to a new parent.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write] The child to switch to a new parent
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``maintain_global`` (bool):  [Read-Write] If set to true the item will maintain its global transform,
         * otherwise it will maintain local
- ``mode`` (RigSwitchParentMode):  [Read-Write] Depending on this the child will switch to the world,
         * back to its default or to the item provided by the Parent pin
- ``parent`` (RigElementKey):  [Read-Write] The optional parent to switch to. This is only used if the mode is set to 'Parent Item'

<a id="unreal.RigUnit_SwitchParent.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             mode: RigSwitchParentMode = RigSwitchParentMode.WORLD,
             child: RigElementKey = [RigElementType.NONE, "None"],
             parent: RigElementKey = [RigElementType.NONE, "None"],
             maintain_global: bool = False) -> None
```

<a id="unreal.RigUnit_SwitchParent.mode"></a>

#### mode

```python
@property
def mode() -> RigSwitchParentMode
```

(RigSwitchParentMode):  [Read-Write] Depending on this the child will switch to the world,
       * back to its default or to the item provided by the Parent pin

<a id="unreal.RigUnit_SwitchParent.mode"></a>

#### mode

```python
@mode.setter
def mode(value: RigSwitchParentMode) -> None
```

<a id="unreal.RigUnit_SwitchParent.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write] The child to switch to a new parent

<a id="unreal.RigUnit_SwitchParent.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SwitchParent.parent"></a>

#### parent

```python
@property
def parent() -> RigElementKey
```

(RigElementKey):  [Read-Write] The optional parent to switch to. This is only used if the mode is set to 'Parent Item'

<a id="unreal.RigUnit_SwitchParent.parent"></a>

#### parent

```python
@parent.setter
def parent(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SwitchParent.maintain_global"></a>

#### maintain_global

```python
@property
def maintain_global() -> bool
```

(bool):  [Read-Write] If set to true the item will maintain its global transform,
       * otherwise it will maintain local

<a id="unreal.RigUnit_SwitchParent.maintain_global"></a>

#### maintain_global

```python
@maintain_global.setter
def maintain_global(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyGetParentWeights"></a>