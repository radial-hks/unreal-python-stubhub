## RigUnit_HierarchyAddControlInteger_LimitSettings Objects

```python
class RigUnit_HierarchyAddControlInteger_LimitSettings(StructBase)
```

Rig Unit Hierarchy Add Control Integer Limit Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``draw_limits`` (bool):  [Read-Write]
- ``limit`` (RigControlLimitEnabled):  [Read-Write]
- ``max_value`` (int32):  [Read-Write]
- ``min_value`` (int32):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.__init__"></a>

#### __init__

```python
def __init__(limit: RigControlLimitEnabled = [False, False],
             min_value: int = 0,
             max_value: int = 0,
             draw_limits: bool = False) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.limit"></a>

#### limit

```python
@property
def limit() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.limit"></a>

#### limit

```python
@limit.setter
def limit(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.min_value"></a>

#### min_value

```python
@property
def min_value() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.min_value"></a>

#### min_value

```python
@min_value.setter
def min_value(value: int) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.max_value"></a>

#### max_value

```python
@property
def max_value() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.max_value"></a>

#### max_value

```python
@max_value.setter
def max_value(value: int) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.draw_limits"></a>

#### draw_limits

```python
@property
def draw_limits() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlInteger_LimitSettings.draw_limits"></a>

#### draw_limits

```python
@draw_limits.setter
def draw_limits(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlInteger_Settings"></a>