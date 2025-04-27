## RigUnit_HierarchySetParentWeights Objects

```python
class RigUnit_HierarchySetParentWeights(RigUnit_DynamicHierarchyBaseMutable)
```

Sets the item's parents' weights

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write] * The child to set the parents' weights for
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``weights`` (Array[RigElementWeight]):  [Read-Write] * The weights to set for the child's parents.
  * The number of weights needs to match the current number of parents.

<a id="unreal.RigUnit_HierarchySetParentWeights.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             child: RigElementKey = [RigElementType.NONE, "None"],
             weights: Array[RigElementWeight] = []) -> None
```

<a id="unreal.RigUnit_HierarchySetParentWeights.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The child to set the parents' weights for

<a id="unreal.RigUnit_HierarchySetParentWeights.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchySetParentWeights.weights"></a>

#### weights

```python
@property
def weights() -> Array[RigElementWeight]
```

(Array[RigElementWeight]):  [Read-Write] * The weights to set for the child's parents.
* The number of weights needs to match the current number of parents.

<a id="unreal.RigUnit_HierarchySetParentWeights.weights"></a>

#### weights

```python
@weights.setter
def weights(value: Array[RigElementWeight]) -> None
```

<a id="unreal.RigUnit_HierarchyReset"></a>