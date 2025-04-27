## RigUnit_PositionConstraint Objects

```python
class RigUnit_PositionConstraint(RigUnit_HighlevelBaseMutable)
```

Constrains an item's position to multiple items' positions

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``filter`` (FilterOptionPerAxis):  [Read-Write]
- ``maintain_offset`` (bool):  [Read-Write]
- ``parents`` (Array[ConstraintParent]):  [Read-Write]
- ``weight`` (float):  [Read-Write]

<a id="unreal.RigUnit_PositionConstraint.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             child: RigElementKey = [RigElementType.NONE, "None"],
             maintain_offset: bool = False,
             filter: FilterOptionPerAxis = [True, True, True],
             parents: Array[ConstraintParent] = [],
             weight: float = 0.000000) -> None
```

<a id="unreal.RigUnit_PositionConstraint.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_PositionConstraint.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_PositionConstraint.maintain_offset"></a>

#### maintain_offset

```python
@property
def maintain_offset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_PositionConstraint.maintain_offset"></a>

#### maintain_offset

```python
@maintain_offset.setter
def maintain_offset(value: bool) -> None
```

<a id="unreal.RigUnit_PositionConstraint.filter"></a>

#### filter

```python
@property
def filter() -> FilterOptionPerAxis
```

(FilterOptionPerAxis):  [Read-Write]

<a id="unreal.RigUnit_PositionConstraint.filter"></a>

#### filter

```python
@filter.setter
def filter(value: FilterOptionPerAxis) -> None
```

<a id="unreal.RigUnit_PositionConstraint.parents"></a>

#### parents

```python
@property
def parents() -> Array[ConstraintParent]
```

(Array[ConstraintParent]):  [Read-Write]

<a id="unreal.RigUnit_PositionConstraint.parents"></a>

#### parents

```python
@parents.setter
def parents(value: Array[ConstraintParent]) -> None
```

<a id="unreal.RigUnit_PositionConstraint.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_PositionConstraint.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_PositionConstraintLocalSpaceOffset"></a>