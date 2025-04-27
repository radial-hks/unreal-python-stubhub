## RigUnit_RotationConstraint Objects

```python
class RigUnit_RotationConstraint(RigUnit_HighlevelBaseMutable)
```

Constrains an item's rotation to multiple items' rotations

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``advanced_settings`` (RigUnit_RotationConstraint_AdvancedSettings):  [Read-Write]
- ``child`` (RigElementKey):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``filter`` (FilterOptionPerAxis):  [Read-Write]
- ``maintain_offset`` (bool):  [Read-Write]
- ``parents`` (Array[ConstraintParent]):  [Read-Write]
- ``weight`` (float):  [Read-Write]

<a id="unreal.RigUnit_RotationConstraint.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             child: RigElementKey = [RigElementType.NONE, "None"],
             maintain_offset: bool = False,
             filter: FilterOptionPerAxis = [True, True, True],
             parents: Array[ConstraintParent] = [],
             advanced_settings: RigUnit_RotationConstraint_AdvancedSettings = [
                 ConstraintInterpType.AVERAGE, EulerRotationOrder.XZY
             ],
             weight: float = 0.000000) -> None
```

<a id="unreal.RigUnit_RotationConstraint.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_RotationConstraint.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_RotationConstraint.maintain_offset"></a>

#### maintain_offset

```python
@property
def maintain_offset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_RotationConstraint.maintain_offset"></a>

#### maintain_offset

```python
@maintain_offset.setter
def maintain_offset(value: bool) -> None
```

<a id="unreal.RigUnit_RotationConstraint.filter"></a>

#### filter

```python
@property
def filter() -> FilterOptionPerAxis
```

(FilterOptionPerAxis):  [Read-Write]

<a id="unreal.RigUnit_RotationConstraint.filter"></a>

#### filter

```python
@filter.setter
def filter(value: FilterOptionPerAxis) -> None
```

<a id="unreal.RigUnit_RotationConstraint.parents"></a>

#### parents

```python
@property
def parents() -> Array[ConstraintParent]
```

(Array[ConstraintParent]):  [Read-Write]

<a id="unreal.RigUnit_RotationConstraint.parents"></a>

#### parents

```python
@parents.setter
def parents(value: Array[ConstraintParent]) -> None
```

<a id="unreal.RigUnit_RotationConstraint.advanced_settings"></a>

#### advanced_settings

```python
@property
def advanced_settings() -> RigUnit_RotationConstraint_AdvancedSettings
```

(RigUnit_RotationConstraint_AdvancedSettings):  [Read-Write]

<a id="unreal.RigUnit_RotationConstraint.advanced_settings"></a>

#### advanced_settings

```python
@advanced_settings.setter
def advanced_settings(
        value: RigUnit_RotationConstraint_AdvancedSettings) -> None
```

<a id="unreal.RigUnit_RotationConstraint.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_RotationConstraint.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_RotationConstraintLocalSpaceOffset"></a>