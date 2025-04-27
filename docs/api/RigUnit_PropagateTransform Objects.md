## RigUnit_PropagateTransform Objects

```python
class RigUnit_PropagateTransform(RigUnitMutable)
```

Propagate Transform can be used to force a recalculation of a bone's global transform
from its local - as well as propagating that change onto the children.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_PropagateTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_to_children`` (bool):  [Read-Write] If set to true the direct children of this item will be recomputed as well.
  Combined with bRecursive all children will be affected recursively.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] The item to offset the transform for
- ``recompute_global`` (bool):  [Read-Write] If set to true the item's global transform will be recomputed from
  its parent's transform and its local.
- ``recursive`` (bool):  [Read-Write] If set to true and with bApplyToChildren enabled
  all children will be affected recursively.

<a id="unreal.RigUnit_PropagateTransform.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             item: RigElementKey = [RigElementType.NONE, "None"],
             recompute_global: bool = False,
             apply_to_children: bool = False,
             recursive: bool = False) -> None
```

<a id="unreal.RigUnit_PropagateTransform.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to offset the transform for

<a id="unreal.RigUnit_PropagateTransform.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_PropagateTransform.recompute_global"></a>

#### recompute_global

```python
@property
def recompute_global() -> bool
```

(bool):  [Read-Write] If set to true the item's global transform will be recomputed from
its parent's transform and its local.

<a id="unreal.RigUnit_PropagateTransform.recompute_global"></a>

#### recompute_global

```python
@recompute_global.setter
def recompute_global(value: bool) -> None
```

<a id="unreal.RigUnit_PropagateTransform.apply_to_children"></a>

#### apply_to_children

```python
@property
def apply_to_children() -> bool
```

(bool):  [Read-Write] If set to true the direct children of this item will be recomputed as well.
Combined with bRecursive all children will be affected recursively.

<a id="unreal.RigUnit_PropagateTransform.apply_to_children"></a>

#### apply_to_children

```python
@apply_to_children.setter
def apply_to_children(value: bool) -> None
```

<a id="unreal.RigUnit_PropagateTransform.recursive"></a>

#### recursive

```python
@property
def recursive() -> bool
```

(bool):  [Read-Write] If set to true and with bApplyToChildren enabled
all children will be affected recursively.

<a id="unreal.RigUnit_PropagateTransform.recursive"></a>

#### recursive

```python
@recursive.setter
def recursive(value: bool) -> None
```

<a id="unreal.RigUnit_SendEvent"></a>