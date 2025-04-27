## RigUnit_HierarchyGetParentWeights Objects

```python
class RigUnit_HierarchyGetParentWeights(RigUnit_DynamicHierarchyBase)
```

Returns the item's parents' weights

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write] * The child to retrieve the weights for
- ``parents`` (RigElementKeyCollection):  [Read-Write] * The key for each parent
- ``weights`` (Array[RigElementWeight]):  [Read-Write] * The weight of each parent

<a id="unreal.RigUnit_HierarchyGetParentWeights.__init__"></a>

#### __init__

```python
def __init__(child: RigElementKey = [RigElementType.NONE, "None"],
             weights: Array[RigElementWeight] = [],
             parents: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_HierarchyGetParentWeights.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The child to retrieve the weights for

<a id="unreal.RigUnit_HierarchyGetParentWeights.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HierarchyGetParentWeights.weights"></a>

#### weights

```python
@property
def weights() -> Array[RigElementWeight]
```

(Array[RigElementWeight]):  [Read-Only] * The weight of each parent

<a id="unreal.RigUnit_HierarchyGetParentWeights.parents"></a>

#### parents

```python
@property
def parents() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only] * The key for each parent

<a id="unreal.RigUnit_HierarchyGetParentWeightsArray"></a>