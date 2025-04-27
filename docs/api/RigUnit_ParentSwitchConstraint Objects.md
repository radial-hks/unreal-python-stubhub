## RigUnit_ParentSwitchConstraint Objects

```python
class RigUnit_ParentSwitchConstraint(RigUnitMutable)
```

The Parent Switch Constraint is used to have an item follow one of multiple parents,
and allowing to switch between the parent in question.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ParentSwitchConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``initial_global_transform`` (Transform):  [Read-Write] The initial global transform for the subject
- ``parent_index`` (int32):  [Read-Write] The parent index to use for constraining the subject
- ``parents`` (RigElementKeyCollection):  [Read-Write] The list of parents to constrain to
- ``subject`` (RigElementKey):  [Read-Write] The subject to constrain
- ``switched`` (bool):  [Read-Write] Returns true if the parent has changed
- ``transform`` (Transform):  [Read-Write] The transform result (full without weighting)
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_ParentSwitchConstraint.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             subject: RigElementKey = [RigElementType.NONE, "None"],
             parent_index: int = 0,
             parents: RigElementKeyCollection = [[]],
             initial_global_transform: Transform = [[
                 0.000000, 0.000000, 0.000000
             ], [-0.000000, 0.000000,
                 0.000000], [1.000000, 1.000000, 1.000000]],
             weight: float = 0.000000,
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             switched: bool = False) -> None
```

<a id="unreal.RigUnit_ParentSwitchConstraint.subject"></a>

#### subject

```python
@property
def subject() -> RigElementKey
```

(RigElementKey):  [Read-Write] The subject to constrain

<a id="unreal.RigUnit_ParentSwitchConstraint.subject"></a>

#### subject

```python
@subject.setter
def subject(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ParentSwitchConstraint.parent_index"></a>

#### parent_index

```python
@property
def parent_index() -> int
```

(int32):  [Read-Write] The parent index to use for constraining the subject

<a id="unreal.RigUnit_ParentSwitchConstraint.parent_index"></a>

#### parent_index

```python
@parent_index.setter
def parent_index(value: int) -> None
```

<a id="unreal.RigUnit_ParentSwitchConstraint.parents"></a>

#### parents

```python
@property
def parents() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write] The list of parents to constrain to

<a id="unreal.RigUnit_ParentSwitchConstraint.parents"></a>

#### parents

```python
@parents.setter
def parents(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_ParentSwitchConstraint.initial_global_transform"></a>

#### initial_global_transform

```python
@property
def initial_global_transform() -> Transform
```

(Transform):  [Read-Write] The initial global transform for the subject

<a id="unreal.RigUnit_ParentSwitchConstraint.initial_global_transform"></a>

#### initial_global_transform

```python
@initial_global_transform.setter
def initial_global_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_ParentSwitchConstraint.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_ParentSwitchConstraint.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_ParentSwitchConstraint.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only] The transform result (full without weighting)

<a id="unreal.RigUnit_ParentSwitchConstraint.switched"></a>

#### switched

```python
@property
def switched() -> bool
```

(bool):  [Read-Only] Returns true if the parent has changed

<a id="unreal.RigUnit_ParentSwitchConstraintArray"></a>