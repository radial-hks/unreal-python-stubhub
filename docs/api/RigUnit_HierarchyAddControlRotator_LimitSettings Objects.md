## RigUnit_HierarchyAddControlRotator_LimitSettings Objects

```python
class RigUnit_HierarchyAddControlRotator_LimitSettings(StructBase)
```

Rig Unit Hierarchy Add Control Rotator Limit Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``draw_limits`` (bool):  [Read-Write]
- ``limit_pitch`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_roll`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_yaw`` (RigControlLimitEnabled):  [Read-Write]
- ``max_value`` (Rotator):  [Read-Write]
- ``min_value`` (Rotator):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.__init__"></a>

#### __init__

```python
def __init__(limit_pitch: RigControlLimitEnabled = [False, False],
             limit_yaw: RigControlLimitEnabled = [False, False],
             limit_roll: RigControlLimitEnabled = [False, False],
             min_value: Rotator = [0.000000, 0.000000, 0.000000],
             max_value: Rotator = [0.000000, 0.000000, 0.000000],
             draw_limits: bool = False) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.limit_pitch"></a>

#### limit_pitch

```python
@property
def limit_pitch() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.limit_pitch"></a>

#### limit_pitch

```python
@limit_pitch.setter
def limit_pitch(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.limit_yaw"></a>

#### limit_yaw

```python
@property
def limit_yaw() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.limit_yaw"></a>

#### limit_yaw

```python
@limit_yaw.setter
def limit_yaw(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.limit_roll"></a>

#### limit_roll

```python
@property
def limit_roll() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.limit_roll"></a>

#### limit_roll

```python
@limit_roll.setter
def limit_roll(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.min_value"></a>

#### min_value

```python
@property
def min_value() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.min_value"></a>

#### min_value

```python
@min_value.setter
def min_value(value: Rotator) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.max_value"></a>

#### max_value

```python
@property
def max_value() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.max_value"></a>

#### max_value

```python
@max_value.setter
def max_value(value: Rotator) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.draw_limits"></a>

#### draw_limits

```python
@property
def draw_limits() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlRotator_LimitSettings.draw_limits"></a>

#### draw_limits

```python
@draw_limits.setter
def draw_limits(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlRotator_Settings"></a>