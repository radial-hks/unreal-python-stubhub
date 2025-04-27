## RigUnit_AimConstraintLocalSpaceOffset Objects

```python
class RigUnit_AimConstraintLocalSpaceOffset(RigUnit_HighlevelBaseMutable)
```

Orients an item such that its aim axis points towards a global target.
Note: This node operates in global space!

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_AimBone.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``advanced_settings`` (RigUnit_AimConstraint_AdvancedSettings):  [Read-Write]
- ``aim_axis`` (Vector):  [Read-Write] Child is rotated so that its AimAxis points to the parents
- ``child`` (RigElementKey):  [Read-Write] The name of the item to apply aim
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``filter`` (FilterOptionPerAxis):  [Read-Write] Filters the final rotation by axes based on the euler rotation order defined in the node's advanced settings
  If flipping is observed, try adjusting the rotation order
- ``maintain_offset`` (bool):  [Read-Write] Maintains the offset between child and weighted average of parents based on initial transforms
- ``parents`` (Array[ConstraintParent]):  [Read-Write]
- ``up_axis`` (Vector):  [Read-Write] Child is rotated around the AimAxis so that its UpAxis points to/Aligns with the WorldUp target
- ``weight`` (float):  [Read-Write]
- ``world_up`` (RigUnit_AimConstraint_WorldUp):  [Read-Write] Defines how Child should rotate around the AimAxis. This is the aim target for the UpAxis

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             child: RigElementKey = [RigElementType.NONE, "None"],
             maintain_offset: bool = False,
             filter: FilterOptionPerAxis = [True, True, True],
             aim_axis: Vector = [0.000000, 0.000000, 0.000000],
             up_axis: Vector = [0.000000, 0.000000, 0.000000],
             world_up: RigUnit_AimConstraint_WorldUp = [[
                 0.000000, 0.000000, 1.000000
             ], ControlRigVectorKind.DIRECTION, [RigElementType.NONE, "None"]],
             parents: Array[ConstraintParent] = [],
             advanced_settings: RigUnit_AimConstraint_AdvancedSettings = [[
                 False, 10.000000,
                 [[0.000000, 0.000000, 0.000000],
                  [-0.000000, 0.000000, 0.000000],
                  [1.000000, 1.000000, 1.000000]]
             ], EulerRotationOrder.XZY],
             weight: float = 0.000000) -> None
```

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write] The name of the item to apply aim

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.maintain_offset"></a>

#### maintain_offset

```python
@property
def maintain_offset() -> bool
```

(bool):  [Read-Write] Maintains the offset between child and weighted average of parents based on initial transforms

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.maintain_offset"></a>

#### maintain_offset

```python
@maintain_offset.setter
def maintain_offset(value: bool) -> None
```

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.filter"></a>

#### filter

```python
@property
def filter() -> FilterOptionPerAxis
```

(FilterOptionPerAxis):  [Read-Write] Filters the final rotation by axes based on the euler rotation order defined in the node's advanced settings
If flipping is observed, try adjusting the rotation order

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.filter"></a>

#### filter

```python
@filter.setter
def filter(value: FilterOptionPerAxis) -> None
```

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.aim_axis"></a>

#### aim_axis

```python
@property
def aim_axis() -> Vector
```

(Vector):  [Read-Write] Child is rotated so that its AimAxis points to the parents

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.aim_axis"></a>

#### aim_axis

```python
@aim_axis.setter
def aim_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.up_axis"></a>

#### up_axis

```python
@property
def up_axis() -> Vector
```

(Vector):  [Read-Write] Child is rotated around the AimAxis so that its UpAxis points to/Aligns with the WorldUp target

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.up_axis"></a>

#### up_axis

```python
@up_axis.setter
def up_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.world_up"></a>

#### world_up

```python
@property
def world_up() -> RigUnit_AimConstraint_WorldUp
```

(RigUnit_AimConstraint_WorldUp):  [Read-Write] Defines how Child should rotate around the AimAxis. This is the aim target for the UpAxis

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.world_up"></a>

#### world_up

```python
@world_up.setter
def world_up(value: RigUnit_AimConstraint_WorldUp) -> None
```

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.parents"></a>

#### parents

```python
@property
def parents() -> Array[ConstraintParent]
```

(Array[ConstraintParent]):  [Read-Write]

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.parents"></a>

#### parents

```python
@parents.setter
def parents(value: Array[ConstraintParent]) -> None
```

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.advanced_settings"></a>

#### advanced_settings

```python
@property
def advanced_settings() -> RigUnit_AimConstraint_AdvancedSettings
```

(RigUnit_AimConstraint_AdvancedSettings):  [Read-Write]

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.advanced_settings"></a>

#### advanced_settings

```python
@advanced_settings.setter
def advanced_settings(value: RigUnit_AimConstraint_AdvancedSettings) -> None
```

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.ConstraintParent"></a>