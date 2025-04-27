## RigUnit_FullbodyIK Objects

```python
class RigUnit_FullbodyIK(RigUnit_HighlevelBaseMutable)
```

Based on Jacobian solver at core, this can solve multi chains within a root using multi effectors

**C++ Source:**

- **Plugin**: FullBodyIK
- **Module**: FullBodyIK
- **File**: RigUnit_FullbodyIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``constraints`` (Array[FBIKConstraintOption]):  [Read-Write]
- ``debug_option`` (FBIKDebugOption):  [Read-Write]
- ``effectors`` (Array[FBIKEndEffector]):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``motion_property`` (MotionProcessInput):  [Read-Only]
- ``propagate_to_children`` (bool):  [Read-Write] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``root`` (RigElementKey):  [Read-Only] The first bone in the chain to solve
- ``solver_property`` (SolverInput):  [Read-Only]

<a id="unreal.RigUnit_FullbodyIK.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             root: RigElementKey = [RigElementType.NONE, "None"],
             effectors: Array[FBIKEndEffector] = [],
             constraints: Array[FBIKConstraintOption] = [],
             solver_property: SolverInput = [],
             motion_property: MotionProcessInput = [],
             propagate_to_children: bool = False,
             debug_option: FBIKDebugOption = []) -> None
```

<a id="unreal.RigUnit_FullbodyIK.root"></a>

#### root

```python
@property
def root() -> RigElementKey
```

(RigElementKey):  [Read-Only] The first bone in the chain to solve

<a id="unreal.RigUnit_FullbodyIK.effectors"></a>

#### effectors

```python
@property
def effectors() -> Array[FBIKEndEffector]
```

(Array[FBIKEndEffector]):  [Read-Write]

<a id="unreal.RigUnit_FullbodyIK.effectors"></a>

#### effectors

```python
@effectors.setter
def effectors(value: Array[FBIKEndEffector]) -> None
```

<a id="unreal.RigUnit_FullbodyIK.end_effectors"></a>

#### end_effectors

```python
@property
def end_effectors() -> Array[FBIKEndEffector]
```

deprecated: 'end_effectors' was renamed to 'effectors'.

<a id="unreal.RigUnit_FullbodyIK.end_effectors"></a>

#### end_effectors

```python
@end_effectors.setter
def end_effectors(value: Array[FBIKEndEffector]) -> None
```

<a id="unreal.RigUnit_FullbodyIK.constraints"></a>

#### constraints

```python
@property
def constraints() -> Array[FBIKConstraintOption]
```

(Array[FBIKConstraintOption]):  [Read-Write]

<a id="unreal.RigUnit_FullbodyIK.constraints"></a>

#### constraints

```python
@constraints.setter
def constraints(value: Array[FBIKConstraintOption]) -> None
```

<a id="unreal.RigUnit_FullbodyIK.solver_property"></a>

#### solver_property

```python
@property
def solver_property() -> SolverInput
```

(SolverInput):  [Read-Only]

<a id="unreal.RigUnit_FullbodyIK.motion_property"></a>

#### motion_property

```python
@property
def motion_property() -> MotionProcessInput
```

(MotionProcessInput):  [Read-Only]

<a id="unreal.RigUnit_FullbodyIK.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Write] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_FullbodyIK.propagate_to_children"></a>

#### propagate_to_children

```python
@propagate_to_children.setter
def propagate_to_children(value: bool) -> None
```

<a id="unreal.RigUnit_FullbodyIK.debug_option"></a>

#### debug_option

```python
@property
def debug_option() -> FBIKDebugOption
```

(FBIKDebugOption):  [Read-Write]

<a id="unreal.RigUnit_FullbodyIK.debug_option"></a>

#### debug_option

```python
@debug_option.setter
def debug_option(value: FBIKDebugOption) -> None
```

<a id="unreal.PBIKBoneSetting"></a>