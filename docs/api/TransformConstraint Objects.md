## TransformConstraint Objects

```python
class TransformConstraint(StructBase)
```

Transform Constraint

**C++ Source:**

- **Module**: AnimationCore
- **File**: Constraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``maintain_offset`` (bool):  [Read-Write] When the constraint is first applied, maintain the offset from the target node
- ``operator`` (ConstraintDescription):  [Read-Write]
  note: thought of separating this out per each but we'll have an issue with applying transform in what order but something to think about if that seems better
- ``source_node`` (Name):  [Read-Write]
- ``target_node`` (Name):  [Read-Write]
- ``weight`` (float):  [Read-Write]

<a id="unreal.TransformConstraint.__init__"></a>

#### __init__

```python
def __init__(operator: ConstraintDescription = [
    True, True, False, False, [True, True, True], [True, True, True],
    [True, True, True]
],
             source_node: Name = "None",
             target_node: Name = "None",
             weight: float = 0.000000,
             maintain_offset: bool = False) -> None
```

<a id="unreal.TransformConstraint.operator"></a>

#### operator

```python
@property
def operator() -> ConstraintDescription
```

(ConstraintDescription):  [Read-Write]
note: thought of separating this out per each but we'll have an issue with applying transform in what order but something to think about if that seems better

<a id="unreal.TransformConstraint.operator"></a>

#### operator

```python
@operator.setter
def operator(value: ConstraintDescription) -> None
```

<a id="unreal.TransformConstraint.source_node"></a>

#### source_node

```python
@property
def source_node() -> Name
```

(Name):  [Read-Write]

<a id="unreal.TransformConstraint.source_node"></a>

#### source_node

```python
@source_node.setter
def source_node(value: Name) -> None
```

<a id="unreal.TransformConstraint.target_node"></a>

#### target_node

```python
@property
def target_node() -> Name
```

(Name):  [Read-Write]

<a id="unreal.TransformConstraint.target_node"></a>

#### target_node

```python
@target_node.setter
def target_node(value: Name) -> None
```

<a id="unreal.TransformConstraint.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write]

<a id="unreal.TransformConstraint.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.TransformConstraint.maintain_offset"></a>

#### maintain_offset

```python
@property
def maintain_offset() -> bool
```

(bool):  [Read-Write] When the constraint is first applied, maintain the offset from the target node

<a id="unreal.TransformConstraint.maintain_offset"></a>

#### maintain_offset

```python
@maintain_offset.setter
def maintain_offset(value: bool) -> None
```

<a id="unreal.EulerTransform"></a>