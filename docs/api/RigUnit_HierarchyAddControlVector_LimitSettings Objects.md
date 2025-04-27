## RigUnit_HierarchyAddControlVector_LimitSettings Objects

```python
class RigUnit_HierarchyAddControlVector_LimitSettings(StructBase)
```

Rig Unit Hierarchy Add Control Vector Limit Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DynamicHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``draw_limits`` (bool):  [Read-Write]
- ``limit_x`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_y`` (RigControlLimitEnabled):  [Read-Write]
- ``limit_z`` (RigControlLimitEnabled):  [Read-Write]
- ``max_value`` (Vector):  [Read-Write]
- ``min_value`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.__init__"></a>

#### __init__

```python
def __init__(limit_x: RigControlLimitEnabled = [False, False],
             limit_y: RigControlLimitEnabled = [False, False],
             limit_z: RigControlLimitEnabled = [False, False],
             min_value: Vector = [0.000000, 0.000000, 0.000000],
             max_value: Vector = [0.000000, 0.000000, 0.000000],
             draw_limits: bool = False) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.limit_x"></a>

#### limit_x

```python
@property
def limit_x() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.limit_x"></a>

#### limit_x

```python
@limit_x.setter
def limit_x(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.limit_y"></a>

#### limit_y

```python
@property
def limit_y() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.limit_y"></a>

#### limit_y

```python
@limit_y.setter
def limit_y(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.limit_z"></a>

#### limit_z

```python
@property
def limit_z() -> RigControlLimitEnabled
```

(RigControlLimitEnabled):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.limit_z"></a>

#### limit_z

```python
@limit_z.setter
def limit_z(value: RigControlLimitEnabled) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.min_value"></a>

#### min_value

```python
@property
def min_value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.min_value"></a>

#### min_value

```python
@min_value.setter
def min_value(value: Vector) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.max_value"></a>

#### max_value

```python
@property
def max_value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.max_value"></a>

#### max_value

```python
@max_value.setter
def max_value(value: Vector) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.draw_limits"></a>

#### draw_limits

```python
@property
def draw_limits() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_HierarchyAddControlVector_LimitSettings.draw_limits"></a>

#### draw_limits

```python
@draw_limits.setter
def draw_limits(value: bool) -> None
```

<a id="unreal.RigUnit_HierarchyAddControlVector_Settings"></a>